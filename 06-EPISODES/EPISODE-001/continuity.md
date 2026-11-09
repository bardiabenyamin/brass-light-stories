# Continuity — EPISODE-001

Status: **checklists ready (§A generic, §A2 characters, §A3 locations, props, and style). Character, prop, location, and timeline canon filled (Prompts 02–03, 2026-11-09). Scene-level tables PENDING (Prompt 04)**

---

## A. Inspection checklist: run on every generated image and clip

Record a pass or fail per asset in `assets.md` (column "QC"). Two failed retries means stop and ask before spending more.

**Identity**
- [ ] Face shape, eye color and shape, and hair match the approved reference
- [ ] Body proportions and relative heights match
- [ ] Outfit, colors, and accessories match the scene's wardrobe state
- [ ] No duplicate or extra characters

**Anatomy and artifacts**
- [ ] Correct number of limbs and fingers; hands are readable
- [ ] No morphing, melting, flicker, or jitter (clips)
- [ ] No stray text, letters, watermarks, or logos
- [ ] No unwanted camera shake (clips)

**Scene continuity**
- [ ] Props are present and in the same hand or position as in the prior shot
- [ ] Time of day, lighting direction, and weather match the scene
- [ ] Screen direction is preserved (left/right of frame; 180° rule)
- [ ] Emotional state matches the script beat
- [ ] Location layout matches the location reference

**Style**
- [ ] Matches the master style (rendering, palette, lighting, depth of field)
- [ ] Nothing resembles a known franchise character or studio look

**Story**
- [ ] The shot reads clearly with no explanation
- [ ] Cliffhanger shot: the reveal is framed clearly and ends on the exact suspense beat in `cliffhanger-plan.md`

## A2. Character identity locks: check every image and clip that shows a character

Pass only if **every** lock for each visible character holds. Record `QC: pass` or `QC: fail (lock #)` in `assets.md`.
Source: `characters.md` "Never changes".

| Ref | Locks (all must match) |
|---|---|
| `wren` | 1 near-black **blunt chin-length bob with straight bangs** (no ponytail) · 2 **grey-green** eyes · 3 freckles across the nose bridge · 4 warm light-brown skin · 5 **burnt-orange boxy corduroy jacket** · 6 brass pipe-whistle on its chain (long chain until Ep2 6:16 pm; **short, knotted chain** after that) · 7 shortest character in frame · 8 no yellow, no glasses |
| `ida` | 1 **silver hair in a low bun** (day) or one braid over her right shoulder (night) · 2 grey-green eyes · 3 faded freckles · 4 **bottle-green apron** in day scenes · 5 **brass key on a dark red cord** worn whenever she is up (asleep, it hangs on the bedside hook; given to Wren in Ep6) · 6 no glasses · 7 upright posture |
| `theo` | 1 **copper-red curls** · 2 **round gold-wire glasses** · 3 **faded-indigo chore coat** · 4 watch chain at the left breast pocket · 5 **no freckles** · 6 the tallest teen · 7 watch uncracked (except the Ep3 early copy) |
| `crane` | 1 **white streak at the front hairline on HIS LEFT** (right of the image in a front view) · 2 pale grey eyes · 3 **long charcoal overcoat** · 4 **black gloves on** · 5 clean-shaven · 6 no glasses or hat · 7 the tallest person in frame |
| `abe` | 1 **charcoal tweed flat cap** · 2 short white beard · 3 navy jacket with brass buttons and **no insignia or text** · 4 pale grey eyes · 5 stooped · 6 the red lantern nearby when seated |
| `ledger` | 1 grey tabby · 2 **white bib and white front paws only** · 3 **notch in the LEFT ear** · 4 green eyes · 5 no collar |
| `keeperphoto` | 1 sepia · 2 young Ida center-left, teen Ansel center-right with his **streak on his left**, the girl at the far right half out of frame · 3 the **snowflake mitten** visible · 4 a clock with no numerals · 5 no text or date |
| `passenger` | 1 seen from behind or at a distance only · 2 camel coat with a dark low ponytail · 3 the **mustard-yellow umbrella** with its bird charm |

**Cross-character checks:** relative heights (Crane 188 > Theo 176 > Abe 168 > Ida 160 > Wren 152) · family resemblance
visible but subtle (Halloway: grey-green eyes, straight brows, freckles; Crane: pale grey eyes, long straight nose) ·
reserved colors respected (yellow only on the umbrella; red only on memory and love props; glows only on story
objects).

## A3. Location, prop, and style checks: run on every keyframe and clip

| Area | Pass only if |
|---|---|
| Style | Matches `03-ART-DIRECTION/visual-style.md`: stylized 3D with painterly texture; no outlines or cel shading; not photoreal; no text, numerals, or logos anywhere |
| Lighting | Exactly one lighting state, matching the scene's time (§C timeline). The key comes from that location's fixed direction (`locations.md`). Faces readable. The clock face is lit only at DUSK or MIDNIGHT |
| Platform | Tunnel at the **left** in the station-front master. Clock above the office window, empty lantern hook beside it. Bench under the lamp post right of the window. Single track. Clock set state correct (CLOCK_ON / CLOCK_OFF) |
| Office | Early Shelf at the bottom of the back wall, behind the brass diamond-lattice grille, on green baize. **Empty unless an arrival is scripted.** Desk and green lamp by the window. Stair set state correct (STAIR_INTACT / STAIR_BROKEN / LADDER) |
| Clock room | The back of the opal face as a disc; the movement, pendulum, and drawer below; the hatch in the floor |
| Kitchen | Valley window on the far wall; the interior window (to the clock room) on the left wall |
| Props | Match `03-ART-DIRECTION/props.md` exactly (no numerals on dials; whistle has 3 holes; key bow is a flower). Reserved colors respected |

## B. Series continuity rules

- Approved EPISODE-001 references are the series canon; later episodes reuse them by path.
- Injuries, damaged props, wardrobe changes, and relationship changes carry forward to the next episode unless
  explicitly resolved on screen.
- Any contradiction of approved canon is flagged here and in PLAN.md. It is never silently fixed.

## C. Canon tables (filled in Prompts 02–04)

### Wardrobe states by episode (characters; Prompt 02)
| Char | State | Description | Used in |
|---|---|---|---|
| wren | W1 day | Burnt-orange jacket · striped cream tee · navy cargo trousers · off-white high-tops | All day scenes, Ep1–6 |
| wren | W2 night | Same jacket over a charcoal sleep shirt · bare shins · unlaced sneakers · tousled hair | Ep1 midnights, Ep2 opening, Ep3 midnight, Ep4 clock room (night), Ep5 midnight, Ep6 final beat |
| ida | I1 day | White blouse · oatmeal cardigan · bottle-green apron · charcoal skirt · brown boots · key on its cord | All day scenes |
| ida | I2 night | Bottle-green dressing gown over a white nightdress · slippers · silver braid · key on its cord **if she is up**; while she sleeps it hangs on her bedside hook (roadmap Ep4) | Ep2 opening, Ep5 midnight (and any night scene where she has been in bed) |
| theo | T1 | Indigo chore coat · grey tee · tobacco trousers · brown boots · watch chain | All |
| crane | C1 | Charcoal overcoat · slate roll-neck · grey scarf · black gloves · cognac case | All |
| abe | A1 | Navy rail jacket · grey vest · flat cap · red lantern | All |

Scene-by-scene wardrobe is assigned in Prompt 04 from these states. No new outfits without updating `characters.md`.

### Character-held props: state changes (canon)
| Prop | Holder | State changes |
|---|---|---|
| Brass pipe-whistle (`whistle`) | Wren | Ep1 long chain → Ep1 midnight: early copy appears (two exist) → Ep2: early copy confiscated by Ida → 6:16 the chain snaps, the whistle is lost, the early copy vanishes → recovered from Crane, **re-knotted short chain** for the rest of the series |
| Brass key (`idakey`) on a dark red cord | Ida | Worn whenever she is up; on the bedside hook while she sleeps. Taken from that hook by Wren (Ep4 night); back with Ida by Ep5 (Prompt 04 stages how); **given to Wren in Ep6**, then on Wren's neck |
| Pocket watch (`watch`) | Theo | Ep3: early copy with a **cracked crystal** → merges in Theo's hand → **uncracked** for good |
| Cognac leather case | Crane | Always with him outdoors |
| Red signal lantern (`lantern`) | Abe | At his feet on the bench; **raised** with Ansel in Ep6 |
| Red tin toy train (memory-object) | Drawer → Crane → Wren → Crane | Ep4: taken by Crane · Ep6 opening: dissolves into light when Wren gives it back |

### Left and right facts (subject's own side)
| Fact | Side |
|---|---|
| Crane's white streak | His **left** (right of the image in a front view) |
| Ledger's ear notch | **Left** ear |
| Ida's night braid | Over her **right** shoulder |
| Theo's watch pocket | **Left** breast pocket |

### Props (designs locked in `03-ART-DIRECTION/props.md`)
| Prop ID | Description | First appears | Who holds it / where | State changes |
|---|---|---|---|---|
| `umbrella` | Mustard-yellow umbrella, mended tear, brass sparrow charm | Ep1 (Mon midnight, on the shelf) | Passenger → bench (lost Tue 6:14) → handed in by Theo | Early copy vanishes at the moment of loss (R2) |
| `whistle`, `idakey`, `watch`, `lantern`, `case` | See "Character-held props" above | | | |
| `ledger` (+ `redthread`) | Green ledger; red-threaded rows (K1) | Ep1 | Office desk | A new red thread for each of Ida's secret returns (one dated Mon night, Ep1) |
| `notebook` | Theo's tally log | Ep1 (mentioned), Ep3 (shown) | Theo | 31 tallies → 32 after the Ep3 return |
| `clock` | Platform clock | Ep1 | Facade / clock room | Jumps +1 minute per early return (R6) · crated in Ep5 · rehung in Ep6 |
| `earlyshelf` | Bottom compartment behind the brass grille | Ep1 | Office back wall | Empty except for arrivals |
| `drawer`, `memset` | Keeper's Drawer and memory-objects | Ep4 | Inside the clock | Items dissolve on return (music box Ep4; train, mitten, larkspur, paper lantern Ep6) |
| `crate`, `trolley` | Clock crate on the baggage trolley | Ep5 | Mid-platform | Hatch opened Ep6; crate unloaded and the clock rehung in Ep6 |
| `carkeys` | Nora's keys, larkspur charm | Ep6 final beat | Early Shelf | Arrival (Season 2 hook) |
| `railcar` | The 6:14 | Ep1 | Track | Arrives from the tunnel 6:14, departs into it 6:20 |

### Time, weather, lighting: season timeline (Prompt 03; lighting states from `visual-style.md` §6)
| Ep | Day / time | Location | Lighting state | Weather |
|---|---|---|---|---|
| 1 | Mon 6:14 (Wren arrives) | Platform | GOLD | Clear |
| 1 | Mon evening (dinner, "Nora") | Kitchen | LAMP | Clear |
| 1 | Mon midnight (umbrella arrives) | Office | MIDNIGHT | Clear, moon |
| 1 | Tue 6:14 (umbrella lost) | Platform | GOLD | **Clearing after an afternoon shower; damp platform** (why she carried an umbrella) |
| 1 | Tue evening (confrontation) | Office | LAMP | — |
| 1 | Tue midnight (whistle arrives) | Office | MIDNIGHT | Clear |
| 2 | Wed 00:01 (opening) | Office | MIDNIGHT | Clear |
| 2 | Wed day (guarding the whistle) | Platform, office | DAY | Clear |
| 2 | Wed 6:14–6:16 (Crane; whistle lost) | Platform | GOLD | Clear |
| 2 | Wed night (photo) | Office | LAMP | — |
| 3 | Thu breakfast | Kitchen | DAY (morning) | Clear |
| 3 | Thu day (Theo's log) | Platform | DAY | Hot |
| 3 | Thu midnight (cracked watch) | Office | MIDNIGHT | Warm night |
| 3 | Fri dawn (the return) | Platform | DAWN | Valley mist |
| 3 | Fri afternoon (the collapse) | Office | DAY + STAIR_BROKEN | **Hot and hazy; dust in the sunbeams** |
| 3 | Fri evening (the song is lost) | Platform | DUSK | Clear |
| 4 | Fri evening (confession) | Kitchen | LAMP | — |
| 4 | Sat day (Crane's hint) | Platform | DAY | Clear |
| 4 | Sat night (the drawer) | Clock room (via LADDER) | MIDNIGHT + DRAWER_OPEN | — |
| 5 | Sat night, continued | Clock room | MIDNIGHT + DRAWER_OPEN | — |
| 5 | The following week (clock removed) | Platform | OVERCAST + CLOCK_OFF | **Overcast, damp** |
| 5 | That week, 6:14 (Abe's story) | Platform | OVERCAST + CLOCK_OFF | Overcast |
| 5 | Evening (Ida's guilt) | Kitchen | LAMP | — |
| 5 | Sat midnight (the offer) | Platform | MIDNIGHT + CLOCK_OFF (the crate chimes) | Clear, cold, stars |
| 6 | Sun 00:00, continued | Platform | MIDNIGHT + CLOCK_OFF | Clear |
| 6 | Sun day (the last day) | Platform | DAY + CLOCK_OFF | Clear |
| 6 | Sun 6:10–6:20 (the last train) | Platform | GOLD + CLOCK_OFF | Clear |
| 6 | Sun evening (clock rehung) | Platform | DUSK + CLOCK_ON | Clear |
| 6 | Sun midnight (car keys) | Office | MIDNIGHT + LADDER | Clear |

### Screen direction (masters in `03-ART-DIRECTION/locations.md`)
| Location / master | Fixed facts |
|---|---|
| Platform, station-front master | Tunnel at the **image left** (west). The 6:14 **arrives left → right** and **departs right → left**. Abe looks left toward the tunnel |
| Platform, track master (reverse) | Tunnel at the **image right**; valley and village behind the track |
| Office, doorway master (looking east) | Early Shelf along the **left** wall (low); window and desk on the **right**; stair in the far left corner |
| Office, shelf master (looking west) | The hall door faces camera; the shelf's arrival glow comes from **low image right** onto faces in the doorway |
| Clock room, hatch master (looking south) | The face disc dead ahead; the drawer below the pendulum; the hatch in the foreground |
| Kitchen, door master (looking south) | Valley window far wall; **interior window on the left** |
| Two-shots (default) | Wren screen-left looking up and right; the adult screen-right. Hold the 180° line within a scene |

### Emotional state by scene
| Scene | Char ID | Enters as | Exits as |
|---|---|---|---|
| — | — | — | — |

### Carried into Episode 2
| Item | State at end of E001 |
|---|---|
| — | — |
