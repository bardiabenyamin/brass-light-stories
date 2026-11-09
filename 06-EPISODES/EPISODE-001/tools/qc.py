"""QC for an EPISODE-001 render: ffprobe spec check, loudness, black/freeze detection, and a contact sheet of every shot
(frame at each shot's midpoint, labelled). Contact sheets go to renders/tmp/qc/ (not committed)."""
import json, subprocess, sys, pathlib
T = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(T))
import assemble as A
render = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else A.EP / "renders/E001_RENDER_review_v01.mp4"
Q = A.TMP / "qc"; Q.mkdir(exist_ok=True)
def sh(cmd): return subprocess.run(cmd, capture_output=True, text=True).stdout + subprocess.run(cmd, capture_output=True, text=True).stderr
probe = json.loads(subprocess.run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(render)], capture_output=True, text=True).stdout)
v = next(s for s in probe["streams"] if s["codec_type"] == "video"); a = next(s for s in probe["streams"] if s["codec_type"] == "audio")
res = {"file": str(render.name), "size_MB": round(int(probe["format"]["size"]) / 1e6, 1), "duration_s": round(float(probe["format"]["duration"]), 2),
       "video": f'{v["codec_name"]} {v["width"]}x{v["height"]} {v["r_frame_rate"]} {v["pix_fmt"]}', "audio": f'{a["codec_name"]} {a["sample_rate"]} Hz {a["channels"]} ch'}
lo = subprocess.run(["ffmpeg", "-i", str(render), "-map", "0:a:0", "-af", "ebur128=peak=true:framelog=quiet", "-f", "null", "-"], capture_output=True, text=True).stderr
res["loudness"] = " ".join(l.strip() for l in lo.splitlines() if l.strip().startswith(("I:", "LRA:", "Peak:")))
bd = subprocess.run(["ffmpeg", "-i", str(render), "-map", "0:v:0", "-vf", "blackdetect=d=0.4:pix_th=0.06", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
res["black_segments"] = [l.split("blackdetect] ")[1] for l in bd.splitlines() if "black_start" in l]
fz = subprocess.run(["ffmpeg", "-i", str(render), "-map", "0:v:0", "-vf", "freezedetect=n=0.0008:d=2.5", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
res["freezes"] = [l.split("] ")[1] for l in fz.splitlines() if "freeze_start" in l or "freeze_duration" in l]
sl = subprocess.run(["ffmpeg", "-i", str(render), "-map", "0:a:0", "-af", "silencedetect=n=-50dB:d=1.5", "-f", "null", "-"], capture_output=True, text=True).stderr
res["silences"] = [l.split("] ")[1] for l in sl.splitlines() if "silence_start" in l or "silence_duration" in l]
# midpoint frame of every shot
t, idx = 0.0, 0; frames = []
for name, shots, _ in A.SC:
    for i, s in enumerate(shots):
        d = A.nfr(s["dur"]) / A.FPS; mid = t + d / 2; idx += 1
        out = Q / f"f{idx:03d}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{mid:.2f}", "-i", str(render), "-frames:v", "1", "-vf",
                        f"scale=480:270,drawtext=fontfile={A.FONT}:text='{idx} {name} {int(mid // 60)}\\:{mid % 60:04.1f}':fontcolor=white:fontsize=18:box=1:boxcolor=black@0.6:x=6:y=6", str(out)], check=True)
        frames.append(out); t += d
for k in range(0, len(frames), 16):
    grp = frames[k:k + 16]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(Q / "f%03d.png"), "-vf", f"select='between(n\\,{k}\\,{k + len(grp) - 1})',tile=4x4", "-frames:v", "1", str(Q / f"sheet_{k // 16 + 1}.png")], check=True)
json.dump(res, open(Q / "qc.json", "w"), indent=1); print(json.dumps(res, indent=1))
