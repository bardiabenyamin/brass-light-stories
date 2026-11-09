"""Local 2D animation (free) for S06_SH04: the 6:14 departs along its rails into the tunnel.
The AI clip (E001_S06_SH04_CLIP_v01) turned the train around after 1.5 s (owner QC, v01). Here the train is cut out
of the approved keyframe (difference against an AI edit with the train removed) and slid along the line of its own
wheels into the tunnel mouth, where the portal hides it. Output: clips/E001_S06_SH04_ANIM_v01.mp4 (1920x1080, 30 fps, 5 s)."""
import pathlib, subprocess, numpy as np
from PIL import Image
EP = pathlib.Path(__file__).resolve().parent.parent
ORIG = EP / "images/keyframes/E001_S06_SH04_KF_v01.png"; PLATE = EP / "images/keyframes/E001_S06_SH04_PLATE_KF_v01.png"
OUT = EP / "clips/E001_S06_SH04_ANIM_v01.mp4"; TMP = EP / "renders/tmp/depart"; TMP.mkdir(parents=True, exist_ok=True)
FPS, DUR = 30, 5.0

def gblur(x, s):
    r = int(3 * s); k = np.exp(-np.arange(-r, r + 1) ** 2 / (2 * s * s)); k /= k.sum()
    pad = lambda v: np.pad(v, r, mode="edge")
    y = np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 0, x)
    return np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 1, y)

A = np.asarray(Image.open(ORIG).convert("RGB")).astype(np.float32) / 255
P = np.asarray(Image.open(PLATE).convert("RGB")).astype(np.float32) / 255
H, W, _ = A.shape
# align the plate to the original on the unchanged left half
best = min(((np.mean(np.abs(A[:, :W // 2] - np.roll(np.roll(P, dy, 0), dx, 1)[:, :W // 2])), dx, dy) for dy in range(-4, 5) for dx in range(-4, 5)))
P = np.roll(np.roll(P, best[2], 0), best[1], 1)
# train mask: strong difference in the right part of the frame above the bench
d = gblur(np.abs(A - P).sum(2), 1.5)
roi = np.zeros((H, W), bool); roi[150:440, 700:1214] = True   # the train only: excludes the re-rendered tunnel arch (x > 1214)
m = (d > 0.18) & roi
ys, xs = np.where(m)
x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
# fill holes inside the bbox rows (train windows are similar in both images only rarely), then feather
mask = np.zeros((H, W), np.float32)
for y in range(y0, y1 + 1):
    row = np.where(m[y, x0:x1 + 1])[0]
    if len(row) > 3: mask[y, x0 + row.min(): x0 + row.max() + 1] = 1
mask = np.clip(gblur(mask, 1.2) * 1.2, 0, 1)
# track direction from the wheel line: lowest mask pixel per column
cols = [(x, np.where(mask[:, x] > 0.5)[0].max()) for x in range(x0 + 5, x1 - 5) if (mask[:, x] > 0.5).any()]
cx, cy = np.array(cols).T
slope = np.polyfit(cx, cy, 1)[0]
front = x1  # the train's front faces the tunnel (right)
print(f"plate shift {best[1:]}, train bbox x {x0}-{x1} y {y0}-{y1}, wheel-line slope {slope:.3f}")

TRAIN = np.dstack([A, mask])
def shift_layer(layer, dx, dy):
    img = Image.fromarray((np.clip(layer, 0, 1) * 255).astype(np.uint8), "RGBA")
    img = img.transform(img.size, Image.AFFINE, (1, 0, -dx, 0, 1, -dy), resample=Image.BILINEAR)
    return np.asarray(img).astype(np.float32) / 255

D = (x1 - x0) + 90                      # travel: the whole train passes the portal line, with margin
x_cut = front + 4                       # the tunnel portal line (the train's front edge at t = 0)
N = int(FPS * DUR)
xx = np.arange(W)[None, :].astype(np.float32)
for i in range(N):
    t = i / FPS
    u = 0.0 if t < 0.8 else min(1.0, ((t - 0.8) / (DUR - 1.2)) ** 1.7)   # holds, pulls away, accelerates, gone by 4.6 s
    dx = D * u; dy = slope * dx
    L = shift_layer(TRAIN, dx, dy)
    hide = np.clip((xx - x_cut) / 10.0, 0, 1)                    # behind the portal
    shade = 1 - 0.45 * np.clip((xx - (x_cut - 60)) / 60.0, 0, 1)  # darkens as it enters the tunnel shadow
    a = L[..., 3] * (1 - hide)
    rgb = L[..., :3] * shade[..., None]
    frame = P * (1 - a[..., None]) + rgb * a[..., None]
    Image.fromarray((np.clip(frame, 0, 1) * 255 + 0.5).astype(np.uint8)).save(TMP / f"f{i:04d}.png")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(TMP / "f%04d.png"), "-vf",
                "crop='min(iw,ih*16/9)':'min(ih,iw*9/16)':'(iw-min(iw,ih*16/9))/2':'(ih-min(ih,iw*9/16))/2',scale=1920:1080:flags=lanczos,setsar=1",
                "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS), str(OUT)], check=True)
print("wrote", OUT)
