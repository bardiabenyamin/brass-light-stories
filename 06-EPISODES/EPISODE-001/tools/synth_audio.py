"""Free, locally synthesized audio for EPISODE-001 (numpy only): Mom's song on the tin whistle (clue K5),
the midnight clock strike, the arrival shimmer, rain drips, and room tones. All original. 48 kHz."""
import numpy as np, wave, pathlib, sys
SR = 48000
OUT = pathlib.Path(__file__).resolve().parent.parent / "audio"
rng = np.random.default_rng(7)

def save(path, x, stereo=True):
    x = np.clip(x, -1, 1)
    if stereo and x.ndim == 1: x = np.stack([x, x], 1)
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2 if stereo else 1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())
    print(path, f"{len(x)/SR:.2f}s")

def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.zeros_like(x); acc = 0.0
    for i in range(len(x)): acc = (1 - a) * x[i] + a * acc; y[i] = acc
    return y

def reverb(x, wet=0.25, taps=((0.031, .5), (0.047, .4), (0.071, .32), (0.113, .25), (0.163, .18), (0.241, .12))):
    y = x.copy()
    for d, g in taps:
        n = int(d * SR); y[n:] += wet * g * x[:-n]
    return y

NOTE = {"A4": 440.0, "B4": 493.88, "C#5": 554.37, "D5": 587.33, "E5": 659.25, "F#5": 739.99, "G5": 783.99, "A5": 880.0, "B5": 987.77}
# Mom's song (original): 4 bars of 3/4 at 84 BPM, ends open on the third (F#) so later episodes can resolve it.
SONG = [("F#5", 1), ("A5", .5), ("G5", .5), ("F#5", 1),  ("E5", 1.5), ("D5", .5), ("E5", 1),
        ("F#5", 1), ("B5", 1), ("A5", 1),  ("F#5", 2.6)]
def whistle(song=SONG, bpm=84, level=.32):
    beat = 60 / bpm; out = []
    for i, (n, b) in enumerate(song):
        d = b * beat; t = np.arange(int(d * SR)) / SR; f = NOTE[n]
        vib = 1 + .004 * np.sin(2 * np.pi * 5.6 * t) * np.clip((t - .18) / .25, 0, 1)
        ph = 2 * np.pi * np.cumsum(f * vib) / SR
        tone = np.sin(ph) + .08 * np.sin(2 * ph) + .03 * np.sin(3 * ph)
        breath = lowpass(rng.standard_normal(len(t)), 2500) * .05
        env = np.minimum(1, t / .035) * np.minimum(1, (d - t) / .07) ** .7
        out.append((tone + breath) * env * level)
    x = np.concatenate(out); x = np.concatenate([np.zeros(int(.3 * SR)), x, np.zeros(int(1.5 * SR))])
    return reverb(x, .35)

def bell(f0=196.0, dur=5.0, level=.5):
    t = np.arange(int(dur * SR)) / SR
    parts = [(.5, .5, .9), (1.0, 1.0, 1.6), (1.19, .45, 1.9), (1.5, .35, 2.3), (2.0, .3, 2.8), (2.74, .2, 3.5), (3.0, .15, 4.0), (4.07, .1, 5.0)]
    x = sum(a * np.sin(2 * np.pi * f0 * r * t + rng.random() * 6) * np.exp(-k * t) for r, a, k in parts)
    x *= np.minimum(1, t / .004)
    return reverb(x / 3 * level, .3)

def shimmer(dur=4.0, level=.18):
    t = np.arange(int(dur * SR)) / SR; env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    pad = sum(a * np.sin(2 * np.pi * f * t) for f, a in [(220, 1), (329.63, .7), (440, .5), (554.37, .3)])
    hi = sum(.12 * np.sin(2 * np.pi * f * t + rng.random() * 6) * (.5 + .5 * np.sin(2 * np.pi * rng.uniform(.3, .9) * t + rng.random() * 6))
             for f in rng.uniform(1800, 4200, 14))
    return reverb((pad / 2.5 + hi / 3) * env * level, .3)

def tick(level=.5):
    t = np.arange(int(.09 * SR)) / SR
    return level * np.sin(2 * np.pi * 1900 * t) * np.exp(-70 * t)

def drips(dur=30.0, rate=1.6, level=.25, rain=.05):
    x = np.zeros(int(dur * SR)); n = int(dur * rate)
    for s in rng.uniform(0, dur - .2, n):
        t = np.arange(int(.06 * SR)) / SR; f = rng.uniform(900, 1700)
        d = np.sin(2 * np.pi * f * t * (1 + 2.5 * t)) * np.exp(-60 * t) * rng.uniform(.3, 1)
        i = int(s * SR); x[i:i + len(d)] += d
    noise = lowpass(rng.standard_normal(len(x)), 1800) * rain if rain else 0
    return reverb(x * level + noise, .2)

def tone(dur, fc=400, level=.04):
    return lowpass(rng.standard_normal(int(dur * SR)), fc) * level * 8

if __name__ == "__main__":
    save(OUT / "music/E001_MUS_momsong_v01.wav", whistle())
    save(OUT / "sfx/E001_SFX_bell_v01.wav", bell())
    save(OUT / "sfx/E001_SFX_shimmer_v01.wav", shimmer())
    save(OUT / "sfx/E001_SFX_tick_v01.wav", tick())
    if not (OUT / "sfx/E001_SFX_drips_v01.wav").exists(): save(OUT / "sfx/E001_SFX_drips_v01.wav", drips())
    # v02 (owner QC, v01 review): no hiss bed. The constant noise read as static
    save(OUT / "sfx/E001_SFX_drips_v02.wav", drips(rain=0, level=.3))
    save(OUT / "sfx/E001_SFX_roomtone_v01.wav", tone(60, 300, .03))
    save(OUT / "sfx/E001_SFX_wind_v01.wav", tone(60, 700, .025) * (0.7 + 0.3 * np.sin(2 * np.pi * 0.07 * np.arange(60 * SR) / SR)))
