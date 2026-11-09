# POW-001 Report — "Midnight at the Early Shelf"

Status: **DONE (2026-11-09).** The render is verified. Every asset is logged in `run-log.md`.
**Render:** `render/POW001_RENDER_review_v01.mp4`
- **Video:** 1920×1080, 30 fps, H.264 yuv420p.
- **Audio:** AAC 48 kHz stereo, −16.4 LUFS integrated.
- **Length:** 30.0 s.

Verified with ffprobe and ebur128, plus frame sampling across all 8 segments.

## 1. Result against each purpose

| Purpose | Result | Evidence |
|---|---|---|
| **Character consistency** | ✅ **Pass.** Wren held identity across her reference, two keyframes, and two clips; Ida across her v02 reference, one keyframe, and one clip. No face drift or morphing in any of the 3 character clips | Run log B13–B16, C23–C25 |
| **Locked style v1** | ✅ **Pass with one fix.** Exteriors, interiors, inserts, and Wren matched first time. **Ida's first render drifted realistic.** Re-rendering her from her own image with Wren's approved image as a style-only reference fixed it with no identity bleed | A1 vs B10 |
| **Animation quality (Lite tier)** | ✅ for characters (subtle performance, five-finger hands held in motion). ❌ **for clocks:** both clips that showed the clock moved its hands against instructions | C22, C21 |
| **Voice** | ✅ Usable. Two stock voices shortlisted by pitch. Annie: 222 Hz, slow and dramatic, used in the edit. Evie: 195 Hz, natural pace, provided for comparison. **Commercial rights not yet verified** | D31–D34 |
| **Real cost** | ✅ **Exactly as quoted:** 44.6 credits total, at 1.5 per image, 5 per 5-s clip, and 0.4 per line. Rate-limit rejections (5 of them) cost nothing | Balance 142.4 → 97.8 |

## 2. What the test taught (production rules from now on)

1. **Light sources:** say "all lamps unlit; the warm light comes from an unseen source below frame right." In 3 of 3
   character shots, "light from off-screen" made the model draw a lamp.
2. **Room geography:** state the light's direction relative to the camera ("from a window behind the camera"), never
   just "from the right". The first shelf shot invented a window that broke the office layout.
3. **Clocks:** keep clock faces out of AI clips. Use a still with a digital camera move, or cut at the frame where the
   hands are right. The model animated the hands in both clock clips despite explicit instructions.
4. **Supporting characters:** render secondary characters with the approved Wren reference as a **style-only
   reference**, so every character sits at the same level of stylization.
5. **Appear/disappear effects:** do them as **image edits plus a crossfade**. Edits are pixel-faithful (the umbrella
   and the clock hands), cheap (1.5 credits), and need no AI motion.
6. **Text artifacts:** check every prop close-up for lettering. One tiny maker's mark appeared on the umbrella; it
   was retouched locally.
7. **Rate limits:** submit at most about 4 image, 2 video, or 2 audio jobs at once. Rejections cost nothing.
8. **Stills:** a still with a digital push is free and suits establishing shots and object shots. Use it wherever
   motion adds nothing.

## 3. Cost projection per episode (`PROPOSED`, Lite tier, measured prices)

| Line item | Episode 1 | Episodes 2–6 (each) | Basis |
|---|---|---|---|
| Series references (32 characters, 17 locations, 20 props; mostly one-time) | about 130 | about 15 (new or changed only) | 69 × 1.5, plus about 25% retries |
| Keyframes (30–40) | about 55–75 | about 55–75 | 1.5 each, plus about 25% retries |
| Clips (45–60 shots; about 30% done as free stills with digital moves) | about 190–250 | about 190–250 | 5 per clip, plus about 20% retries |
| Narration and dialogue (about 60–80 lines) | about 30–40 | about 30–40 | 0.4 per line, plus retakes |
| Music and SFX | not yet priced | — | Priced in Prompt 08 |
| **Estimated total** | **about 405–495 credits** | **about 290–380 credits** | |

The **current balance of 97.8 credits does not cover Episode 1.** A bigger plan or a credit top-up is a **material
spending decision for the owner**. On the higher video tier (`grok_video_v15`, 22.5 per clip) the clip line alone
becomes about 850–1,100 credits per episode. The test does not justify that tier; Lite held identity well.

## 4. Decisions for the owner

1. **Approve the two character references as series canon?** Wren `E001_CHR_wren_front_v01.png`; Ida
   `E001_CHR_ida_front_v02.png` (v01 rejected for style).
2. **Approve the platform-at-midnight location reference as canon?** `E001_LOC_platform_midnight_wide_v01.png`.
3. **Ida's key bow:** the model drew a round five-petal flower in both renders. `PROPOSED`: adopt the round flower as
   canon (it renders reliably) instead of the larkspur spike in `props.md`.
4. **Narrator voice:** Annie (in the render) or Evie (`audio/*_evie_v01.wav`). Pitch only shortlists; please listen.
   The commercial-use rights of Higgsfield voices and the starter plan must be confirmed before anything is
   published.
5. **Budget for Episode 1:** see §3. Full-episode spend (Prompts 06–08) is still **not approved**, and the paid tools
   are blocked again.

## 5. Not covered by this test

- Music and real sound effects: placeholders were synthesized locally.
- Lip-sync: narration only.
- The 6:14 train.
- Daylight and golden-hour scenes.
- Theo, Crane, and Abe.
- Remotion: the assembly was done with ffmpeg; `05-EDIT/` is set up in Prompt 09.
