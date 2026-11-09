"""Generate the EPISODE-001 production docs from the single sources (assemble.py EDL, e001_spec.py, jobs.json, vospan.json).
Writes: storyboard.md, audio-cue-sheet.md, animation-batch.md, dialogue.md (line table section), run-log jobs appendix."""
import json, sys, pathlib, re
T = pathlib.Path(__file__).resolve().parent; EP = T.parent
sys.path.insert(0, str(T))
import assemble as A, e001_spec as S
JOBS = {**S.KNOWN, **json.loads((T / "jobs.json").read_text())}
VSP = json.loads((T / "vospan.json").read_text())

def rel(p):
    p = pathlib.Path(p)
    try: return str(p.relative_to(EP))
    except ValueError: return "../../" + str(p.relative_to(A.ROOT))
def tc(t): m, s = divmod(t, 60); return f"{int(m)}:{s:04.1f}"
def shot_id(s):
    src = s.get("img") or s.get("src") or s.get("A")
    if s["k"] == "card": return "TITLE CARD"
    if s["k"] == "black": return "BLACK"
    n = pathlib.Path(src).name
    m = re.search(r"(S\d\d_SH\d\d)", n)
    return (m.group(1) if m else n.split(".")[0]) + (" (POW-001 reuse)" if "POW001" in n else "")
def kind(s):
    return {"still": "STILL + digital move", "clip": "CLIP", "xfade": "STILL x2 + crossfade", "card": "CARD", "black": "BLACK"}[s["k"]]
def move(s):
    if s["k"] == "still":
        z0, z1 = s["z"]; pan = "" if s["c"] == s["c1"] else f", pan {s['c'][0]:.2f}→{s['c1'][0]:.2f}"
        return f"push {z0:.2f}→{z1:.2f} at ({s['c'][0]:.2f},{s['c'][1]:.2f}){pan}"
    if s["k"] == "clip":
        return f"source {s['a']}–{s['b']} s at {s['speed']}×" + (f" + {s['hold']} s hold" if s["hold"] else "") + (" (motion-interpolated)" if s["speed"] < 0.95 else "")
    if s["k"] == "xfade": return f"crossfade at {s['at']} s over {s['xd']} s; push {s['z'][0]}→{s['z'][1]}"
    if s["k"] == "card": return " / ".join(s["lines"])
    return ""

rows, cues, t = [], [], 0.0
for name, shots, cs in A.SC:
    st = t
    for i, s in enumerate(shots):
        d = A.nfr(s["dur"]) / A.FPS
        src = s.get("img") or s.get("src") or s.get("A")
        rows.append((name, i + 1, tc(t), round(d, 2), shot_id(s), kind(s), move(s), rel(src) if src else "—"))
        t += d
    for c in cs: cues.append((st + c["at"], name, c))
total = t
LINES = {f"E001_VO_{spk.lower()}_L0{a[1:]}_v01.wav": (a, sc, spk, txt) for a, sc, spk, txt in S.LINES}

# ---------- storyboard.md
sb = ["# Storyboard — EPISODE-001 \"The Early Shelf\"", "",
      f"Status: **LOCKED FOR REVIEW RENDER v01 (2026-11-09).** Generated from the edit decision list in `tools/assemble.py` + `tools/edl_tail.py`.",
      f"Total runtime: **{tc(total)}** ({total:.1f} s) · {len(rows)} shots · 1920×1080 · 30 fps.", "",
      "Types: **CLIP** = AI animation (grok_video_v15_lite) · **STILL** = keyframe with a digital camera move · **POW-001 reuse** = asset from the approved proof-of-work.",
      "Dialogue is staged over listeners, backs, profiles, or inserts (no lip-sync).", "",
      "| Scene | # | In | Dur (s) | Shot | Type | Camera / timing | Source |", "|---|---|---|---|---|---|---|---|"]
sb += [f"| {a} | {b} | {c} | {d} | {e} | {f} | {g} | `{h}` |" for a, b, c, d, e, f, g, h in rows]
(EP / "storyboard.md").write_text("\n".join(sb) + "\n")

# ---------- audio-cue-sheet.md
ac = ["# Audio cue sheet — EPISODE-001", "", f"Generated from the EDL. Times are absolute in the review render (total {tc(total)}).",
      "Mix: dialogue on top; music ducked about 7 dB under speech; loudness normalized to -16 LUFS integrated, -1.5 dBTP.", "",
      "| Time | Scene | Type | Asset | Gain (dB) | Notes |", "|---|---|---|---|---|---|"]
for at, sc, c in sorted(cues, key=lambda x: x[0]):
    f = pathlib.Path(c["f"]).name
    if c["k"] == "vo":
        a, _, spk, txt = LINES.get(f, ("", "", "", ""))
        ac.append(f"| {tc(at)} | {sc} | VO {spk} | `{f}` | {c['gain']} | {a}: \"{txt.replace(chr(10), ' ')[:90]}\" |")
    elif c["k"] == "sfx":
        ac.append(f"| {tc(at)} | {sc} | SFX | `{f}` | {c['gain']} | {('dur ' + str(c['dur']) + ' s') if c['dur'] else ''} |")
    else:
        ac.append(f"| {tc(at)} | {sc} | {'BED' if c.get('loop') else 'MUSIC'} | `{f}` | {c['gain']} | {c['dur']} s from {c['inn']} s, fade {c['fin']}/{c['fout']} s{', ducked' if c['duck'] else ''} |")
(EP / "audio-cue-sheet.md").write_text("\n".join(ac) + "\n")

# ---------- animation-batch.md
ab = ["# Animation batch — EPISODE-001", "", "Model: grok_video_v15_lite, 720p (1280×704 output, 24 fps), start image = the verified keyframe. 1 credit per second.",
      "Video negative appended to every prompt: `" + S.NEGV + "`", "",
      "| Clip | Start keyframe | Dur (s) | Prompt (motion) | Job ID | File | Used in edit |", "|---|---|---|---|---|---|---|"]
for k, (d, p) in S.CLIP.items():
    used = [f"{r[0]} #{r[1]} ({r[6]})" for r in rows if r[4] == k and r[5] == "CLIP"]
    ab.append(f"| {k} | `{JOBS.get(k, '—')}` | {d} | {p.split(' Avoid:')[0]} | `{JOBS.get(k + '_CLIP', '—')}` | `clips/E001_{k}_CLIP_v01.mp4` | {'; '.join(used) or 'not used'} |")
ab += ["", "Reused from POW-001 (no new spend): `POW001_SH02_CLIP_v01` (clock insert, cut at 1.5 s + hold), `SH05`, `SH06`, `SH07`."]
(EP / "animation-batch.md").write_text("\n".join(ab) + "\n")

# ---------- dialogue table (appended section is regenerated each time)
dl = ["", "## Lines as generated (Prompt 08)", "",
      "Voices (seed_audio presets, 48 kHz): **NARR + WREN = Annie** (owner-delegated pick, POW-001) · **IDA = Vera** (speech rate -8) · **THEO = Archie**.",
      "Ida and Theo voices were chosen by measured pitch (Vera 172 Hz, narrow range; Archie 137 Hz, narrow range): `PROPOSED — NEEDS APPROVAL` (owner should audition).", "",
      "| Line | Scene | Speaker | Text | File | Speech (s) | In edit at |", "|---|---|---|---|---|---|---|"]
vo_at = {pathlib.Path(c["f"]).name: at for at, sc, c in cues if c["k"] == "vo"}
words = {}
for f, (a, sc, spk, txt) in LINES.items():
    sp = VSP.get(f, {}); words[spk] = words.get(spk, 0) + len(re.findall(r"[\w'-]+", txt))
    dl.append(f"| {a} | {sc} | {spk} | {txt.replace(chr(10), ' ')} | `audio/dialogue/{f}` | {sp.get('end', 0) - sp.get('start', 0):.2f} | {tc(vo_at[f]) if f in vo_at else 'NOT PLACED'} |")
dl += ["", f"Word count: {words} · **total {sum(words.values())}** (below the 650–750 guide by design; see `script.md`)."]
d = (EP / "dialogue.md").read_text().split("\n## Lines as generated")[0].rstrip() + "\n" + "\n".join(dl) + "\n"
(EP / "dialogue.md").write_text(d)
print("docs written; total", tc(total), len(rows), "shots")
