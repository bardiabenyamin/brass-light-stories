# POW-001 — "Midnight at the Early Shelf" (proof-of-work plan)

Status: **APPROVED TO RUN** (owner, 2026-11-09: "Proof-of-work cap: use as needed credits, approved to spend after
Prompt 03"; "start it within the approved budget"). Prompt 03 completed and locked the same day.
Working ceiling: **about 70 credits**. Pause and report rather than exceed it. At most 2 retries per item.

## Purpose

1. **Character consistency:** do Wren and Ida stay on-model across a reference and two or three shots?
2. **Locked style:** does the v1 master style hold across exteriors, interiors, close-ups, and inserts?
3. **Animation quality:** morphing, face drift, hands, and the risky clock-hand insert.
4. **Voice quality** for the narrator (stock preset voice; commercial rights to be verified before publishing).
5. **Real cost** per image, clip, and line, and the retry rate. This feeds the per-episode budget.

The result doubles as the Ep1 cold open and a channel teaser, so the spend is not wasted.

## Shot list (about 32 s)

| # | Shot | Location / light | Source | Motion | Edit length |
|---|---|---|---|---|---|
| SH01 | Wide: the station front at midnight; the clock face glows like a pale moon | Platform · MIDNIGHT | **LR-06** (doubles as the location reference) | Clip C01: slow push-in | 5.0 s |
| SH02 | Insert: the minute hand meets twelve | Platform · MIDNIGHT | New keyframe | Clip C02: one hand step (risky shot) | 3.0 s |
| SH03 | Medium: the back wall, the **empty** Early Shelf behind its grille | Office · MIDNIGHT | New keyframe | Still with a slow push (free, in the edit) | 3.0 s |
| SH04 | Same framing: the yellow umbrella **glows into being** | Office · MIDNIGHT | Edit of SH03 (+ umbrella prop) | Crossfade SH03 → SH04 plus bloom (free) | 4.5 s |
| SH05 | Medium: Wren (W2) peeks around the hall door frame, lit amber from low right | Office (shelf master) · MIDNIGHT | Keyframe + **Wren ref** | Clip C05: she leans in, eyes widen | 5.0 s |
| SH06 | Close-up: Wren's awe; her hand finds the whistle | Office · MIDNIGHT | Keyframe + **Wren ref** | Clip C06: her hand tightens on the whistle (hands test) | 4.0 s |
| SH07 | Medium-wide: Ida (I2) in the doorway, watching; her hand closes on the key | Office (shelf master) · MIDNIGHT | Keyframe + **Ida ref** | Clip C07: hand closes on the key | 5.0 s |
| — | Black tail with a final tick | — | — | — | 1.5 s |

**Narration** (Wren, a stock preset voice; final wording comes in Prompt 04):
- VO1, over SH01–SH02: *"In Larkspur, things get lost the day before they go missing."*
- VO2, over SH05: *"Grandma had exactly one rule. The bottom shelf was hers."*

**Sound:** placeholder clock tick and midnight chime synthesized locally with ffmpeg (free). No generated music in
the test.

## Models and measured prices (preflight `get_cost`, 2026-11-09)

| Use | Model | Setting | Credits each |
|---|---|---|---|
| Character references + keyframes | `gpt_image_2_6` (default; accepts reference images) | quality high, 1k | **1.5** |
| Clips | `grok_video_v15_lite` (start-frame image-to-video) | 5 s, 720p (upscaled to 1080p in the edit) | **5** |
| Narration | `seed_audio` (stock preset voice) | one line | **0.4** |
| *(compared, not used)* | `grok_video_v15` / `seedance_2_5` / `flux_3_image` | 5 s 720p / 5 s 720p no audio / 1k | 22.5 / 35 / 2 |

GPT Image has no negative-prompt field, so each prompt ends with a condensed **"Avoid:"** clause drawn from the
locked master negative plus that character's or location's negative.

## Estimate

| Item | Count | Credits |
|---|---|---|
| Images: 2 character refs + 7 keyframes | 9 × 1.5 | 13.5 |
| Clips | 5 × 5 | 25.0 |
| Narration | 2 × 0.4 | 0.8 |
| **Base total** | | **39.3** |
| Retry allowance (about 4 images, 2 clips, 2 lines) | | about 16.8 |
| **Planned worst case** | | **about 56** (under the 70 ceiling) |
| Optional A/B: one SH05 clip on `grok_video_v15`, to compare quality against the Lite tier | 1 × 22.5 | Only if the running total + 22.5 ≤ 70 |

## Phases and stop rules

| Phase | Work | Gate before the next phase |
|---|---|---|
| A | Wren ref, Ida ref, SH01, SH02, SH03 (one batch) | Inspect each against `continuity.md` §A, §A2, §A3. Retry failures (≤ 2). **If Wren or Ida fails twice, stop and report: that is a test result** |
| B | SH04 (edit of SH03), SH05 and SH06 (with the Wren ref), SH07 (with the Ida ref) | Same inspection; identity must match the refs |
| C | Clips C01, C02, C05, C06, C07 | Inspect sampled frames for morphing, drift, and hands |
| D | VO1, VO2 | Listen check (duration, clipping); rights noted as unverified |
| E | Local assembly with ffmpeg: 1920×1080, 30 fps, H.264, 48 kHz | Verify with ffprobe; frame-check |

The running cost is checked with the read-only `balance` after every phase and logged in `COST-LOG.md`.

**Files:**
- The character refs and SH01 go to their canon locations under `06-EPISODES/EPISODE-001/references/`, as
  candidates. They become canon only after owner approval.
- Test-only files go under `04-TESTS/POW-001/`.
- Prompts are composed by `compose_pow.py` from the locked blocks into `pow_prompts.json`.
