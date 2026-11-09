"""Local 2D animation (free) for S06_SH04: the 6:14 departs ALONG ITS OWN TRACK and leaves the frame on the right.

History: the AI clip (E001_S06_SH04_CLIP_v01) turned the train around (owner QC v01). ANIM_v01 slid the train into the
hillside (owner QC v02) because the AI 'empty track' plate had erased the train's own (back) track. v02 of this script:
  1. measures the two tracks in the keyframe (line search on rail highlights): back track (the train's) and foreground track
  2. restores the erased back track on the plate by borrowing the plate's real foreground track (rails, sleepers, gravel)
     and squeezing it, column by column, into the back track's measured perspective band
  3. moves the train cut-out along the back track's centre line (with a slight perspective scale-up) until it leaves the
     frame on the right. No occlusion line, no tunnel.
Output: clips/E001_S06_SH04_ANIM_v02.mp4 (1920x1080, 30 fps, 5 s)."""
import pathlib, subprocess, numpy as np
from PIL import Image
EP = pathlib.Path(__file__).resolve().parent.parent
ORIG = EP / "images/keyframes/E001_S06_SH04_KF_v01.png"; PLATE = EP / "images/keyframes/E001_S06_SH04_PLATE_KF_v01.png"
OUT = EP / "clips/E001_S06_SH04_ANIM_v02.mp4"; TMP = EP / "renders/tmp/depart2"; TMP.mkdir(parents=True, exist_ok=True)
FPS, DUR = 30, 5.0
# measured rail lines y = y0 + m (x - 1205)   (keyframe, right of the train; see run-log v03)
BACK_FAR, BACK_NEAR = (404, 0.104), (414, 0.120)      # the train's track (erased in the plate)
FG_FAR, FG_NEAR = (438, 0.152), (472, 0.176)          # foreground track (present in the plate)
line = lambda L, x: L[0] + L[1] * (x - 1205)

def gblur(x, s):
    r = int(3 * s); k = np.exp(-np.arange(-r, r + 1) ** 2 / (2 * s * s)); k /= k.sum()
    pad = lambda v: np.pad(v, r, mode="edge")
    y = np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 0, x)
    return np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 1, y)

A = np.asarray(Image.open(ORIG).convert("RGB")).astype(np.float32) / 255
P = np.asarray(Image.open(PLATE).convert("RGB")).astype(np.float32) / 255
H, W, _ = A.shape

# 2. restore the back track on the plate
P2 = P.copy()
X0 = 690
for x in range(X0, W):
    s0, s1 = line(FG_FAR, x) - 7, line(FG_NEAR, x) + 7          # source band: rails + ballast of the foreground track
    d0, d1 = line(BACK_FAR, x) - 4, line(BACK_NEAR, x) + 4      # destination band: the back track
    n = int(np.ceil(d1) - np.floor(d0))
    if n < 3: continue
    ys = np.arange(int(np.floor(d0)), int(np.floor(d0)) + n)
    src_y = s0 + (ys - d0) / (d1 - d0) * (s1 - s0)
    col = np.stack([np.interp(src_y, np.arange(H), P[:, x, c]) for c in range(3)], 1)
    edge = np.minimum((ys - d0) / 3.0, (d1 - ys) / 3.0).clip(0, 1)            # soft top/bottom edges
    ramp = np.clip((x - X0) / 40.0, 0, 1)                                     # fade in from the left end
    a = (edge * ramp)[:, None]
    P2[ys, x] = col * a + P2[ys, x] * (1 - a)
Image.fromarray((P2 * 255 + 0.5).astype(np.uint8)).save(EP / "images/keyframes/E001_S06_SH04_PLATE_KF_v02.png")

# train cut-out (difference against the ORIGINAL plate, train area only)
d = gblur(np.abs(A - P).sum(2), 1.5)
roi = np.zeros((H, W), bool); roi[150:440, 700:1214] = True
m = (d > 0.18) & roi
ys_, xs_ = np.where(m); x0, x1, y0, y1 = xs_.min(), xs_.max(), ys_.min(), ys_.max()
mask = np.zeros((H, W), np.float32)
for y in range(y0, y1 + 1):
    row = np.where(m[y, x0:x1 + 1])[0]
    if len(row) > 3: mask[y, x0 + row.min(): x0 + row.max() + 1] = 1
mask = np.clip(gblur(mask, 1.2) * 1.2, 0, 1)
TRAIN = Image.fromarray((np.dstack([A, mask]) * 255).astype(np.uint8), "RGBA")

# 3. motion along the back track's centre line, pivot at the front wheels on the near rail
slope = (BACK_FAR[1] + BACK_NEAR[1]) / 2
px, py = 1185.0, line(BACK_NEAR, 1185) + 2
D = 900.0                      # the whole train has left the frame by the end of the move
N = int(FPS * DUR)
for i in range(N):
    t = i / FPS
    u = 0.0 if t < 0.8 else min(1.0, ((t - 0.8) / 3.8) ** 1.7)      # standing, pulls away, accelerates; gone at 4.6 s
    dx = D * u; dy = slope * dx; s = 1 + 0.30 * u                   # slight growth: the track comes toward the camera
    # inverse affine: input = (output - pivot - d) / s + pivot
    a, c = 1 / s, px - (px + dx) / s
    e, f = 1 / s, py - (py + dy) / s
    L = np.asarray(TRAIN.transform(TRAIN.size, Image.AFFINE, (a, 0, c, 0, e, f), resample=Image.BILINEAR)).astype(np.float32) / 255
    al = L[..., 3:4]
    frame = P2 * (1 - al) + L[..., :3] * al
    Image.fromarray((np.clip(frame, 0, 1) * 255 + 0.5).astype(np.uint8)).save(TMP / f"f{i:04d}.png")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(TMP / "f%04d.png"), "-vf",
                "crop='min(iw,ih*16/9)':'min(ih,iw*9/16)':'(iw-min(iw,ih*16/9))/2':'(ih-min(ih,iw*9/16))/2',scale=1920:1080:flags=lanczos,setsar=1",
                "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), str(OUT)], check=True)
print("wrote", OUT, "train bbox", (x0, x1, y0, y1), "slope", round(slope, 3))
