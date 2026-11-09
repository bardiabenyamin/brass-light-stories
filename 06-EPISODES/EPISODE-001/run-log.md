# EPISODE-001 production run log (fast-track, 2026-11-09)

Every paid submission, with job ID, cost, output file, and inspection result. Prices were measured by preflight.
Prompts are built by `tools/e001_spec.py` from the locked blocks; job IDs are mirrored in `tools/jobs.json`.
Budget: owner's "as needed but spent wisely" on the free starter plan, so the working ceiling is the **97.8 credits** on the account.

## Measured prices (preflight, 2026-11-09)

| Item | Credits |
|---|---|
| gpt_image_2_6 · 1k · medium (with references) | 0.5 |
| gpt_image_2_6 · 1k · high | 1.5 |
| gpt_image_2_6 · 2k · medium / 1k · low | 1.0 / 0.25 |
| grok_video_v15_lite (any resolution) | 1.0 per second (1–15 s) |
| kling3_0_turbo 3 s / happy_horse 3 s (not used) | 4.5 / 7.5 |
| seed_audio speech | about 0.033 per word |
| elevenlabs_music_v2 instrumental | 0.064 per second |
| mirelo_text_to_audio SFX | 0.25 per second |

## Balance checkpoints

| When | Balance | Spent this run |
|---|---|---|
| Start | 97.8 | 0 |

## Jobs

| # | Item | Settings | Job ID | Credits | Output | Inspection |
|---|---|---|---|---|---|---|
| 1 | REF_THEO (canon front) | high · 4:5 · style ref Wren v01 | `40c51c02-3824-4533-9e04-8626d1380e94` | 1.5 | `references/characters/E001_CHR_theo_front_v01.png` | **Pass:** copper curls, thin round gold-wire glasses, hazel eyes, prominent ears, indigo chore coat, grey tee, tobacco trousers, watch chain from his **left** breast pocket. Five-finger hands. Style matches Wren. A few faint skin marks on the nose (spec says no freckles); acceptable |
| 2 | S02_SH01 railcar leaves the tunnel | medium · 16:9 · ref platform-midnight | `a40e9361-40b7-453e-99dc-31445bf70d23` | 0.5 | `images/keyframes/E001_S02_SH01_KF_v01.png` | **Pass:** tunnel at image left, railcar livery correct (slate-teal, cream, brass stripe, round lamps), clock out of frame, sun above the ridge on the left. Note: the platform lamp is lit (GOLD says unlit); acceptable at 6:14 |
| 3 | S03_SH01 office wide, Ida leads Wren in | medium · refs Ida v02, Wren v01 | `9e63d1f6-5b9f-4546-8d5f-b707f08fd03e` | 0.5 | `images/keyframes/E001_S03_SH01_KF_v01.png` | **Pass, with a geography flag:** identities, wardrobe, green lamp, ledger, grille along the bottom shelf, window on the right, stair on the left are all correct. **The shelf wall faces the hall door** (canon: left wall). Kept, and logged as a PROPOSED canon update in `continuity.md`. **Medium quality is good enough:** the rest of the episode uses medium |
| 4 | S02_SH04 Ida waits on the platform | medium · refs Ida v02, Wren (style) | `5848c1b2-1927-4532-8152-ebde48f0aa7e` | 0.5 | `images/keyframes/E001_S02_SH04_KF_v01.png` | **Pass:** all Ida locks (bun, grey-green eyes, freckles, flower-bow key on red cord, apron, cardigan); hands folded, five fingers; looking screen-left; sun from the left |
| A01 | VO narration S02a (Annie) | seed_audio · 48 kHz | `67a54516-ebe4-40cc-b576-645ffa5a35e0` | ~1.6 | `audio/dialogue/E001_VO_narr_L001_v01.wav` (19.6 s) | Pending listen-through in the assembly |
| A03 | VO narration S02b (Annie) | seed_audio · 48 kHz | `3ebc73a0-cc4b-45a2-84e7-2708e80cb794` | ~1.6 | `audio/dialogue/E001_VO_narr_L003_v01.wav` (17.8 s) | Pending |

## All Episode 1 jobs (mirrors `tools/jobs.json`)

| Key | Job ID | Output | Inspection |
|---|---|---|---|
| REF_THEO | `40c51c02-3824-4533-9e04-8626d1380e94` | `references/characters/E001_CHR_theo_front_v01.png` | Pass (see table above) |
| S02_SH01 | `a40e9361-40b7-453e-99dc-31445bf70d23` | `images/keyframes/E001_S02_SH01_KF_v01.png` | Pass (see table above) |
| S03_SH01 | `9e63d1f6-5b9f-4546-8d5f-b707f08fd03e` | `images/keyframes/E001_S03_SH01_KF_v01.png` | Pass (see table above) |
| S02_SH04 | `5848c1b2-1927-4532-8152-ebde48f0aa7e` | `images/keyframes/E001_S02_SH04_KF_v01.png` | Pass (see table above) |
| S02_SH02 | `c80bee5d-5468-4479-ae1c-2d8a57aba2ac` | `images/keyframes/E001_S02_SH02_KF_v01.png` | Pass: Wren locks, railcar livery, open door |
| S02_SH03 | `dbbd95d3-9801-487a-83ef-b64c090443d1` | `images/keyframes/E001_S02_SH03_KF_v01.png` | Fail: three clock hands + a stray numeral → fixed by edit S02_SH03_FIX (v02) |
| S02_SH06 | `11634d29-e8b0-4396-8f00-314e75d7c43b` | `images/keyframes/E001_S02_SH06_KF_v01.png` | Pass: Wren left / Ida right, no hug, apron green in sun |
| S02_SH07 | `7e380ec5-cb0c-42e1-b3ff-a12bc9973242` | `images/keyframes/E001_S02_SH07_KF_v01.png` | Pass: Abe locks (cap, beard, brass buttons), cat eats from palm, lantern |
| A01 | `67a54516-ebe4-40cc-b576-645ffa5a35e0` | `audio/dialogue/E001_VO_narr_L001_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A03 | `3ebc73a0-cc4b-45a2-84e7-2708e80cb794` | `audio/dialogue/E001_VO_narr_L003_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A02 | `aadd6467-904e-4eb2-82fb-00607ada4a08` | `audio/dialogue/E001_VO_ida_L002_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A04 | `276f3a70-c505-4565-b68b-ef2c99f93df7` | `audio/dialogue/E001_VO_ida_L004_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S02_SH03_FIX | `1b10b310-897b-4a8d-8b95-6ca94f84b976` | `images/keyframes/E001_S02_SH03_KF_v02.png` | Pass: two hands (reads 6:14), numeral removed, rest unchanged |
| S02_SH08 | `a442fc30-03ec-479c-8561-8c1f3402097d` | `images/keyframes/E001_S02_SH08_KF_v01.png` | Pass: Theo locks, watch in left hand |
| S03_SH02 | `620026d6-f667-45c9-a099-9be20cd68e69` | `images/keyframes/E001_S03_SH02_KF_v01.png` | Pass |
| S03_SH03 | `d3064473-f416-491f-b6c3-8bbc16ca9d46` | `images/keyframes/E001_S03_SH03_KF_v01.png` | Pass: red-thread rows, no legible text |
| A05 | `fa6911ec-4e77-4aa6-b3e0-de8b54532632` | `audio/dialogue/E001_VO_narr_L005_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A06 | `cf962635-d29b-42f8-80c1-ca305e41fb8b` | `audio/dialogue/E001_VO_wren_L006_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S02_SH01_CLIP | `e945888a-b0fd-41b3-9b78-87d606cb89b5` | `clips/E001_S02_SH01_CLIP_v01.mp4` | Pass 0–3.2 s (dust puffs later) |
| S02_SH02_CLIP | `d6442079-d7ea-4582-b592-8a2f62837951` | `clips/E001_S02_SH02_CLIP_v01.mp4` | Pass |
| S02_SH05 | `422a4da7-f9ac-4957-8bcc-a769e5d2f7a0` | `images/keyframes/E001_S02_SH05_KF_v01.png` | Pass |
| S03_SH04 | `02a66c9f-184f-4be0-a5fe-accae1b1a3d3` | `images/keyframes/E001_S03_SH04_KF_v01.png` | Pass |
| S03_SH05 | `1dfd8761-4c7a-4c92-98fb-56f2fe0eefb1` | `images/keyframes/E001_S03_SH05_KF_v01.png` | Pass: lamp-lit relight of POW SH03 v02 (same layout), compartment empty |
| S03_SH06 | `236ccd4f-d3d7-4c29-8eca-afbeeb51cc71` | `images/keyframes/E001_S03_SH06_KF_v01.png` | Pass: five-petal key bow on red cord, five-finger hand |
| A07 | `84db6d48-55f1-4095-aab9-d3e27ba7f278` | `audio/dialogue/E001_VO_ida_L007_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A08 | `2f491b0a-01fd-4cc8-b656-1fa02e8bba43` | `audio/dialogue/E001_VO_wren_L008_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S02_SH07_CLIP | `61e0fbd2-64cb-4520-8229-16a7b969c159` | `clips/E001_S02_SH07_CLIP_v01.mp4` | Pass: eats, then he strokes it |
| S04_SH01 | `c613a1eb-2cc5-4efd-a173-323f95aeb13f` | `images/keyframes/E001_S04_SH01_KF_v01.png` | Pass: interior window with the lit clock face; table, stove, valley window |
| S05_SH02 | `a6ce25ee-5944-44ed-8cde-eb29476eb4ef` | `images/keyframes/E001_S05_SH02_KF_v01.png` | Fail: grille shelves drawn in the hallway → fixed by edit S05_SH02_FIX (v02) |
| S05_SH03 | `1ad6f49f-c72b-4e5c-a4ce-9d888174b226` | `images/keyframes/E001_S05_SH03_KF_v01.png` | Pass: zigzag mend legible (not text), sparrow charm |
| S06_SH01 | `e47e489e-43e1-48d5-83c1-6ae7f5383833` | `images/keyframes/E001_S06_SH01_KF_v01.png` | Pass: edit of the fixed station image, wet platform |
| A09 | `d7052ac1-349b-41b2-925c-0b6783939ae0` | `audio/dialogue/E001_VO_ida_L009_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A10 | `c4da7f98-61e6-4cb8-bf33-242317d64307` | `audio/dialogue/E001_VO_narr_L010_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S03_SH06_CLIP | `c1032962-a972-4cd8-9a81-93ae7fc6f1fb` | `clips/E001_S03_SH06_CLIP_v01.mp4` | Pass |
| A11 | `231ef3bf-d5ab-4c93-81f4-a0697997d5de` | `audio/dialogue/E001_VO_ida_L011_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A12 | `30cc7a38-f369-4001-ae35-516802a3c957` | `audio/dialogue/E001_VO_wren_L012_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S04_SH02 | `88f919ef-ec00-437c-98ca-e8d0fc7ba218` | `images/keyframes/E001_S04_SH02_KF_v01.png` | Pass |
| S04_SH03 | `619f2709-c40a-4f22-8216-e725c096d314` | `images/keyframes/E001_S04_SH03_KF_v01.png` | Pass |
| S05_SH01 | `83c5f2ee-2bb2-4aeb-9b07-ccb4c20e2784` | `images/keyframes/E001_S05_SH01_KF_v01.png` | Pass (still). Clip: she turns and walks forward; the whistle reads longer than canon when close → only 0.2–3.6 s used |
| S05_SH02_FIX | `3d80e1b0-ca13-4426-a897-9f3a2c46601a` | `images/keyframes/E001_S05_SH02_KF_v02.png` | Pass: bare wall, light under the door |
| A13 | `612532dc-bde1-4dcf-8864-568ea3a9e669` | `audio/dialogue/E001_VO_ida_L013_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A14 | `313712b4-42fe-4d3c-9d24-3ca386eddadb` | `audio/dialogue/E001_VO_narr_L014_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S06_SH02 | `a10b5635-b120-487b-8d5c-3dc5163dea78` | `images/keyframes/E001_S06_SH02_KF_v01.png` | Pass: passenger back view only, umbrella + charm, tunnel image right (reverse master) |
| S06_SH03 | `98578662-bf8d-4e5c-90dd-212a29484cc7` | `images/keyframes/E001_S06_SH03_KF_v01.png` | Pass |
| S06_SH05 | `23c03614-421d-4e7d-be3b-0dc790789a7f` | `images/keyframes/E001_S06_SH05_KF_v01.png` | Pass: pixel-faithful edit of S03_SH05 + umbrella (vanish crossfade) |
| S07_SH01 | `0de02e64-bddb-49ba-ae1e-9b9d5499a0d5` | `images/keyframes/E001_S07_SH01_KF_v01.png` | Pass: Theo + dripping umbrella |
| A15 | `46df1e9f-d7d7-4417-9766-57a9970dc017` | `audio/dialogue/E001_VO_narr_L015_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A16 | `e517abf4-92e3-44f3-b6b0-2585791ac566` | `audio/dialogue/E001_VO_narr_L016_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S05_SH01_CLIP | `64555d5b-829f-4383-945a-302c895d118f` | `clips/E001_S05_SH01_CLIP_v01.mp4` | Partial: use 0.2–3.6 s |
| MUS_warm | `ddece9ee-2d51-4f34-9e82-158ba4b4741f` | `audio/music/E001_MUS_warm_v01.wav` | Generated, 60.0 s, instrumental. Not listened to |
| MUS_midnight | `97afdbd4-9a2a-4037-b025-4988e3443f7f` | `audio/music/E001_MUS_midnight_v01.wav` | Generated, 60.0 s, instrumental. Not listened to |
| S06_SH04 | `4dcef8cc-f9a2-408b-83fe-378d6a66c644` | `images/keyframes/E001_S06_SH04_KF_v01.png` | Pass: pixel-faithful edit, woman removed, umbrella on bench |
| S07_SH02 | `28ce15c1-0814-4df6-83f3-19863beb27fa` | `images/keyframes/E001_S07_SH02_KF_v01.png` | Pass |
| S07_SH03 | `3bbe58e0-c092-480d-ab51-e2e079f78c6e` | `images/keyframes/E001_S07_SH03_KF_v01.png` | Pass: thumb toward the tower stair (K4) |
| S07_SH04 | `a6353ad2-2e22-4a2f-9a1a-fb5460688261` | `images/keyframes/E001_S07_SH04_KF_v01.png` | Pass: hands, charm; tear not legible → 'Same tear' uses S05_SH03 |
| S07_SH01_CLIP | `1d536229-97fd-43df-af6c-e14645a2c56b` | `clips/E001_S07_SH01_CLIP_v01.mp4` | Pass |
| S08_SH01 | `c0effff8-d90d-4301-af75-93df9e636d5c` | `images/keyframes/E001_S08_SH01_KF_v01.png` | Pass |
| S08_SH02 | `4de404b6-24da-4896-8906-6d882be75036` | `images/keyframes/E001_S08_SH02_KF_v01.png` | Pass |
| S08_SH03 | `fc37402f-9093-45a8-b621-0f6f4bd0222e` | `images/keyframes/E001_S08_SH03_KF_v01.png` | Pass |
| S08_SH04 | `aa370990-54e7-4795-acd6-09389da346a1` | `images/keyframes/E001_S08_SH04_KF_v01.png` | Pass |
| S06_SH04_CLIP | `ac2de9e3-3f55-4398-b224-e84f084873b1` | `clips/E001_S06_SH04_CLIP_v01.mp4` | Pass: train leaves right into the tunnel, umbrella still |
| A17 | `941d2df0-1eec-4a3a-827c-258110f533c5` | `audio/dialogue/E001_VO_narr_L017_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A18 | `e54f2e7b-bc30-436f-92c6-15721b919157` | `audio/dialogue/E001_VO_narr_L018_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S09_SH02 | `84ab5842-65b0-417d-9650-955a81df92a4` | `images/keyframes/E001_S09_SH02_KF_v01.png` | Pass: whistle arrives, glow; whistle shape slightly flared |
| S09_SH04 | `5704a768-5d49-4b27-be66-4144ead58e66` | `images/keyframes/E001_S09_SH04_KF_v01.png` | Pass (high): two whistles, one on chain, one glowing, five-finger hands |
| S09_SH05 | `3650ee77-b25d-4ab7-b485-be49559b4c42` | `images/keyframes/E001_S09_SH05_KF_v01.png` | Pass |
| A19 | `e516a8d4-a3ea-47ed-b029-f4010a0ebbf6` | `audio/dialogue/E001_VO_narr_L019_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A20 | `f8af2c2a-9179-4d2c-bc62-7773cc64beb3` | `audio/dialogue/E001_VO_theo_L020_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| S09_SH03 | `3dbefd30-1fd5-445c-b7cc-593515927803` | `images/keyframes/E001_S09_SH03_KF_v01.png` | Pass: W2, open grille, reaching |
| S09_SH04_CLIP | `da896a94-5e7b-4836-b3a7-e8bf8bee505b` | `clips/E001_S09_SH04_CLIP_v01.mp4` | Pass: glow pulses |
| S09_SH05_CLIP | `5d0c3caf-3aee-46fa-98f3-f55f36a88ade` | `clips/E001_S09_SH05_CLIP_v01.mp4` | Pass: fear builds; hand leaves frame on the push |
| A21 | `2849217b-5dd7-4a4e-90e1-421ed98ad339` | `audio/dialogue/E001_VO_narr_L021_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A22 | `4e5dadc4-7d04-4b73-bf14-13e677bf1c79` | `audio/dialogue/E001_VO_theo_L022_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A23 | `fe2fbf43-0756-43c8-8820-cca3a91d59f3` | `audio/dialogue/E001_VO_narr_L023_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A24 | `30625146-1e33-4b97-b3f7-664645496d96` | `audio/dialogue/E001_VO_wren_L024_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A25 | `e3a65dab-2b89-44c0-a227-6b8c128826c3` | `audio/dialogue/E001_VO_ida_L025_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A26 | `1816de18-1886-42c9-9d1f-1b0767e8be03` | `audio/dialogue/E001_VO_wren_L026_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A27 | `5c7a079e-e112-4d57-bc6d-60aac3b0a935` | `audio/dialogue/E001_VO_ida_L027_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A28 | `116c2c36-ef86-4870-ba65-b658caf34253` | `audio/dialogue/E001_VO_wren_L028_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A29 | `b52e80ab-6467-49bb-8363-76d05de4bf33` | `audio/dialogue/E001_VO_ida_L029_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A30 | `8eb2ddb2-e4f6-4d81-bcba-0c9c70db55f7` | `audio/dialogue/E001_VO_wren_L030_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A31 | `10e7e548-25c7-4a0d-b81e-d5e0277e0132` | `audio/dialogue/E001_VO_narr_L031_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A32 | `8155bf70-ceda-466c-a7d4-9a70bc845699` | `audio/dialogue/E001_VO_narr_L032_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| A33 | `e6b104f4-ba36-4cda-9565-474067c164f2` | `audio/dialogue/E001_VO_narr_L033_v01.wav` | Generated; duration and speech span measured (`tools/vospan.json`). Not listened to: owner audition required |
| SFX_train_arrive | `4b58e28c-b967-4e12-b6bd-7fa7c0da177a` | `audio/sfx/E001_SFX_train_arrive_v01.wav` | Generated; level envelope checked (approach builds −30 → −19 dB) |
| SFX_train_depart | `7e46475c-45d2-4281-bb67-7b4447e01ac0` | `audio/sfx/E001_SFX_train_depart_v01.wav` | Generated; level envelope checked (approach builds −30 → −19 dB) |

## Balance checkpoints (continued)

| When | Balance | Spent this run |
|---|---|---|
| After batches 1–9 (images), 7 clips, music, 20 voice jobs | 32.02 | 65.78 |
| **Final** (all assets generated) | **14.22** | **83.58** (images 22.0 · clips 31.0 · voice 18.4 · music 7.68 · SFX 4.5) |

## Lessons (Episode 1)

1. Medium quality (0.5) holds the locked style as well as high for keyframes when the approved references are attached. High was used only for the canon reference and the hands hero shot.
2. **Edit-based continuity is the cheapest control:** the wet Tuesday platform, the abandoned umbrella, the shelf vanish, and both fixes were 0.5-credit edits of existing frames, pixel-faithful outside the change.
3. Wide shots invent extra clock hands. Always state 'exactly two hands' and check every clock face at zoom.
4. A style reference that contains set dressing leaks that dressing (the grille shelves appeared in the hallway). Use a reference without the object, or edit afterwards.
5. grok clips that push in will 'improve' small props (the 5 cm whistle grew into a recorder). For prop-critical shots, prompt 'camera holds still' and trim.
6. seed_audio bills per job in 0.1 steps: about 0.039 per word overall. Short single-line jobs cost relatively more.
7. Slowed clips need motion interpolation (minterpolate) or they stutter. It is single-threaded, so render segments in parallel.
