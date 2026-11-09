# Asset Manifest — EPISODE-001

Status: **Episode 1 assets generated and verified (fast-track, 2026-11-09).** Generated this run: **39 images, 9 clips,
33 voice files, 2 music beds, 2 SFX** (83.58 credits; see `run-log.md`). Plus 7 SFX/music files synthesized locally (free). Canon: Wren v01, Ida v02,
platform-midnight v01 **APPROVED** (owner, 2026-11-09). Theo front v01: **VERIFIED, `PROPOSED — NEEDS APPROVAL` as canon**.
Last verified: 2026-11-09 (`find` and ffprobe on this folder; listing below).

Status values: `PLANNED` (prompt written, not submitted) · `SUBMITTED` · `GENERATED` (file saved, not yet inspected) ·
`VERIFIED` (file exists and passed the continuity checklist) · `REJECTED` · `APPROVED` (owner signed off; now
canon) · `BLOCKED`.

A row may say GENERATED, VERIFIED, or APPROVED only if the file exists at the listed path.

---

## Tool availability (checked 2026-11-09)

| Need | Tool | Connected? | How verified | Use permitted? |
|---|---|---|---|---|
| Images / video / audio | Higgsfield MCP | **Yes**: starter plan, **14.22 credits** after Episode 1 | `balance` + transaction log | Episode 1 spend approved and **used**; tools blocked again (35 deny entries) |
| Voice | ElevenLabs | No | No integration present | — (manual handoff, or Higgsfield audio, if rights are confirmed) |
| Assembly | ffmpeg 6.1.1 + numpy (`tools/assemble.py`) | Yes | Review render built | Local, free. Remotion not needed for this format |
| Publishing | YouTube | No | No integration present | Manual upload; any upload needs explicit owner authorization |

## Manifest

| Asset ID | File path | Type | Source refs | Tool / model | Status | QC | Credits | Retries | Cost (USD) | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| E001_CHR_wren_front | `references/characters/E001_CHR_wren_front_v01.png` | Character ref | none (first image of this character) | gpt_image_2_6 (high, 1k), job 21ea2f37 | APPROVED | pass (all §A2 locks; style) | 1.5 | 0 | — | POW-001. **APPROVED AS CANON 2026-11-09 (owner)** |
| E001_CHR_wren_side | `references/characters/E001_CHR_wren_side_v01.png` | Character ref | approved E001_CHR_wren_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-02 |
| E001_CHR_wren_34 | `references/characters/E001_CHR_wren_34_v01.png` | Character ref | approved E001_CHR_wren_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-03 |
| E001_CHR_wren_full | `references/characters/E001_CHR_wren_full_v01.png` | Character ref | approved E001_CHR_wren_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-04 |
| E001_CHR_wren_expr | `references/characters/E001_CHR_wren_expr_v01.png` | Character ref | approved E001_CHR_wren_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-05 |
| E001_CHR_ida_front | `references/characters/E001_CHR_ida_front_v02.png` | Character ref | v01 (design) + Wren v01 (style only) | gpt_image_2_6 (high, 1k), job 54574eff | APPROVED | pass (all §A2 locks; style) | 3.0 | 1 | — | POW-001. v01 (job 517f057c) REJECTED: style too realistic. **APPROVED AS CANON 2026-11-09 (owner)** |
| E001_CHR_ida_side | `references/characters/E001_CHR_ida_side_v01.png` | Character ref | approved E001_CHR_ida_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-07 |
| E001_CHR_ida_34 | `references/characters/E001_CHR_ida_34_v01.png` | Character ref | approved E001_CHR_ida_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-08 |
| E001_CHR_ida_full | `references/characters/E001_CHR_ida_full_v01.png` | Character ref | approved E001_CHR_ida_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-09 |
| E001_CHR_ida_expr | `references/characters/E001_CHR_ida_expr_v01.png` | Character ref | approved E001_CHR_ida_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-10 |
| E001_CHR_theo_front | `references/characters/E001_CHR_theo_front_v01.png` | Character ref | Wren v01 (style only) | gpt_image_2_6 high | VERIFIED | locks pass (run-log item 1) | 1.5 | 0 | — | CR-11 prompt + style ref. PROPOSED — NEEDS APPROVAL as canon |
| E001_CHR_theo_side | `references/characters/E001_CHR_theo_side_v01.png` | Character ref | approved E001_CHR_theo_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-12 |
| E001_CHR_theo_34 | `references/characters/E001_CHR_theo_34_v01.png` | Character ref | approved E001_CHR_theo_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-13 |
| E001_CHR_theo_full | `references/characters/E001_CHR_theo_full_v01.png` | Character ref | approved E001_CHR_theo_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-14 |
| E001_CHR_theo_expr | `references/characters/E001_CHR_theo_expr_v01.png` | Character ref | approved E001_CHR_theo_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-15 |
| E001_CHR_crane_front | `references/characters/E001_CHR_crane_front_v01.png` | Character ref | none (first image of this character) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-16 |
| E001_CHR_crane_side | `references/characters/E001_CHR_crane_side_v01.png` | Character ref | approved E001_CHR_crane_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-17 |
| E001_CHR_crane_34 | `references/characters/E001_CHR_crane_34_v01.png` | Character ref | approved E001_CHR_crane_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-18 |
| E001_CHR_crane_full | `references/characters/E001_CHR_crane_full_v01.png` | Character ref | approved E001_CHR_crane_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-19 |
| E001_CHR_crane_expr | `references/characters/E001_CHR_crane_expr_v01.png` | Character ref | approved E001_CHR_crane_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-20 |
| E001_CHR_abe_front | `references/characters/E001_CHR_abe_front_v01.png` | Character ref | none (first image of this character) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-21 |
| E001_CHR_abe_side | `references/characters/E001_CHR_abe_side_v01.png` | Character ref | approved E001_CHR_abe_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-22 |
| E001_CHR_abe_34 | `references/characters/E001_CHR_abe_34_v01.png` | Character ref | approved E001_CHR_abe_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-23 |
| E001_CHR_abe_full | `references/characters/E001_CHR_abe_full_v01.png` | Character ref | approved E001_CHR_abe_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-24 |
| E001_CHR_abe_expr | `references/characters/E001_CHR_abe_expr_v01.png` | Character ref | approved E001_CHR_abe_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-25 |
| E001_CHR_ledger_front | `references/characters/E001_CHR_ledger_front_v01.png` | Character ref | none (first image of this character) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-26 |
| E001_CHR_ledger_side | `references/characters/E001_CHR_ledger_side_v01.png` | Character ref | approved E001_CHR_ledger_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-27 |
| E001_CHR_ledger_34 | `references/characters/E001_CHR_ledger_34_v01.png` | Character ref | approved E001_CHR_ledger_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-28 |
| E001_CHR_ledger_full | `references/characters/E001_CHR_ledger_full_v01.png` | Character ref | approved E001_CHR_ledger_front | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-29 |
| E001_CHR_ledger_expr | `references/characters/E001_CHR_ledger_expr_v01.png` | Character ref | approved E001_CHR_ledger_front (+ _34 for the expression sheet) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-30 |
| E001_PRP_keeperphoto | `references/props/E001_PRP_keeperphoto_v01.png` | Prop (photo variants) | approved E001_CHR_ida_front, E001_CHR_crane_front, E001_CHR_wren_front (likeness: young Ida, teen Ansel, Nora) | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-31 |
| E001_CHR_passenger_back | `references/characters/E001_CHR_passenger_back_v01.png` | Extra ref | none | — | PLANNED | — | 0 | 0 | 0 | Prompt in prompts.md CR-32 |
| E001_LOC_platform_gold_wide | `references/locations/E001_LOC_platform_gold_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_platform_day_wide | `references/locations/E001_LOC_platform_day_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_platform_overcast_wide | `references/locations/E001_LOC_platform_overcast_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_platform_dawn_wide | `references/locations/E001_LOC_platform_dawn_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_platform_dusk_wide | `references/locations/E001_LOC_platform_dusk_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_platform_midnight_wide | `references/locations/E001_LOC_platform_midnight_wide_v01.png` | Location ref | none (master) | gpt_image_2_6 (high, 1k), job 9af21ca8 | APPROVED | pass (§A3 platform) | 1.5 | 0 | — | POW-001. The clock reads 10:08, so it is time-neutral; the midnight version is POW001_SH01_KF_v01. **APPROVED AS CANON 2026-11-09 (owner)** |
| E001_LOC_platform_overcast_clockoff_wide | `references/locations/E001_LOC_platform_overcast_clockoff_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_office_day_wide | `references/locations/E001_LOC_office_day_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_office_lamp_wide | `references/locations/E001_LOC_office_lamp_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_office_midnight_wide | `references/locations/E001_LOC_office_midnight_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_office_day_stairbroken_wide | `references/locations/E001_LOC_office_day_stairbroken_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_office_midnight_ladder_wide | `references/locations/E001_LOC_office_midnight_ladder_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_clockroom_day_wide | `references/locations/E001_LOC_clockroom_day_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_clockroom_midnight_wide | `references/locations/E001_LOC_clockroom_midnight_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_clockroom_midnight_draweropen_wide | `references/locations/E001_LOC_clockroom_midnight_draweropen_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_kitchen_day_wide | `references/locations/E001_LOC_kitchen_day_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_LOC_kitchen_lamp_wide | `references/locations/E001_LOC_kitchen_lamp_wide_v01.png` | Location ref | none (master) | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_umbrella | `references/props/E001_PRP_umbrella_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_whistle | `references/props/E001_PRP_whistle_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_idakey | `references/props/E001_PRP_idakey_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_ledger | `references/props/E001_PRP_ledger_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_redthread | `references/props/E001_PRP_redthread_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_watch | `references/props/E001_PRP_watch_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_watchcracked | `references/props/E001_PRP_watchcracked_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_notebook | `references/props/E001_PRP_notebook_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_clock | `references/props/E001_PRP_clock_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_earlyshelf | `references/props/E001_PRP_earlyshelf_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_drawer | `references/props/E001_PRP_drawer_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_memset | `references/props/E001_PRP_memset_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_toytrain | `references/props/E001_PRP_toytrain_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_mitten | `references/props/E001_PRP_mitten_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_lantern | `references/props/E001_PRP_lantern_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_case | `references/props/E001_PRP_case_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_crate | `references/props/E001_PRP_crate_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_trolley | `references/props/E001_PRP_trolley_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_carkeys | `references/props/E001_PRP_carkeys_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |
| E001_PRP_railcar | `references/props/E001_PRP_railcar_v01.png` | Prop ref | none | — | PLANNED | — | 0 | 0 | 0 | prompts.md |

**Episode references total: 6.0 credits** (inside the POW-001 spend)

## Episode 1 production assets (generated 2026-11-09)

| Asset ID | File path | Type | Tool / model | Status | Notes |
|---|---|---|---|---|---|
| E001_CHR_theo_front_v01 | `references/characters/E001_CHR_theo_front_v01.png` | Character ref | gpt_image_2_6 high | VERIFIED | PROPOSED — NEEDS APPROVAL as canon |
| E001_S02_SH01_KF_v01 | `images/keyframes/E001_S02_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH02_KF_v01 | `images/keyframes/E001_S02_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH03_KF_v01 | `images/keyframes/E001_S02_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | REJECTED | 3 clock hands; replaced by v02 edit |
| E001_S02_SH03_KF_v02 | `images/keyframes/E001_S02_SH03_KF_v02.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH04_KF_v01 | `images/keyframes/E001_S02_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH05_KF_v01 | `images/keyframes/E001_S02_SH05_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH06_KF_v01 | `images/keyframes/E001_S02_SH06_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH07_KF_v01 | `images/keyframes/E001_S02_SH07_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH08_KF_v01 | `images/keyframes/E001_S02_SH08_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH01_KF_v01 | `images/keyframes/E001_S03_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH02_KF_v01 | `images/keyframes/E001_S03_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH03_KF_v01 | `images/keyframes/E001_S03_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH04_KF_v01 | `images/keyframes/E001_S03_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH05_KF_v01 | `images/keyframes/E001_S03_SH05_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S03_SH06_KF_v01 | `images/keyframes/E001_S03_SH06_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S04_SH01_KF_v01 | `images/keyframes/E001_S04_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S04_SH02_KF_v01 | `images/keyframes/E001_S04_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S04_SH03_KF_v01 | `images/keyframes/E001_S04_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S05_SH01_KF_v01 | `images/keyframes/E001_S05_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S05_SH02_KF_v01 | `images/keyframes/E001_S05_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | REJECTED | grille shelves in hallway; replaced by v02 edit |
| E001_S05_SH02_KF_v02 | `images/keyframes/E001_S05_SH02_KF_v02.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S05_SH03_KF_v01 | `images/keyframes/E001_S05_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S06_SH01_KF_v01 | `images/keyframes/E001_S06_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S06_SH02_KF_v01 | `images/keyframes/E001_S06_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S06_SH03_KF_v01 | `images/keyframes/E001_S06_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S06_SH04_KF_v01 | `images/keyframes/E001_S06_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S06_SH05_KF_v01 | `images/keyframes/E001_S06_SH05_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S07_SH01_KF_v01 | `images/keyframes/E001_S07_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S07_SH02_KF_v01 | `images/keyframes/E001_S07_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S07_SH03_KF_v01 | `images/keyframes/E001_S07_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S07_SH04_KF_v01 | `images/keyframes/E001_S07_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S08_SH01_KF_v01 | `images/keyframes/E001_S08_SH01_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S08_SH02_KF_v01 | `images/keyframes/E001_S08_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S08_SH03_KF_v01 | `images/keyframes/E001_S08_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S08_SH04_KF_v01 | `images/keyframes/E001_S08_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S09_SH02_KF_v01 | `images/keyframes/E001_S09_SH02_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S09_SH03_KF_v01 | `images/keyframes/E001_S09_SH03_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S09_SH04_KF_v01 | `images/keyframes/E001_S09_SH04_KF_v01.png` | Keyframe | gpt_image_2_6 high | VERIFIED |  |
| E001_S09_SH05_KF_v01 | `images/keyframes/E001_S09_SH05_KF_v01.png` | Keyframe | gpt_image_2_6 medium | VERIFIED |  |
| E001_S02_SH01_CLIP_v01 | `clips/E001_S02_SH01_CLIP_v01.mp4` | Clip | grok_video_v15_lite 4.0s | VERIFIED | trimmed in edit |
| E001_S02_SH02_CLIP_v01 | `clips/E001_S02_SH02_CLIP_v01.mp4` | Clip | grok_video_v15_lite 3.0s | VERIFIED |  |
| E001_S02_SH07_CLIP_v01 | `clips/E001_S02_SH07_CLIP_v01.mp4` | Clip | grok_video_v15_lite 3.0s | VERIFIED |  |
| E001_S03_SH06_CLIP_v01 | `clips/E001_S03_SH06_CLIP_v01.mp4` | Clip | grok_video_v15_lite 3.0s | VERIFIED |  |
| E001_S05_SH01_CLIP_v01 | `clips/E001_S05_SH01_CLIP_v01.mp4` | Clip | grok_video_v15_lite 4.0s | VERIFIED | trimmed in edit |
| E001_S06_SH04_CLIP_v01 | `clips/E001_S06_SH04_CLIP_v01.mp4` | Clip | grok_video_v15_lite 4.0s | VERIFIED |  |
| E001_S07_SH01_CLIP_v01 | `clips/E001_S07_SH01_CLIP_v01.mp4` | Clip | grok_video_v15_lite 3.0s | VERIFIED |  |
| E001_S09_SH04_CLIP_v01 | `clips/E001_S09_SH04_CLIP_v01.mp4` | Clip | grok_video_v15_lite 3.0s | VERIFIED |  |
| E001_S09_SH05_CLIP_v01 | `clips/E001_S09_SH05_CLIP_v01.mp4` | Clip | grok_video_v15_lite 4.0s | VERIFIED |  |
| E001_VO_ida_L002_v01 | `audio/dialogue/E001_VO_ida_L002_v01.wav` | Voice | seed_audio | GENERATED | 4.8s; awaiting owner listen |
| E001_VO_ida_L004_v01 | `audio/dialogue/E001_VO_ida_L004_v01.wav` | Voice | seed_audio | GENERATED | 7.5s; awaiting owner listen |
| E001_VO_ida_L007_v01 | `audio/dialogue/E001_VO_ida_L007_v01.wav` | Voice | seed_audio | GENERATED | 2.0s; awaiting owner listen |
| E001_VO_ida_L009_v01 | `audio/dialogue/E001_VO_ida_L009_v01.wav` | Voice | seed_audio | GENERATED | 3.9s; awaiting owner listen |
| E001_VO_ida_L011_v01 | `audio/dialogue/E001_VO_ida_L011_v01.wav` | Voice | seed_audio | GENERATED | 3.9s; awaiting owner listen |
| E001_VO_ida_L013_v01 | `audio/dialogue/E001_VO_ida_L013_v01.wav` | Voice | seed_audio | GENERATED | 3.9s; awaiting owner listen |
| E001_VO_ida_L025_v01 | `audio/dialogue/E001_VO_ida_L025_v01.wav` | Voice | seed_audio | GENERATED | 2.1s; awaiting owner listen |
| E001_VO_ida_L027_v01 | `audio/dialogue/E001_VO_ida_L027_v01.wav` | Voice | seed_audio | GENERATED | 14.8s; awaiting owner listen |
| E001_VO_ida_L029_v01 | `audio/dialogue/E001_VO_ida_L029_v01.wav` | Voice | seed_audio | GENERATED | 3.0s; awaiting owner listen |
| E001_VO_narr_L000_v01 | `audio/dialogue/E001_VO_narr_L000_v01.wav` | Voice | POW-001 reuse | GENERATED | 6.5s; awaiting owner listen |
| E001_VO_narr_L001_v01 | `audio/dialogue/E001_VO_narr_L001_v01.wav` | Voice | seed_audio | GENERATED | 19.6s; awaiting owner listen |
| E001_VO_narr_L003_v01 | `audio/dialogue/E001_VO_narr_L003_v01.wav` | Voice | seed_audio | GENERATED | 17.8s; awaiting owner listen |
| E001_VO_narr_L005_v01 | `audio/dialogue/E001_VO_narr_L005_v01.wav` | Voice | seed_audio | GENERATED | 16.3s; awaiting owner listen |
| E001_VO_narr_L010_v01 | `audio/dialogue/E001_VO_narr_L010_v01.wav` | Voice | seed_audio | GENERATED | 7.3s; awaiting owner listen |
| E001_VO_narr_L014_v01 | `audio/dialogue/E001_VO_narr_L014_v01.wav` | Voice | seed_audio | GENERATED | 4.1s; awaiting owner listen |
| E001_VO_narr_L015_v01 | `audio/dialogue/E001_VO_narr_L015_v01.wav` | Voice | seed_audio | GENERATED | 11.5s; awaiting owner listen |
| E001_VO_narr_L016_v01 | `audio/dialogue/E001_VO_narr_L016_v01.wav` | Voice | seed_audio | GENERATED | 5.1s; awaiting owner listen |
| E001_VO_narr_L017_v01 | `audio/dialogue/E001_VO_narr_L017_v01.wav` | Voice | seed_audio | GENERATED | 18.8s; awaiting owner listen |
| E001_VO_narr_L018_v01 | `audio/dialogue/E001_VO_narr_L018_v01.wav` | Voice | seed_audio | GENERATED | 18.3s; awaiting owner listen |
| E001_VO_narr_L019_v01 | `audio/dialogue/E001_VO_narr_L019_v01.wav` | Voice | seed_audio | GENERATED | 13.2s; awaiting owner listen |
| E001_VO_narr_L021_v01 | `audio/dialogue/E001_VO_narr_L021_v01.wav` | Voice | seed_audio | GENERATED | 3.9s; awaiting owner listen |
| E001_VO_narr_L023_v01 | `audio/dialogue/E001_VO_narr_L023_v01.wav` | Voice | seed_audio | GENERATED | 5.3s; awaiting owner listen |
| E001_VO_narr_L031_v01 | `audio/dialogue/E001_VO_narr_L031_v01.wav` | Voice | seed_audio | GENERATED | 4.4s; awaiting owner listen |
| E001_VO_narr_L032_v01 | `audio/dialogue/E001_VO_narr_L032_v01.wav` | Voice | seed_audio | GENERATED | 21.1s; awaiting owner listen |
| E001_VO_narr_L033_v01 | `audio/dialogue/E001_VO_narr_L033_v01.wav` | Voice | seed_audio | GENERATED | 3.7s; awaiting owner listen |
| E001_VO_theo_L020_v01 | `audio/dialogue/E001_VO_theo_L020_v01.wav` | Voice | seed_audio | GENERATED | 2.6s; awaiting owner listen |
| E001_VO_theo_L022_v01 | `audio/dialogue/E001_VO_theo_L022_v01.wav` | Voice | seed_audio | GENERATED | 7.6s; awaiting owner listen |
| E001_VO_wren_L006_v01 | `audio/dialogue/E001_VO_wren_L006_v01.wav` | Voice | seed_audio | GENERATED | 1.1s; awaiting owner listen |
| E001_VO_wren_L008_v01 | `audio/dialogue/E001_VO_wren_L008_v01.wav` | Voice | seed_audio | GENERATED | 1.5s; awaiting owner listen |
| E001_VO_wren_L012_v01 | `audio/dialogue/E001_VO_wren_L012_v01.wav` | Voice | seed_audio | GENERATED | 3.6s; awaiting owner listen |
| E001_VO_wren_L024_v01 | `audio/dialogue/E001_VO_wren_L024_v01.wav` | Voice | seed_audio | GENERATED | 3.6s; awaiting owner listen |
| E001_VO_wren_L026_v01 | `audio/dialogue/E001_VO_wren_L026_v01.wav` | Voice | seed_audio | GENERATED | 0.8s; awaiting owner listen |
| E001_VO_wren_L028_v01 | `audio/dialogue/E001_VO_wren_L028_v01.wav` | Voice | seed_audio | GENERATED | 2.3s; awaiting owner listen |
| E001_VO_wren_L030_v01 | `audio/dialogue/E001_VO_wren_L030_v01.wav` | Voice | seed_audio | GENERATED | 2.3s; awaiting owner listen |
| E001_MUS_midnight_v01 | `audio/music/E001_MUS_midnight_v01.wav` | Music | elevenlabs_music_v2 | GENERATED | 60.0s |
| E001_MUS_momsong_v01 | `audio/music/E001_MUS_momsong_v01.wav` | Music | local synth (numpy) | GENERATED | 10.1s |
| E001_MUS_warm_v01 | `audio/music/E001_MUS_warm_v01.wav` | Music | elevenlabs_music_v2 | GENERATED | 60.0s |
| E001_SFX_bell_v01 | `audio/sfx/E001_SFX_bell_v01.wav` | SFX | local synth (numpy) | GENERATED | 5.0s |
| E001_SFX_drips_v01 | `audio/sfx/E001_SFX_drips_v01.wav` | SFX | local synth (numpy) | GENERATED | 30.0s |
| E001_SFX_roomtone_v01 | `audio/sfx/E001_SFX_roomtone_v01.wav` | SFX | local synth (numpy) | GENERATED | 60.0s |
| E001_SFX_shimmer_v01 | `audio/sfx/E001_SFX_shimmer_v01.wav` | SFX | local synth (numpy) | GENERATED | 4.0s |
| E001_SFX_tick_v01 | `audio/sfx/E001_SFX_tick_v01.wav` | SFX | local synth (numpy) | GENERATED | 0.1s |
| E001_SFX_train_arrive_v01 | `audio/sfx/E001_SFX_train_arrive_v01.wav` | SFX | mirelo | GENERATED | 10.0s |
| E001_SFX_train_depart_v01 | `audio/sfx/E001_SFX_train_depart_v01.wav` | SFX | mirelo | GENERATED | 8.0s |
| E001_SFX_wind_v01 | `audio/sfx/E001_SFX_wind_v01.wav` | SFX | local synth (numpy) | GENERATED | 60.0s |
