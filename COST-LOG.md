# Cost Log (channel-wide)

Log every paid action: generations, retries, upscales, voice, music, and subscriptions. Episode-level detail also
goes in that episode's `assets.md`.

## Budget

| Item | Value | Status |
|---|---|---|
| Proof-of-work test credit cap | "as needed" (owner, 2026-11-09); working ceiling about 70 credits (`PROPOSED`) | APPROVED, effective after Prompt 03 |
| Per-episode credit cap | — | MISSING: NEEDS OWNER INPUT |
| Monthly tool spend ceiling (USD) | — | MISSING: NEEDS OWNER INPUT |

## Tool accounts (verified)

| Tool | Verified | Plan | Balance at check | Method |
|---|---|---|---|---|
| Higgsfield (MCP) | 2026-11-09 | starter | 142.4 credits | Read-only `balance` call. Nothing spent |
| ElevenLabs | Not connected | — | — | No integration in this session |
| YouTube | Not connected | — | — | No integration in this session |

Commercial-use rights for each plan: **NOT VERIFIED**. The owner must confirm in each tool's plan terms before any
monetized upload.

## Spend log

| Date | Episode/test | Tool | Model/action | Asset IDs | Credits | Retries | Approx. USD | Approved by | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-09 | Setup | — | — | — | 0 | 0 | 0 | — | Setup only. No assets generated |
| 2026-11-09 | POW-001 | Higgsfield | gpt_image_2_6 (high, 1k): 2 character refs, 1 location ref, 6 keyframes, 3 retries/edits | E001_CHR_wren_front_v01, E001_CHR_ida_front_v01/v02, E001_LOC_platform_midnight_wide_v01, POW001_SH01–SH07 KFs | 18.0 | 2 (Ida style, SH03 geography) + 1 edit | — | Owner, 2026-11-09 ("as needed, after Prompt 03") | 12 × 1.5 |
| 2026-11-09 | POW-001 | Higgsfield | grok_video_v15_lite (5 s, 720p): 5 clips | POW001_SH01/02/05/06/07_CLIP_v01 | 25.0 | 0 | — | Owner, 2026-11-09 | 5 × 5 |
| 2026-11-09 | POW-001 | Higgsfield | seed_audio: 4 narration lines (2 voices) | POW001_VO_wren_L001/L002_{annie,evie}_v01 | 1.6 | 0 | — | Owner, 2026-11-09 | 4 × 0.4 |

| 2026-11-09 | EPISODE-001 | Higgsfield | gpt_image_2_6 · 1k: 37 medium (0.5) + 2 high (1.5: Theo canon ref, two-whistles hero) | E001_CHR_theo_front_v01; E001_S02–S09 keyframes (39 files incl. 2 fix edits) | 22.0 | 2 targeted edits (clock hands, hallway shelves) | — | Owner, 2026-11-09 ("Episode 1 spend cap: as needed but spent wisely") | Exact, from the Higgsfield transaction log |
| 2026-11-09 | EPISODE-001 | Higgsfield | grok_video_v15_lite · 720p: 9 clips (3–4 s, 1 credit/s) | E001_S02_SH01/02/07, S03_SH06, S05_SH01, S06_SH04, S07_SH01, S09_SH04/05 _CLIP_v01 | 31.0 | 0 | — | Owner, 2026-11-09 | |
| 2026-11-09 | EPISODE-001 | Higgsfield | seed_audio: 33 voice jobs (Annie, Vera, Archie), 474 words | E001_VO_*_L001–L033_v01 | 18.4 | 0 | — | Owner, 2026-11-09 | About 0.039 per word with per-job rounding (higher than the 0.033 preflight) |
| 2026-11-09 | EPISODE-001 | Higgsfield | elevenlabs_music_v2 instrumental: 2 × 60 s | E001_MUS_warm_v01, E001_MUS_midnight_v01 | 7.68 | 0 | — | Owner, 2026-11-09 | |
| 2026-11-09 | EPISODE-001 | Higgsfield | mirelo SFX: train arrival 10 s, departure 8 s | E001_SFX_train_arrive_v01, E001_SFX_train_depart_v01 | 4.5 | 0 | — | Owner, 2026-11-09 | Other SFX and Mom's song synthesized locally (free) |
| 2026-11-09 | EPISODE-001 | local ffmpeg/numpy | Assembly, mix, loudness | E001_RENDER_master/review_v01 | 0 | — | — | — | |
| 2026-11-09 | EPISODE-001 v02 fixes | Higgsfield | grok_video_v15_lite: 3 clips (Theo talking 3 s + 6 s, Theo watch 3 s); gpt_image_2_6 medium: 3 edits | E001_S07_SH01_CLIP_v02, E001_S07_SH03_CLIP_v01, E001_S02_SH08_CLIP_v01; E001_S03_SH01_KF_v02, E001_S02_SH06_KF_v02, E001_S06_SH04_PLATE_KF_v01 | 13.5 | 0 | — | Owner, 2026-11-09 ("Use the remaining balance credits to animate as much as you can") | Fix pass after owner QC of v01 |

**Running total: 141.68 credits** (POW-001 44.6 + EPISODE-001 83.58 + v02 fixes 13.5). Balance 142.4 → 97.8 → 14.22 → **0.72** (each checked with `balance` and the transaction log). Rate-limited submissions were not charged.
