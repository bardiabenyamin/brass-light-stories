"""Local fix (free) for crossfades through the brass grille: build the 'object present' frame on top of the ORIGINAL
empty-shelf image so both crossfade frames share one grille, pixel for pixel.
  base  = empty shelf (A); edit = AI edit with the object added (B; re-rendered, about 1 px off, wires missing near the object)
  1. align B to A (best integer shift), 2. take only the object and its light from B (difference mask, feathered),
  3. redraw A's lattice wires in front of the object, relit by B's local light (ratio of blurred images).
Usage: python3 grille_composite.py BASE EDIT OUT y0 y1 x0 x1   (the box limits the change to the compartment)"""
import sys, numpy as np
from PIL import Image

def gblur(x, s):
    r = int(3 * s); k = np.exp(-np.arange(-r, r + 1) ** 2 / (2 * s * s)); k /= k.sum()
    pad = lambda v: np.pad(v, r, mode="edge")
    y = np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 0, x)
    return np.apply_along_axis(lambda v: np.convolve(pad(v), k, "valid"), 1, y)

def main(base, edit, out, y0, y1, x0, x1):
    A = np.asarray(Image.open(base).convert("RGB")).astype(np.float32) / 255
    B = np.asarray(Image.open(edit).convert("RGB")).astype(np.float32) / 255
    la, lb = A.mean(2), B.mean(2)
    best = min(((np.mean(np.abs(la[50:400] - np.roll(np.roll(lb, dy, 0), dx, 1)[50:400])), dx, dy) for dy in range(-4, 5) for dx in range(-4, 5)))
    _, dx, dy = best; B = np.roll(np.roll(B, dy, 0), dx, 1); lb = B.mean(2)
    box = np.zeros(la.shape, np.float32); box[y0:y1, x0:x1] = 1; box = gblur(box, 4)
    # 2. object + light mask: where the edit differs strongly from the base (smoothed), inside the box
    d = gblur(np.abs(B - A).sum(2), 3)
    m_obj = np.clip((d - 0.10) / 0.15, 0, 1) * box
    m_obj = np.clip(gblur(m_obj, 2) * 1.3, 0, 1)
    res = A * (1 - m_obj[..., None]) + B * m_obj[..., None]
    # 3. A's wires (thin bright structure) redrawn in front, lit by B's local light
    hp = la - gblur(la, 3)
    m_wire = np.clip((hp - 0.025) / 0.05, 0, 1) * box * np.clip(m_obj * 3, 0, 1)
    ratio = np.clip(gblur(B, 8) / np.maximum(gblur(A, 8), 1e-3), 0.6, 3.0)
    A_lit = np.clip(A * ratio, 0, 1)
    res = res * (1 - m_wire[..., None]) + A_lit * m_wire[..., None]
    Image.fromarray((np.clip(res, 0, 1) * 255 + 0.5).astype(np.uint8)).save(out)
    print(f"{out}: shift dx={dx} dy={dy}; object px {int((m_obj > 0.5).sum())}; wire px redrawn {int((m_wire > 0.5).sum())}")

if __name__ == "__main__":
    a = sys.argv; main(a[1], a[2], a[3], *map(int, a[4:8]))
