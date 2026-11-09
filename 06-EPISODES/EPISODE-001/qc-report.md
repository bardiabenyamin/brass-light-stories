# QC report — EPISODE-001 "The Early Shelf" (Prompt 10)

## v02 (fix pass, 2026-11-09): current

Render: `renders/E001_RENDER_review_v02.mp4` (committed, 86.7 MB) · master `renders/E001_RENDER_master_v02.mp4` (210.7 MB, CRF 16:
not committed (> 95 MB), delivered as a download; rebuildable with `python3 tools/assemble.py`).
**Status: ROUGH CUT v02 FOR OWNER REVIEW (not final).** The owner's 8 defects in v01 are fixed and verified below. It is still a
mostly-stills animatic with 18 animated shots; see "What v02 still is not".

### Owner's v01 defects: verification in v02

| # | v01 time | Defect | Fix | Verified how (v02) | Result |
|---|---|---|---|---|---|
| 1 | 0:20–0:23 | Arrival train drifts off the rails into the building | Only the on-track first 1.4 s of the clip, slowed | 12 frames every 0.25 s, 0:19.0–0:21.9 | PASS: on the rails throughout |
| 2 | 0:43–0:47 | Train standing on the platform | Keyframe edit v02: straight platform edge, rails under the whole train | Frames 0:43.5–0:47.0 | PASS |
| 3 | 1:02–1:07 | Ida has three arms | Keyframe edit v02: two arms | Frames 1:02–1:09 + zoom on the keyframe | PASS |
| 4 | 3:06–3:11 | Departure train U-turns into nothing | Local cutout animation along the train's own wheel line into the tunnel | 12 frames every 0.45 s, 3:05.7–3:10.8 | PASS: the train exits along the track into the tunnel; the umbrella stays still |
| 5 | 3:20–3:23 | Theo's mouth not moving | New talking clip, retimed to our voice line | Face crops every 0.3 s: mouth open during 3:19.85–3:21.25 (the line), closed after | PASS (phrase-level sync, not phoneme-exact) |
| 6 | 3:28–3:36 | Theo's mouth not moving | New 6 s talking clip, 4 speech bursts mapped to the 4 phrases (9 retimed pieces) | Face crops every 0.4 s: mouth moves in each phrase and closes in each pause | PASS (phrase-level) |
| 7 | 4:22–4:29 | Grille wires disappear around the glowing whistle | Composite: whistle + glow placed behind the original, unchanged grille (same fix applied to the umbrella vanish at 3:11) | 12 frames every 0.6 s on the grille | PASS: lattice complete through the crossfade |
| 8 | whole video | Constant static | It was my synthesized room-tone, wind and rain-hiss beds: removed. Drips regenerated without hiss | Edit list has no noise beds; silencedetect (-50 dB) finds only the two intended pauses (4:15.5–4:17.9, 4:45.2–4:48.4) | PASS |

Also restaged in v02: every remaining line that played over the speaker's own still face (Wren and Ida in S03, S04, S08) is now heard
over the listener, the shelf, the ledger, or Ida's key (shot / reverse shot). Verified on frame sheets of S04 and S08.
Added animation: Theo with his watch (0:53–0:59), followed by a clock cutaway.

### Technical spec (v02)

| Check | Result | Status |
|---|---|---|
| Video / audio | H.264 1920×1080 30 fps yuv420p · AAC 48 kHz stereo | PASS |
| Runtime | 4:53.3 (293.31 s; matches the edit list to the frame) | PASS |
| Loudness | -15.6 LUFS integrated, LRA 7.2 LU, peak -1.3 dBFS | PASS |
| Black / freeze | Title card, one scene fade, cut to black + end card (all intended) | PASS |
| Committed size | 86.7 MB (< 95 MB) | PASS |

### What v02 still is not (honest limits)

- **Not fully animated.** 18 shots move, counting reuses (AI clips from v01 and v02, 4 reused from the proof-of-work, and the local
  train animation); the rest are stills with camera moves. Full animation of a 5-minute episode needs roughly 150–250 more
  credits at current prices (1 credit per second of clip, with retries). The balance is 0.72.
- **Lip-sync is phrase-level** on Theo's two shots only. Everyone else's lines are staged off-face by design.
- **Voices still not human-audited** (pronunciation of "Larkspur" and "Nora"; casting of Vera and Archie).
- Stills are 1344 px upscaled to 1080p; a few deep crops are soft (S03 Wren close crop, S07 shelf crop, S02 clock cutaway).
- Commercial-use rights for the Higgsfield outputs are not yet verified by the owner.

---

## v01 (first review cut): superseded


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
