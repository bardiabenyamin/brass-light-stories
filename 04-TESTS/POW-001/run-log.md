# POW-001 run log

Every submission, its job ID, cost, output file, and inspection result. Updated as the run progresses (it survives
session restarts). Prices were measured by preflight, and the balance is checked after each phase.

## Balance checkpoints

| When | Balance (credits) | Spent since start |
|---|---|---|
| Start (before any submission) | 142.4 | 0 |
| After Phase A (5 images; one 429 rejection, not charged) | 134.9 | **7.5** (= 5 × 1.5, matching the quote) |
| After Phase B (7 images: 3 retries/edits + 4 keyframes; one 429, not charged) | 124.4 | **18.0** (+10.5 = 7 × 1.5) |
| **Final** (after 5 clips + 4 lines; three more 429s, not charged) | **97.8** | **44.6** (+25 clips, +1.6 audio) |

## Jobs

| # | Item | Model / settings | Job ID | Result | Credits | Output file | Inspection |
|---|---|---|---|---|---|---|---|
| A0 | REF_WREN v01 (CR-01), 1st try | gpt_image_2_6 · high · 1k · 4:5 | — | **429 rate limit, no job created** | 0 | — | — |
| A1 | REF_IDA v01 (CR-06) | same | `517f057c-13ba-4c8a-9e4d-6935d143123a` | completed | 1.5 | `06-EPISODES/EPISODE-001/references/characters/E001_CHR_ida_front_v01.png` | Identity locks 1–7 **pass**. **Style fail:** near-realistic skin and proportions; clashes with Wren. Key bow came out as a round 5-petal flower, not the larkspur spike in `props.md` |
| A2 | SH01 = LR-06 platform MIDNIGHT | same · 16:9 | `9af21ca8-ada6-4cb5-aa85-dfd96f658e71` | completed | 1.5 | `06-EPISODES/EPISODE-001/references/locations/E001_LOC_platform_midnight_wide_v01.png` | **Pass** as the location reference (tunnel left, clock above the dark office window, empty hook, bench and lamp right, moon upper right, no people, no text). **The clock reads about 10:08**, so it needs a hands-to-midnight edit for the PoW |
| A3 | SH02 clock insert | same · 16:9 | `b4b50218-8680-49cc-ae6e-196bfdb5c3d1` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH02_KF_v01.png` | **Pass**: celadon face, 12 batons (thicker at 12/3/6/9), no numerals, hour hand at 12, minute hand one step before. Note: a small lit window in the lower corner |
| A4 | SH03 empty Early Shelf v01 | same · 16:9 | `37811720-ac49-4860-b620-0cd45720970e` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH03_KF_v01.png` | **Fail (my prompt's fault):** a window on the east wall (canon: south, behind the camera) and a lit cream desk lamp (canon: the office is dark at midnight). Shelf design itself passes |
| A5 | REF_WREN v01 (CR-01), resubmitted | gpt_image_2_6 · high · 1k · 4:5 | `21ea2f37-44ef-47ea-82f8-616daf026597` | completed | 1.5 | `06-EPISODES/EPISODE-001/references/characters/E001_CHR_wren_front_v01.png` | **Pass, all locks:** bob with bangs, grey-green eyes (zoom-checked), freckles, skin, burnt-orange corduroy jacket, striped tee, navy cargo trousers, whistle with **exactly 3 holes** on a long chain, five-finger hands. Style matches the lock (sculpted, slightly enlarged eyes) |
| B10 | REF_IDA v02 (retry 1): re-render from v01, Wren v01 as the style reference | same · 4:5 · refs: A1 + A5 | `54574eff-0450-4488-9b09-d32079670dce` | completed | 1.5 | `06-EPISODES/EPISODE-001/references/characters/E001_CHR_ida_front_v02.png` | **Pass, all locks, and the style now matches Wren** (sculpted, enlarged eyes, smoother skin). No identity bleed from Wren. **This is now Ida's identity reference** |
| B11 | SH01 edit: clock hands to midnight | same · 16:9 · ref: A2 | `78ae169f-f9f4-42a5-b810-d7c41661a53f` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH01_KF_v01.png` | **Pass:** both hands at 12; everything else unchanged |
| B12 | SH03 v02 (retry 1): dark room, moonlight from behind the camera | same · 16:9 | `f03ea6b7-3309-4102-a4f3-d1ca402c404d` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH03_KF_v02.png` | **Pass:** window-bar shadows from behind the camera, no lamps or visible windows, empty grille compartment. Note: the shelves read blue-painted under moonlight; the DAY office reference must say honey wood |
| B13 | SH05 Wren peeks (W2), Wren v01 ref | same · 16:9 · ref: A5 | `2f2aed20-d275-4d95-8bdf-86fe4dafcd28` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH05_KF_v01.png` | **Identity pass** (all locks, five-finger hand). **Lighting deviation:** "amber glow from off-screen" became a visible lit lamp at the right edge. Fixed by a right-strip crop in the edit |
| B14 | SH06 Wren close-up (W2), resubmitted | same · 16:9 · ref: A5 | `4bc8dda6-b7be-4c3f-b7f1-60b948b9e456` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH06_KF_v01.png` | **Pass:** identity, a correct hand grip on the 3-hole whistle, awe. Eyes read hazel-green under amber. A lit lantern at the right edge (crop) |
| B15 | SH04 edit: the umbrella arrives (from B12) | same · 16:9 · ref: B12 | `cc5480ba-7493-4206-9205-216dabcefbc9` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH04_KF_v01.png` (+ `_retouch.png`) | **Pass:** the rest of the frame is pixel-faithful to SH03 v02 (a clean crossfade); mustard canopy, J-handle, **brass sparrow charm**, amber glow. **Defects:** about 15 px of maker's-mark lettering on the canopy (blurred locally in `_retouch`); the mended tear is not legible at this scale (the PR-01 prop reference must carry it) |
| B16 | SH07 Ida in the doorway (I2), Ida v02 ref | same · 16:9 · ref: B10 | `f25f3ad3-9f40-4010-879c-ffbd9680be15` | completed | 1.5 | `04-TESTS/POW-001/keyframes/POW001_SH07_KF_v01.png` | **Identity pass:** braid over her right shoulder, dressing gown, nightdress, slippers, key on cord, hand at her chest. **Deviations:** a lit desk lamp and a small red toy boat at the right edge (crop) |
| C22 | Clip C02, clock insert | grok_video_v15_lite · 5 s · 720p · start: A3 | `e1f0d2fc-26ca-400e-842e-527ff13baa79` | completed | 5 | `clips/POW001_SH02_CLIP_v01.mp4` (1280×704, 24 fps, with model audio) | **Partial:** the minute hand reaches 12 at about 1.5 s, then **keeps sweeping** to about 12:05. The face is stable. Edit: cut at 1.5 s and hold that frame |
| C23 | Clip C05, Wren peeks | same · start: B13 | `b9d81c18-ab6e-4965-94b8-a3701b942bed` | completed | 5 | `clips/POW001_SH05_CLIP_v01.mp4` | **Pass:** she leans in and her eyes widen; identity stable in every sampled frame; no morphing |
| C21 | Clip C01, platform push-in (1st try 429, not charged) | same · start: B11 | `f3844ad2-4f96-4bb0-b756-914f046661af` | completed | 5 | `clips/POW001_SH01_CLIP_v01.mp4` | **Fail for its purpose:** the push-in and building are stable, but **the clock hands move from 12:00 to about 12:08** despite "hands stay still". Edit uses a free digital push on the B11 still instead |
| C24 | Clip C06, Wren close-up and whistle | same · start: B14 | `ad39cc06-ebe6-4467-bcf1-1c7fa2d7f120` | completed | 5 | `clips/POW001_SH06_CLIP_v01.mp4` | **Pass:** identity stable; the hand on the whistle stays well formed. The expression drifts from awe to resolve (acceptable) |
| C25 | Clip C07, Ida in the doorway | same · start: B16 | `edd11c6c-4785-4500-a22a-61609ac41897` | completed | 5 | `clips/POW001_SH07_CLIP_v01.mp4` | **Pass:** identity stable; a small hand movement at the key; a slight camera drift (harmless) |
| D31 | VO1, voice "Annie" (preset) | seed_audio | `fe8d4daf-48d5-40e5-824c-cf1f22399828` | completed | 0.4 | `audio/POW001_VO_wren_L001_annie_v01.wav` (6.5 s, peak −1.9 dB) | Pass. 222 Hz; slow and dramatic, with about 1 s pauses. **Used in the render** |
| D33 | VO1, voice "Evie" (casting A/B) | seed_audio | `4eaecafe-42e5-4bc7-9abd-a55e0a5576c3` | completed | 0.4 | `audio/POW001_VO_wren_L001_evie_v01.wav` (4.0 s, peak −7.4 dB) | Pass. 195 Hz; natural pace |
| D32 | VO2, Annie (1st try 429, not charged) | seed_audio | `56325f8b-4046-494a-8474-60bbf4427938` | completed | 0.4 | `audio/POW001_VO_wren_L002_annie_v01.wav` (5.7 s, peak −1.6 dB) | Pass. **Used in the render** |
| D34 | VO2, Evie (1st try 429, not charged) | seed_audio | `662b5007-c899-4aa9-adff-75a7e1316dee` | completed | 0.4 | `audio/POW001_VO_wren_L002_evie_v01.wav` (6.5 s, peak −6.9 dB) | Pass |
| E | Assembly (local ffmpeg, `render.sh`) | — | — | completed | 0 | `render/POW001_RENDER_review_v01.mp4` | **Verified:** 1920×1080, 30 fps, H.264 yuv420p, AAC 48 kHz stereo, 30.0 s, −16.4 LUFS. Frame check of all segments passed (clock 11:59 → 12:00 hold; wide at 12:00; umbrella crossfade; lamps cropped out). Narration at 0.8 s and 13.8 s as scripted |

Voice shortlist method: the female preset previews (14) were analyzed for median pitch. Teen-girl range is about
220–250 Hz; the brief is "mid-low for her age, dry". **Annie** (235 Hz, narrow range: calm, dry) and **Evie** (219 Hz)
were chosen. Pitch only shortlists; the owner should audition before final casting.

## Lessons so far

1. **Shot prompts must state the camera direction against the room geography.** "Moonlight from the right" invented a
   window that contradicts `locations.md`. Fix: say where the light source is relative to the camera ("from a window
   behind the camera").
2. **The model keeps characters at different stylization levels** unless a style reference is given. An older face
   drifts toward realism. Fix being tested: render secondary characters with the approved Wren reference as a
   style-only reference.
3. **Wide shots ignore small time details** (the clock read 10:08 at "midnight"). Fix: a cheap targeted edit, or
   describe the hands explicitly in every clock shot.
4. **Rate limit:** about 4 concurrent image jobs, 2 video, and 2 audio. Submit in small batches. Rejected submissions are not charged.
5. **"Light from off-screen" makes the model draw the light source** (a lamp or lantern) in 3 of 3 character shots.
   Fix for production prompts: "all lamps unlit; the warm light comes from an unseen source below frame right".
6. **AI video animates clock hands even when told not to** (2 of 2 clock shots). Rule: keep clock faces out of AI
   clips. Use stills with digital camera moves, or cut each clip at the frame where the hands are correct.
7. **Character identity holds very well in motion** with grok_video_v15_lite at 5 s (3 of 3 character clips, no
   morphing or face drift). Hands held up, both in a static grip and while moving.
8. **Image edits are pixel-faithful** (the umbrella edit and the clock-hands edit), which makes appear and disappear
   crossfades cheap and reliable.

## Close-out

- Totals: 12 images, 5 clips, 4 lines = **44.6 credits** (ceiling about 70). The optional higher-tier comparison clip (22.5) was **not run**: Lite held identity, and the remaining issues come from prompting.
- The 6 unblocked generation tools were **re-blocked** right after the run (`.claude/settings.json` restored to 35 deny entries).
- Report: `report.md`.
