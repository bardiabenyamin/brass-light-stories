"""Dense QC strips: frames every STEP seconds over a time range of a render, tiled into one sheet.
Usage: python3 qc_strips.py RENDER OUTDIR NAME T0 T1 STEP COLS [CROP]   (CROP = ffmpeg crop expr, e.g. 1300:520:300:560)"""
import subprocess, sys, pathlib, numpy as np
render, outdir, name = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
t0, t1, step, cols = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7])
crop = (f"crop={sys.argv[8]}," if len(sys.argv) > 8 else "")
outdir.mkdir(parents=True, exist_ok=True)
frames = []
for i, t in enumerate(np.arange(t0, t1, step)):
    f = outdir / f"{name}_{i:03d}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", render, "-frames:v", "1", "-vf", f"{crop}scale=384:-2", str(f)], check=True)
    frames.append(f)
rows = (len(frames) + cols - 1) // cols
subprocess.run(["ffmpeg", "-v", "error", "-y", "-start_number", "0", "-i", str(outdir / f"{name}_%03d.png"), "-frames:v", "1",
                "-vf", f"tile={cols}x{rows}", str(outdir / f"sheet_{name}.png")], check=True)
print(outdir / f"sheet_{name}.png", len(frames), "frames")
