"""Print speech span (first/last sample above threshold) and internal pauses for each VO file."""
import numpy as np, wave, glob, sys, json
def load(p):
    w = wave.open(p); n = w.getnframes(); ch = w.getnchannels(); sr = w.getframerate()
    x = np.frombuffer(w.readframes(n), dtype=np.int16).astype(float) / 32768
    return (x.reshape(-1, ch).mean(1) if ch > 1 else x), sr
out = {}
for p in sorted(glob.glob(sys.argv[1] if len(sys.argv) > 1 else "audio/dialogue/*.wav")):
    x, sr = load(p); hop = int(.01 * sr)
    e = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)])
    th = max(e.max() * 0.03, 1e-4); on = np.where(e > th)[0]
    s, t = on[0] * .01, (on[-1] + 1) * .01
    # pauses > 0.35 s inside the span
    gaps = []; run = 0
    for i in range(on[0], on[-1] + 1):
        if e[i] <= th: run += 1
        else:
            if run * .01 >= .35: gaps.append((round((i - run) * .01, 2), round(i * .01, 2)))
            run = 0
    out[p.split("/")[-1]] = {"dur": round(len(x) / sr, 2), "start": round(s, 2), "end": round(t, 2), "gaps": gaps}
    print(f"{p.split('/')[-1]:<32} dur {len(x)/sr:6.2f}  speech {s:5.2f}-{t:6.2f}  pauses {gaps}")
json.dump(out, open("tools/vospan.json", "w"), indent=1)
