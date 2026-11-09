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

**Running total: 44.6 credits** (balance 142.4 → 97.8, checked 2026-11-09). Rate-limited submissions (5) were not charged.
