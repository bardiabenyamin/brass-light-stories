"""EPISODE-001 assembly (local, free): picture with ffmpeg, sound mixed in numpy, loudness with ffmpeg.
Spec: 1920x1080, 30 fps, H.264 yuv420p, AAC 48 kHz stereo, about -16 LUFS.
Usage: python3 assemble.py [--only-audio] [--from N]
Outputs: renders/E001_RENDER_master_v01.mp4 (crf 18, not committed if > 95 MB)
         renders/E001_RENDER_review_v01.mp4 (2-pass, sized under 95 MB, committed)
The edit decision list (EDL) below is the single source for shot order, durations and audio cue times."""
import json, subprocess, sys, wave, pathlib
import numpy as np

T = pathlib.Path(__file__).resolve().parent
EP = T.parent; ROOT = EP.parent.parent; POW = ROOT / "04-TESTS/POW-001"
TMP = EP / "renders/tmp"; TMP.mkdir(parents=True, exist_ok=True)
SR, FPS = 48000, 30
VSPAN = json.load(open(T / "vospan.json"))

def KF(s, v="v01"): return EP / f"images/keyframes/E001_{s}_KF_{v}.png"
def CL(s): return EP / f"clips/E001_{s}_CLIP_v01.mp4"
PKF = lambda n: POW / f"keyframes/{n}.png"
PCL = lambda n: POW / f"clips/POW001_{n}_CLIP_v01.mp4"
VO = lambda n: EP / f"audio/dialogue/E001_VO_{n}_v01.wav"
SFX = lambda n: EP / f"audio/sfx/E001_SFX_{n}_v01.wav"
MUS = lambda n: EP / f"audio/music/E001_MUS_{n}_v01.wav"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
GROK = "1252:704:14:0"          # grok_video_v15_lite 1280x704 -> 16:9
POWC = "1144:644:0:30"          # POW clips: also removes the lit lamp at the right edge

# ---------------------------------------------------------------- shot constructors
def still(img, dur, z=(1.0, 1.06), c=(0.5, 0.5), c1=None, fin=0, fout=0):
    return dict(k="still", img=img, dur=dur, z=z, c=c, c1=c1 or c, fin=fin, fout=fout)
def clip(src, a, b, speed=1.0, crop=GROK, hold=0.0, fin=0, fout=0):
    return dict(k="clip", src=src, a=a, b=b, speed=speed, crop=crop, hold=hold, fin=fin, fout=fout, dur=(b - a) / speed + hold)
def xf(imgA, imgB, dur, at, xd, z=(1.0, 1.06), c=(0.5, 0.5), fin=0, fout=0):
    return dict(k="xfade", A=imgA, B=imgB, dur=dur, at=at, xd=xd, z=z, c=c, fin=fin, fout=fout)
def card(lines, dur): return dict(k="card", lines=lines, dur=dur)
def black(dur): return dict(k="black", dur=dur)
# ---------------------------------------------------------------- audio cue constructors (times relative to scene start)
def vo(name, at, inn=None, gain=0.0): return dict(k="vo", f=VO(name), at=at, inn=inn, gain=gain, name=name)
def sfx(f, at, gain=0.0, dur=None, fin=0.02, fout=0.05, inn=0.0): return dict(k="sfx", f=f, at=at, gain=gain, dur=dur, fin=fin, fout=fout, inn=inn)
def mus(f, at, dur, inn=0.0, gain=-18.0, fin=2.0, fout=2.0, duck=True): return dict(k="mus", f=f, at=at, dur=dur, inn=inn, gain=gain, fin=fin, fout=fout, duck=duck)
def bed(f, at, dur, gain=-6.0, fin=1.0, fout=1.0): return dict(k="mus", f=f, at=at, dur=dur, inn=0.0, gain=gain, fin=fin, fout=fout, duck=False, loop=True)

MID, WARM = MUS("midnight"), MUS("warm")
SC = []
# S01 cold open: Monday midnight (reuses POW-001 assets)
SC.append(("S01", [
    clip(PCL("SH02"), 0, 1.5, crop=GROK, hold=1.5, fin=0.5),
    still(PKF("POW001_SH01_KF_v01"), 5.0, (1.00, 1.08), (0.49, 0.40)),
    xf(PKF("POW001_SH03_KF_v02"), PKF("POW001_SH04_KF_v01_retouch"), 7.0, 2.5, 1.5, (1.0, 1.06), (0.5, 0.7)),
    card(["THE EARLY SHELF", "Episode 1"], 4.0)],
  [sfx(SFX("tick"), 0.0, -4), sfx(SFX("tick"), 1.0, -4), sfx(SFX("bell"), 1.5, -2),
   vo("narr_L000", 3.6), sfx(SFX("shimmer"), 9.3, -2),
   mus(MID, 0.0, 19.0, 0.0, -17, 2.0, 3.0), bed(SFX("wind"), 3.0, 5.0, -10)]))
# S02 platform, Monday 6:14, golden hour
SC.append(("S02", [
    clip(CL("S02_SH01"), 0, 3.2, 0.8, fin=0.4),
    clip(CL("S02_SH02"), 0, 3.0, 0.8),
    still(KF("S02_SH03", "v02"), 8.25, (1.0, 1.22), (0.49, 0.36)),
    still(KF("S02_SH04"), 5.0, (1.0, 1.08), (0.5, 0.4)),
    still(KF("S02_SH05"), 3.0, (1.02, 1.08), (0.45, 0.4)),
    still(KF("S02_SH06"), 4.5, (1.0, 1.06), (0.5, 0.5)),
    clip(CL("S02_SH07"), 0, 3.0, 0.5),
    still(KF("S02_SH08"), 8.5, (1.0, 1.12), (0.32, 0.4))],
  [sfx(SFX("train_arrive"), 0.0, -4), bed(SFX("wind"), 0, 43.0, -8),
   vo("narr_L001", 1.0), vo("ida_L002", 21.6), vo("narr_L003", 24.5),
   mus(WARM, 0.5, 42.5, 0.0, -16, 3.0, 3.0)]))
# S03 office, Monday evening, lamplight
SC.append(("S03", [
    still(KF("S03_SH01"), 7.5, (1.0, 1.08), (0.5, 0.5), fin=0.5),
    still(KF("S03_SH02"), 7.5, (1.15, 1.15), (0.42, 0.5), (0.58, 0.5)),
    still(KF("S03_SH03"), 9.2, (1.0, 1.12), (0.45, 0.5)),
    still(KF("S03_SH04"), 3.2, (1.0, 1.05), (0.6, 0.4)),
    still(KF("S03_SH05"), 2.5, (1.0, 1.08), (0.5, 0.8)),
    clip(CL("S03_SH06"), 0, 3.0, 0.72),
    still(KF("S03_SH04"), 6.53, (1.3, 1.42), (0.62, 0.33), fout=0.7)],
  [bed(SFX("roomtone"), 0, 40.6, -6),
   vo("ida_L004", 0.9, inn=1.0), vo("narr_L005", 7.8), vo("wren_L006", 24.6), vo("ida_L007", 26.0, inn=0.85),
   vo("wren_L008", 27.7), vo("ida_L009", 30.2), vo("narr_L010", 34.6),
   mus(WARM, 0.0, 30.0, 42.0, -19, 2.0, 4.0), mus(MID, 33.5, 7.1, 0.0, -21, 2.5, 1.5)]))
# S04 kitchen, Monday night, lamplight ("Nora")
SC.append(("S04", [
    still(KF("S04_SH01"), 4.5, (1.0, 1.08), (0.5, 0.55), fin=0.6),
    still(KF("S04_SH02"), 2.8, (1.0, 1.05), (0.5, 0.45)),
    still(KF("S04_SH03"), 5.3, (1.0, 1.08), (0.5, 0.4)),
    still(KF("S04_SH02"), 3.7, (1.15, 1.22), (0.45, 0.4), fout=0.8)],
  [bed(SFX("roomtone"), 0, 16.3, -6)] + [sfx(SFX("tick"), t, -22) for t in np.arange(0.5, 16.0, 1.0)] +
  [vo("ida_L011", 1.2, inn=1.6), vo("wren_L012", 4.9), vo("ida_L013", 7.8, inn=1.1), vo("narr_L014", 11.0)]))
# S05 kitchen -> hall -> office, Monday midnight (Mom's song; the umbrella arrives; Ida watches)
SC.append(("S05", [
    still(KF("S05_SH01"), 6.0, (1.0, 1.12), (0.25, 0.45), fin=0.8),
    clip(CL("S05_SH01"), 0.2, 3.6, 0.4),
    still(TMP / "S05_SH01_last.png", 4.5, (1.0, 1.06), (0.5, 0.45)),
    clip(PCL("SH02"), 0, 1.5, crop=GROK, hold=1.5),
    still(KF("S05_SH02", "v02"), 4.0, (1.0, 1.15), (0.55, 0.6)),
    clip(PCL("SH05"), 0, 4.3, crop=POWC),
    still(PKF("POW001_SH04_KF_v01_retouch"), 3.9, (1.0, 1.05), (0.5, 0.7)),
    still(KF("S05_SH03"), 4.4, (1.0, 1.15), (0.6, 0.55)),
    clip(PCL("SH06"), 0, 3.2, crop=POWC),
    clip(PCL("SH07"), 0, 5.0, crop="1120:630:0:37", fout=0.8),
    black(0.5)],
  [bed(SFX("roomtone"), 0, 47.3, -6), vo("narr_L015", 0.6), mus(MUS("momsong"), 12.1, 10.0, 0.0, -3, 0.05, 1.0, duck=False),
   sfx(SFX("tick"), 19.0, -6), sfx(SFX("tick"), 20.0, -6), sfx(SFX("bell"), 20.5, -2), vo("narr_L016", 21.1),
   vo("narr_L017", 26.4), sfx(SFX("shimmer"), 29.6, -3), mus(MID, 21.5, 25.8, 8.0, -18, 2.0, 2.0)]))
# S06 platform, Tuesday 6:14 after rain; the umbrella is lost and its early copy vanishes (R2)
SC.append(("S06", [
    still(KF("S06_SH01"), 6.5, (1.0, 1.08), (0.5, 0.45), fin=0.8),
    still(KF("S06_SH02"), 7.0, (1.0, 1.06), (0.4, 0.5)),
    still(KF("S06_SH03"), 6.0, (1.0, 1.08), (0.6, 0.4)),
    clip(CL("S06_SH04"), 0, 4.0, 0.8),
    xf(KF("S06_SH05"), KF("S03_SH05"), 9.0, 1.5, 2.0, (1.0, 1.08), (0.5, 0.8), fout=0.6)],
  [bed(SFX("drips"), 0, 24.5, -4), bed(SFX("wind"), 0, 24.5, -12), vo("narr_L018", 0.8), sfx(SFX("train_arrive"), 4.5, -12),
   sfx(SFX("train_depart"), 19.5, -6), vo("narr_L019", 19.8), sfx(SFX("shimmer"), 25.6, -6), bed(SFX("roomtone"), 24.5, 9.0, -6),
   mus(WARM, 0.0, 24.5, 10.0, -20, 2.0, 2.5)]))
# S07 office, Tuesday evening: Theo hands it in
SC.append(("S07", [
    clip(CL("S07_SH01"), 0, 3.0, 0.75, fin=0.5),
    still(KF("S07_SH02"), 5.0, (1.0, 1.06), (0.55, 0.4)),
    still(KF("S07_SH03"), 8.0, (1.0, 1.08), (0.4, 0.45)),
    still(KF("S05_SH03"), 1.6, (1.15, 1.2), (0.55, 0.55)),
    still(KF("S07_SH04"), 1.7, (1.0, 1.06), (0.5, 0.6)),
    still(KF("S06_SH05"), 2.7, (1.35, 1.42), (0.5, 0.78))],
  [bed(SFX("roomtone"), 0, 23.0, -6), sfx(SFX("drips"), 0.0, -10, dur=4.0, fout=1.0),
   vo("theo_L020", 0.6), vo("narr_L021", 4.3), vo("theo_L022", 9.3), vo("narr_L023", 17.0)]))
EDL_TAIL = T / "edl_tail.py"   # S08, S09 and the end card are appended from this file once their lines are measured
exec(EDL_TAIL.read_text())

# ---------------------------------------------------------------- picture
V = ["-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), "-an"]
def run(cmd): subprocess.run(cmd, check=True)
def nfr(d): return int(round(d * FPS))
def fades(s, n):
    f = []
    if s.get("fin"): f.append(f"fade=in:st=0:d={s['fin']}")
    if s.get("fout"): f.append(f"fade=out:st={n / FPS - s['fout']:.3f}:d={s['fout']}")
    return ("," + ",".join(f)) if f else ""
CROP169 = "crop='min(iw,ih*16/9)':'min(ih,iw*9/16)':'(iw-min(iw,ih*16/9))/2':'(ih-min(ih,iw*9/16))/2'"
def zp(n, z, c, c1):
    z0, z1 = z; (x0, y0), (x1, y1) = c, c1; p = f"on/{max(n - 1, 1)}"
    zz = f"({z0}+({z1}-{z0})*{p})"
    x = f"max(0,min(iw-iw/zoom,iw*({x0}+({x1}-{x0})*{p})-iw/zoom/2))"
    y = f"max(0,min(ih-ih/zoom,ih*({y0}+({y1}-{y0})*{p})-ih/zoom/2))"
    return f"zoompan=z='{zz}':x='{x}':y='{y}':d={n}:s=1920x1080:fps={FPS}"
import hashlib
def render(i, s):
    h = hashlib.md5(json.dumps(s, sort_keys=True, default=str).encode()).hexdigest()[:10]
    final = TMP / f"seg_{h}.mp4"; n = nfr(s["dur"])
    if final.exists(): return final
    out = TMP / f"seg_{h}.part.mp4"
    if s["k"] == "still":
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(s["img"]), "-vf",
             f"{CROP169},scale=3840:2160:flags=lanczos,{zp(n, s['z'], s['c'], s['c1'])},setsar=1{fades(s, n)}", "-frames:v", str(n)] + V + [str(out)])
    elif s["k"] == "clip":
        slow = s["speed"] < 0.95
        mi = ",minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" if slow else ",fps=30"
        hold = f",tpad=stop_mode=clone:stop_duration={s['hold']}" if s["hold"] else ""
        vf = (f"trim={s['a']}:{s['b']},setpts=(PTS-STARTPTS)/{s['speed']},crop={s['crop']},scale=1280:720:flags=lanczos{mi},"
              f"scale=1920:1080:flags=lanczos,setsar=1{hold}{fades(s, n)}")
        run(["ffmpeg", "-v", "error", "-y", "-i", str(s["src"]), "-map", "0:v:0", "-vf", vf, "-frames:v", str(n)] + V + [str(out)])
    elif s["k"] == "xfade":
        a, b = TMP / f"seg_{h}a.mp4", TMP / f"seg_{h}b.mp4"
        za, zb = s["z"][0], s["z"][1]; zm = za + (zb - za) * (s["at"] + s["xd"]) / s["dur"]
        na = nfr(s["at"] + s["xd"]); nb = n - nfr(s["at"])
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(s["A"]), "-vf", f"{CROP169},scale=3840:2160:flags=lanczos,{zp(na, (za, zm), s['c'], s['c'])},setsar=1", "-frames:v", str(na)] + V + [str(a)])
        zs = za + (zb - za) * s["at"] / s["dur"]
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(s["B"]), "-vf", f"{CROP169},scale=3840:2160:flags=lanczos,{zp(nb, (zs, zb), s['c'], s['c'])},setsar=1", "-frames:v", str(nb)] + V + [str(b)])
        run(["ffmpeg", "-v", "error", "-y", "-i", str(a), "-i", str(b), "-filter_complex",
             f"[0:v][1:v]xfade=transition=fade:duration={s['xd']}:offset={s['at']},format=yuv420p{fades(s, n)}", "-frames:v", str(n)] + V + [str(out)])
    elif s["k"] == "card":
        l1, l2 = s["lines"]; d = s["dur"]
        txt = (f"drawtext=fontfile={FONT}:text='{l1}':fontcolor=0xD8B46A:fontsize=92:x=(w-tw)/2:y=(h-th)/2-40,"
               f"drawtext=fontfile={FONT}:text='{l2}':fontcolor=0xBFAE8C:fontsize=40:x=(w-tw)/2:y=(h/2)+50")
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=0x0B0D12:s=1920x1080:r={FPS}", "-vf",
             f"{txt},fade=in:st=0:d=0.8,fade=out:st={d - 0.9}:d=0.9", "-frames:v", str(n)] + V + [str(out)])
    elif s["k"] == "black":
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c=black:s=1920x1080:r={FPS}", "-frames:v", str(n)] + V + [str(out)])
    out.rename(final)
    return final

# ---------------------------------------------------------------- sound (numpy)
def load(p):
    w = wave.open(str(p)); ch, sr, n = w.getnchannels(), w.getframerate(), w.getnframes()
    x = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768
    x = x.reshape(-1, ch)
    if ch == 1: x = np.repeat(x, 2, 1)
    assert sr == SR, (p, sr)
    return x
def db(g): return 10 ** (g / 20)
def place(buf, x, t):
    i = int(round(t * SR)); j = min(len(buf), i + len(x))
    if j > i: buf[i:j] += x[: j - i]

def mix(timeline, total):
    vo_buf = np.zeros((int(total * SR) + SR, 2), np.float32); mus_buf = vo_buf.copy(); fx_buf = vo_buf.copy(); duck_buf = vo_buf.copy()
    log = []
    for t0, c in timeline:
        if c["k"] == "vo":
            x = load(c["f"]); sp = VSPAN[c["f"].name]
            inn = c["inn"] if c["inn"] is not None else max(0.0, sp["start"] - 0.05)
            x = x[int(inn * SR):int((sp["end"] + 0.25) * SR)]
            fl = int(0.01 * SR); x[:fl] *= np.linspace(0, 1, fl)[:, None]; x[-fl * 5:] *= np.linspace(1, 0, fl * 5)[:, None]
            place(vo_buf, x * db(c["gain"]), t0 + c["at"]); log.append((round(t0 + c["at"], 2), c["name"]))
        elif c["k"] == "sfx":
            if not c["f"].exists(): print("MISSING SFX", c["f"].name); continue
            x = load(c["f"])[int(c["inn"] * SR):]
            if c["dur"]: x = x[: int(c["dur"] * SR)]
            n = len(x); fi, fo = int(c["fin"] * SR), int(c["fout"] * SR)
            if fi: x[:fi] *= np.linspace(0, 1, fi)[:, None]
            if fo: x[-fo:] *= np.linspace(1, 0, fo)[:, None]
            place(fx_buf, x * db(c["gain"]), t0 + c["at"])
        elif c["k"] == "mus":
            if not c["f"].exists(): print("MISSING", c["f"].name); continue
            src = load(c["f"]); need = int(c["dur"] * SR); start = int(c["inn"] * SR)
            x = np.concatenate([src[start:]] + [src] * (1 + need // len(src)))[:need].copy()
            fi, fo = int(c["fin"] * SR), int(c["fout"] * SR)
            if fi: x[:fi] *= np.linspace(0, 1, fi)[:, None]
            if fo: x[-fo:] *= np.linspace(1, 0, fo)[:, None]
            place(duck_buf if c["duck"] else mus_buf, x * db(c["gain"]), t0 + c["at"])
    # duck music under dialogue: envelope of VO presence, smoothed, -7 dB at full presence
    env = np.abs(vo_buf).max(1); hop = 480
    pres = np.array([env[i:i + hop].max() for i in range(0, len(env), hop)]) > 0.02
    k = np.ones(40) / 40; sm = np.convolve(pres.astype(float), k, "same"); sm = np.clip(sm * 1.5, 0, 1)
    g = 1 - (1 - db(-7)) * np.repeat(sm, hop)[: len(env)]
    out = vo_buf + fx_buf + mus_buf + duck_buf * g[:, None]
    return out[: int(total * SR)], log

def save_wav(p, x):
    x = np.clip(x, -1, 1)
    with wave.open(str(p), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    only_audio = "--only-audio" in sys.argv
    # frame grab used as a still in S05
    run(["ffmpeg", "-v", "error", "-y", "-ss", "3.58", "-i", str(CL("S05_SH01")), "-map", "0:v:0", "-frames:v", "1", "-vf", f"crop={GROK}", str(TMP / "S05_SH01_last.png")])
    shots, timeline, t = [], [], 0.0; marks = []
    for name, sh, cues in SC:
        d = sum(nfr(s["dur"]) for s in sh) / FPS
        marks.append((name, round(t, 2), round(d, 2)))
        for c in cues: timeline.append((t, c))
        shots += sh; t += d
    total = t
    print("scenes:", marks, "total", round(total, 2))
    if not only_audio:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(3) as ex: segs = list(ex.map(lambda a: render(*a), enumerate(shots)))
        (TMP / "list.txt").write_text("".join(f"file '{p.name}'\n" for p in segs))
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(TMP / "list.txt"), "-c", "copy", str(TMP / "picture.mp4")])
    if "--picture-only" in sys.argv: print("picture done"); sys.exit(0)
    m, log = mix(timeline, total)
    save_wav(TMP / "mix_raw.wav", m * 0.8)
    run(["ffmpeg", "-v", "error", "-y", "-i", str(TMP / "mix_raw.wav"), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000", "-ar", "48000", "-c:a", "pcm_s16le", str(TMP / "mix.wav")])
    json.dump({"scenes": marks, "vo": log, "total": total}, open(TMP / "timeline.json", "w"), indent=1)
    master = EP / "renders/E001_RENDER_master_v01.mp4"; review = EP / "renders/E001_RENDER_review_v01.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-i", str(TMP / "picture.mp4"), "-i", str(TMP / "mix.wav"), "-map", "0:v:0", "-map", "1:a:0",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(master)])
    # review copy: 2-pass, about 2.2 Mb/s video so that ~5 min stays well under 95 MB
    for p in (1, 2):
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(master), "-c:v", "libx264", "-preset", "slow", "-b:v", "2200k", "-pass", str(p),
               "-passlogfile", str(TMP / "x264"), "-pix_fmt", "yuv420p", "-r", str(FPS)]
        cmd += (["-an", "-f", "mp4", "/dev/null"] if p == 1 else ["-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", str(review)])
        run(cmd)
    print("done", master, review)
