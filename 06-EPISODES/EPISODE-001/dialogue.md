# Dialogue / Voice Script — EPISODE-001

Status: **DONE (generated 2026-11-09).** 33 new voice files + 1 reused from POW-001, all placed in the review render.
**Voices APPROVED by the owner, 2026-11-09** ("Voices are good"): Annie (Wren + narration), Vera (Ida), Archie (Theo).

This is the clean voice-generation script: one line per row with stable IDs, so lines can be regenerated singly
without disturbing the rest.

---

## Voice profiles (Prompt 08)

| Speaker ID | Character | Vocal qualities | Pace | Range | Pronunciation notes | Voice source and commercial rights |
|---|---|---|---|---|---|---|
| NARR | Narrator = adult-ish Wren looking back (V.O.) | Mid-low for her age, dry, unhurried | Slow, with pauses | Narrow | "Larkspur" = LARK-spur | Higgsfield seed_audio preset **Annie** (owner-delegated choice). Commercial rights: **NOT VERIFIED** (owner) |
| WREN | Wren on screen | Same voice as NARR, more present | Natural | Narrow | — | Annie |
| IDA | Ida Halloway (71) | Dry, composed, low | Slow (speech rate -8) | Narrow | "Nora" = NOR-ah | Preset **Vera** (172 Hz median): `PROPOSED — NEEDS APPROVAL` |
| THEO | Theo Marsh (15) | Deadpan | Natural | Narrow | — | Preset **Archie** (137 Hz median): `PROPOSED — NEEDS APPROVAL` |

Rule: original voices only. Do not imitate any real actor or public figure.

## Line format

| Line ID | Scene | Speaker ID | Line | Emotion / delivery | Pauses / emphasis | File | Status |
|---|---|---|---|---|---|---|---|
| E001_L001 | S01 | NARR | _example only_ | calm, curious | [beat] after "door" | `audio/dialogue/E001_VO_NARR_L001_v01.wav` | NOT GENERATED |

Markup: `[beat]` short pause · `[breath]` audible breath · `*word*` emphasis · `→` emotional shift mid-line.

---

## Lines

See "Lines as generated" below (one row per generation job; IDs map to `tools/e001_spec.py` LINES).

## Word count

Narration: — · Dialogue: — · **Total: —** (target about 650–750, never padded)

## Lines as generated (Prompt 08)

Voices (seed_audio presets, 48 kHz): **NARR + WREN = Annie** (owner-delegated pick, POW-001) · **IDA = Vera** (speech rate -8) · **THEO = Archie**.
Ida and Theo voices were chosen by measured pitch (Vera 172 Hz, narrow range; Archie 137 Hz, narrow range): `PROPOSED — NEEDS APPROVAL` (owner should audition).

| Line | Scene | Speaker | Text | File | Speech (s) | In edit at |
|---|---|---|---|---|---|---|
| A00 | S01 | NARR | In Larkspur, things get lost the day before they go missing. | `audio/dialogue/E001_VO_narr_L000_v01.wav` | 6.43 | 0:03.6 |
| A01 | S02 | NARR | The summer my parents needed to sort some things out, they put me on a train to the end of the line.  Larkspur Junction. One station, one clock, and one train a day.  Grandma met me on the platform like she was collecting a parcel. | `audio/dialogue/E001_VO_narr_L001_v01.wav` | 19.54 | 0:20.0 |
| A02 | S02 | IDA | You have your mother's chin. | `audio/dialogue/E001_VO_ida_L002_v01.wav` | 1.33 | 0:40.6 |
| A03 | S02 | NARR | She didn't hug me. Grandma wasn't a hugger.  There was an old man on the bench, feeding a cat that clearly belonged to no one, and a boy checking his pocket watch against the station clock, like one of them was lying. | `audio/dialogue/E001_VO_narr_L003_v01.wav` | 17.76 | 0:43.5 |
| A04 | S03 | IDA | Everything lost in Larkspur ends up here. Sooner or later. | `audio/dialogue/E001_VO_ida_L004_v01.wav` | 7.47 | 1:02.9 |
| A05 | S03 | NARR | Hats. Gloves. A violin case. Every one of them waiting for somebody to remember.  Grandma wrote each one down in a big green ledger. Some of the lines had red thread stitched right through them. | `audio/dialogue/E001_VO_narr_L005_v01.wav` | 16.02 | 1:09.8 |
| A06 | S03 | WREN | What's that for? | `audio/dialogue/E001_VO_wren_L006_v01.wav` | 0.72 | 1:26.6 |
| A07 | S03 | IDA | Mending. | `audio/dialogue/E001_VO_ida_L007_v01.wav` | 1.56 | 1:28.0 |
| A08 | S03 | WREN | And the bottom shelf? | `audio/dialogue/E001_VO_wren_L008_v01.wav` | 0.98 | 1:29.7 |
| A09 | S03 | IDA | Is mine. Don't touch it. | `audio/dialogue/E001_VO_ida_L009_v01.wav` | 3.77 | 1:32.2 |
| A10 | S03 | NARR | Grandma had exactly one rule. Naturally, I broke it the first night. | `audio/dialogue/E001_VO_narr_L010_v01.wav` | 5.65 | 1:36.6 |
| A11 | S04 | IDA | Eat your soup, Nora. | `audio/dialogue/E001_VO_ida_L011_v01.wav` | 3.86 | 1:45.4 |
| A12 | S04 | WREN | It's Wren, Grandma. | `audio/dialogue/E001_VO_wren_L012_v01.wav` | 1.55 | 1:47.8 |
| A13 | S04 | IDA | Wren. I know that. | `audio/dialogue/E001_VO_ida_L013_v01.wav` | 3.78 | 1:50.4 |
| A14 | S04 | NARR | Nora is my mom. Grandma had never mixed us up before. | `audio/dialogue/E001_VO_narr_L014_v01.wav` | 3.68 | 1:53.6 |
| A15 | S05 | NARR | I couldn't sleep, so I did what I always do. I played Mom's song on her whistle. | `audio/dialogue/E001_VO_narr_L015_v01.wav` | 11.40 | 1:59.5 |
| A16 | S05 | NARR | Then the station clock struck twelve, and the light under the office door turned gold. | `audio/dialogue/E001_VO_narr_L016_v01.wav` | 4.71 | 2:20.0 |
| A17 | S05 | NARR | The bottom shelf had been empty when I went to bed.  Now there was an umbrella on it. Yellow. Mended near the tip. A little brass bird on the strap.  I didn't know someone was watching me watch it. | `audio/dialogue/E001_VO_narr_L017_v01.wav` | 18.64 | 2:25.3 |
| A18 | S06 | NARR | It rained all Tuesday afternoon. At six-fourteen the sky cleared, the train came in, and a woman in a camel coat sat down on the bench with a yellow umbrella.  Mended near the tip. A little brass bird on the strap. | `audio/dialogue/E001_VO_narr_L018_v01.wav` | 18.19 | 2:47.0 |
| A19 | S06 | NARR | When the train left, she was on it. The umbrella wasn't.  I ran to the office.  The bottom shelf was empty again. Like it had never been there at all. | `audio/dialogue/E001_VO_narr_L019_v01.wav` | 12.75 | 3:06.0 |
| A20 | S07 | THEO | Someone left this on the bench. | `audio/dialogue/E001_VO_theo_L020_v01.wav` | 1.40 | 3:19.8 |
| A21 | S07 | NARR | Theo. He keeps the station clock running, and apparently he hands in umbrellas. | `audio/dialogue/E001_VO_narr_L021_v01.wav` | 3.59 | 3:24.0 |
| A22 | S07 | THEO | Clock gained a minute again last night. No reason. And don't go up the tower, by the way. The stairs are rotten. | `audio/dialogue/E001_VO_theo_L022_v01.wav` | 7.16 | 3:28.8 |
| A23 | S07 | NARR | Same tear. Same bird. Same umbrella. | `audio/dialogue/E001_VO_narr_L023_v01.wav` | 4.80 | 3:36.7 |
| A24 | S08 | WREN | This was on your shelf last night. Before she lost it. | `audio/dialogue/E001_VO_wren_L024_v01.wav` | 3.32 | 3:44.3 |
| A25 | S08 | IDA | I know. I saw you. | `audio/dialogue/E001_VO_ida_L025_v01.wav` | 1.64 | 3:47.9 |
| A26 | S08 | WREN | What is it? | `audio/dialogue/E001_VO_wren_L026_v01.wav` | 0.56 | 3:50.1 |
| A27 | S08 | IDA | The shelf shows what Larkspur will lose tomorrow. We watch. We write it down. And we never, ever give anything back early. | `audio/dialogue/E001_VO_ida_L027_v01.wav` | 10.37 | 3:51.4 |
| A28 | S08 | WREN | Why not? | `audio/dialogue/E001_VO_wren_L028_v01.wav` | 0.72 | 4:03.0 |
| A29 | S08 | IDA | Promise me, Wren. | `audio/dialogue/E001_VO_ida_L029_v01.wav` | 1.44 | 4:05.6 |
| A30 | S08 | WREN | I promise. | `audio/dialogue/E001_VO_wren_L030_v01.wav` | 0.79 | 4:09.2 |
| A31 | S08 | NARR | I meant it. For about six hours. | `audio/dialogue/E001_VO_narr_L031_v01.wav` | 4.37 | 4:12.4 |
| A32 | S09 | NARR | At midnight, the clock struck twelve, and the shelf turned gold again.  This time I recognized what was on it.  My mom's whistle.  Which was strange, because my mom's whistle was hanging around my neck. | `audio/dialogue/E001_VO_narr_L032_v01.wav` | 20.79 | 4:18.6 |
| A33 | S09 | NARR | Tomorrow, I lose the only thing my mom ever gave me. | `audio/dialogue/E001_VO_narr_L033_v01.wav` | 3.30 | 4:41.2 |

Word count: {'NARR': 370, 'IDA': 59, 'WREN': 28, 'THEO': 28} · **total 485** (below the 650–750 guide by design; see `script.md`).
