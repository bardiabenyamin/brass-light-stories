# Character References — series canon (held in EPISODE-001)

Status: **2 of 32 exist and are APPROVED AS CANON (owner, 2026-11-09).** 30 PENDING. Copy-ready prompts are written (`../../prompts.md` § "Character
reference batch", CR-01 to CR-32). Generation is **on hold until Prompt 03 is complete** (owner instruction,
2026-11-09). After that, only **Wren and Ida** are generated first, for the proof-of-work. Never list an image here as
existing unless the file is in this folder.

Design source: `../../characters.md`. Inspection: `../../continuity.md` §A and §A2.

## Required files: `E001_CHR_<ref>_<view>_v01.png`

| Ref ID | Character | front | side | 34 | full | expr | Approved as canon |
|---|---|---|---|---|---|---|---|
| `wren` | Wren Halloway | **APPROVED** `_v01` | PENDING | PENDING | PENDING | PENDING | **Canon 2026-11-09** |
| `ida` | Ida Halloway | **APPROVED** `_v02` (v01 rejected: style) | PENDING | PENDING | PENDING | PENDING | **Canon 2026-11-09** |
| `theo` | Theo Marsh | **VERIFIED** `_v01` (PROPOSED as canon) | PENDING | PENDING | PENDING | PENDING | — |
| `crane` | Ansel Crane | PENDING | PENDING | PENDING | PENDING | PENDING | — |
| `abe` | Abe Crane | PENDING | PENDING | PENDING | PENDING | PENDING | — |
| `ledger` | Ledger (cat) | PENDING | PENDING | PENDING | PENDING | PENDING | — |

| Extra | File | Status |
|---|---|---|
| Umbrella passenger (back view only) | `E001_CHR_passenger_back_v01.png` | PENDING |
| Keepers' photo (young Ida, teen Ansel, child Nora) | `../props/E001_PRP_keeperphoto_v01.png` | PENDING |

Framing and aspect ratio: front, side, and ¾ are waist-up at 4:5 · full body is 2:3 · the expression sheet is a 3×2
grid at 3:2 · the cat uses 1:1 or 4:3 · the photo is 3:2.

## Approval procedure (per character)

1. Generate **front** → inspect against `continuity.md` §A2 → if it fails, retry (at most 2 without approval) with a
   new version number (`_v02`); never overwrite.
2. Once the front is approved, generate side, ¾, and full body using the approved front as the image reference (and the
   tool's character or reference feature, if available). Then generate the expression sheet.
3. Check that all five match each other and the locks. Mark `Approved as canon` with the date. Log it in
   `../../assets.md` and `../../../../COST-LOG.md`.
4. Approved references are **series canon**. Replacing one requires owner approval and a copy in `../../_backups/`.

**Lesson from POW-001:** generate every other character with the approved Wren front as a **style-only** reference ("use the second image only for rendering style"). Without it, older faces drift toward realism.
