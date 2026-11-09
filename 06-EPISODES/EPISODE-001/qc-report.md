# QC report — EPISODE-001 "The Early Shelf" (Prompt 10)

Render under review: `renders/E001_RENDER_review_v01.mp4` (committed, 86.8 MB) · master `renders/E001_RENDER_master_v01.mp4`
(211 MB, CRF 16: **not committed** (over the 95 MB limit), delivered as a download; rebuildable with `python3 tools/assemble.py`).
Checked 2026-11-09 with `tools/qc.py` (ffprobe, EBU R128, blackdetect, freezedetect, silencedetect, one frame per shot on contact sheets) plus targeted frame pulls.

**Verdict: PASS FOR OWNER REVIEW.** Not final: it needs the owner's listen-through (voices) and approval before any upload.

## Technical spec

| Check | Target | Result | Status |
|---|---|---|---|
| Container / video | MP4, H.264, 1920×1080, 30 fps | h264 1920×1080 30/1 yuv420p | PASS |
| Audio | 48 kHz | AAC 48 kHz stereo (160 kb/s review, 192 kb/s master) | PASS |
| Runtime | About 5 min (story sets length) | **4:53.4** (293.38 s); picture = edit list to the frame (fixed: see below) | PASS |
| Loudness | About -16 LUFS for review (YouTube normalizes to -14) | **-15.7 LUFS** integrated, LRA 7.0 LU, peak -1.4 dBFS | PASS |
| File size (committed copy) | < 95 MB | 86.8 MB | PASS |
| Black frames | Only intended | 0:15.0–0:19.0 title card (dark card) · 2:45.6–2:46.3 scene fade · 4:45.4–4:53.3 cut to black + end card | PASS (all intended) |
| Freezes | Only intended | 4:48.1 for 4.4 s = static end card | PASS |
| Silence | Only intended | 4:45.4–4:48.4: two seconds of silence after the final line (deliberate) | PASS |
| Dialogue overlap | None | 34 VO events checked: no overlaps, none run past their scene | PASS |

## Continuity / visual (62 shots on 4 contact sheets)

| Check | Result |
|---|---|
| Character identity locks (Wren W1/W2, Ida I1/I2, Theo T1, Abe, Ledger) | PASS on every shot. Hands checked on the inserts (key, umbrella, two whistles): five fingers |
| Screen direction | Station-front master: tunnel image left, the 6:14 arrives left→right. Reverse master (bench): tunnel image right, departure moves right. Two-shots: Wren left, adult right. PASS |
| Lighting states | GOLD (Mon, Tue-wet), LAMP (office, kitchen), MIDNIGHT (lamps unlit; amber only from the shelf). PASS |
| Reserved colors | Mustard only on the umbrella; red only on Ida's cord, the ledger threads, Abe's lantern. PASS (a small reddish box in S09_SH03 background, minor) |
| Text artifacts | None legible (the tear stitching is a zigzag, not lettering). PASS |
| Clock faces | Midnight shots read 12:00; the 6:14 shots are approximate (flag F5) |
| Rules shown | R1 (midnight arrival, ×2), R2 (copy vanishes at the moment of loss). No R3–R10. PASS |
| Clues | K1 1:18 · K6 1:32 and 3:51 · K3 1:44 · K5 2:11 · K2 + K4 3:29–3:36 · Abe and Ledger 0:47. PASS |
| Cliffhanger | Readable without explanation (two whistles + final line). Ida absent from the final beat. PASS |

## Defects found and fixed during QC (before delivery)

1. **Audio/picture drift (about 1 s by the end):** motion interpolation dropped 2–5 frames at the end of each of the 10 slowed clips.
   Fixed: segments padded to exact frame counts, and the assembler now pads automatically. Verified: render length = edit list.
2. **Prop scale (flag F3):** a 4.5 s hold on the whistle close-up in S05 read as a long recorder, contradicting the 5 cm whistle
   in S09. Fixed: the clip now stops at 2.6 s and the song plays over the midnight clock face (the POW-001 keyframe),
   which flows straight into the clock-strikes-twelve insert. Verified on extracted frames 2:06–2:23.

The review render was rebuilt in place after these fixes; the pre-fix build was never delivered or committed.

## Known limitations (accepted for v01; owner to judge)

| # | Item | Severity | Fix path |
|---|---|---|---|
| L1 | **Voices not heard by a human.** Pronunciation ("Larkspur", "Nora"), the pacing of Ida's slow lines, and Vera/Archie casting are unverified | High (until auditioned) | Owner listens; any line can be regenerated alone (about 0.1–1.5 credits each) |
| L2 | It's an illustrated-motion style: 9 animated clips + 4 reused, the rest stills with camera moves. No lip-sync by design | Medium | More clips need more credits (1 per second) |
| L3 | Stills are 1344 px wide, upscaled to 1080p; pushes up to 1.4× are a little soft (S03 Wren close crop, S07 shelf crop) | Low | Higher-resolution regeneration (1.0 credit each at 2k) |
| L4 | Music beds (2 × 60 s) repeat in places; not listened to | Low–medium | Owner listen; a third cue costs about 3.8 credits |
| L5 | Synthesized SFX (bell, shimmer, drips, room tone) are simple | Low | Replace with library or mirelo SFX (0.25 credits per second) |
| L6 | Continuity flags F1–F7 in `continuity.md` (shelf wall facing the door, K5 location, whistle shape on the shelf, 6:14 clock hands) | Low | Owner approves or requests changes |
| L7 | Rights: commercial use of Higgsfield outputs (images, video, seed_audio voices, ElevenLabs music, mirelo SFX) on the starter plan is **NOT VERIFIED** | Blocks monetized upload | Owner checks the plan terms before publishing |

**Asset generation status:** the Episode 1 spend is used (83.58 credits; 14.22 left). Paid tools are blocked again (35 deny entries).
