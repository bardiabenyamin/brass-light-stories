# Locations — *The Early Shelf*, Season 1

Status: **LOCKED v1 — Prompt 03, 2026-11-09.** No location images exist yet. The reference prompts are in
`../06-EPISODES/EPISODE-001/prompts.md` § "Location reference batch" (LR-xx), built from the blocks below. Lighting
states and style come from `visual-style.md`.

Canon sources: `02-SERIES/series-bible.md` §2 (the four locations, the tunnel at the platform's end, the clock on an
iron bracket, the clock room above the office, the kitchen window onto the clock's back). Nothing here contradicts
them; this file adds the detail.

---

## 0. Station geography (canon; never contradict)

```
                         N  (mountainside behind the station)
          ┌─────────────────────── STATION BUILDING (2 floors) ───────────────────────┐
          │ UPPER:  [ Ida's flat: KITCHEN ]  ▣ interior window ▣  [ CLOCK ROOM ]        │
          │ GROUND: [ station hall ] ── door ── [ LOST-AND-FOUND OFFICE ] (stair, NE)   │
          └──────────────────────────────────────────────── ◯ platform CLOCK on facade ┘
  W  TUNNEL ▓▓▶  ════════ PLATFORM (stone) ════  bench + lamp post  ════════════════ buffers   E
  (mountain)     ──────── single track ────────────────────────────────────────────────
                         S  (valley, village of slate roofs below)
```

- The platform runs **east–west** along the station's south front. The **tunnel mouth is at the west end**; the line
  ends at buffers at the east end.
- **The 6:14 arrives out of the tunnel and leaves back into it.**
- **The platform clock** is set into the south facade above the office window, in an ornate black wrought-iron ring
  bracket. It has a translucent opal-glass face and a movement directly behind it in the clock room. An empty iron
  lantern hook hangs beside it.
- **The office** (ground floor) has its hall door on the **west** wall, the Early Shelf on the **north** (back) wall,
  a tall window on the **south** wall onto the platform, the desk in the **south-east** corner, and the narrow stair
  in the **north-east** corner up to the clock room.
- **Upper floor:** Ida's flat (kitchen) to the west and the clock room to the east, joined only by a small
  **interior window** in the kitchen's east wall. The clock room is reached only by the office stair (a ladder from
  Ep4 on).

## 1. LOC_PLATFORM — the platform

**Master camera:** "station-front master". Across the track, eye level, 35 mm, looking **north** at the station
front. **The tunnel is at the image left** (west); the buffers and the village side are at the image right.

**Screen direction:**
- In the master, the 6:14 **arrives moving left → right** and **departs right → left** into the tunnel.
- Abe, on the bench, looks **left** (toward the tunnel) when he waits.
- In the reverse "track master" (from the bench, looking south over the valley), everything flips: the tunnel is at
  the image right.

**Fixed features:**
- A two-story station of grey granite blocks with cream-painted timber trim and a steep blue-grey slate roof.
- The round celadon-faced clock in its iron ring above the office window, with the empty lantern hook beside it.
- A long slatted bench with cast-iron legs under a cast-iron lamp post, just right of the office window.
- A blank name board seen edge-on.
- The arched granite tunnel mouth at the far left, in a pine-covered slope.
- Mountain ridges behind.

**Key light by state:** GOLD comes from the image left (the tunnel end, low). DAY comes from behind the camera
(south). MIDNIGHT moonlight is high from the image right (south-east), with the lamp post and the glowing clock face as
practicals.

| Set state | Episodes | Description |
|---|---|---|
| `CLOCK_ON` | Ep1 → Ep5 mid; Ep6 end | The clock in place |
| `CLOCK_OFF` | Ep5 (after removal) → Ep6 until rehung | The iron ring is empty, with a round pale patch of unweathered stone inside it. The pine crate sits on the baggage trolley mid-platform |
| `TRAIN_IN` | 6:14 to 6:20 scenes | The railcar (`props.md` `railcar`) stands at the platform |

```location platform
Larkspur Junction, a small two-story mountain railway station built of grey granite blocks with cream-painted timber trim and a steep blue-grey slate roof, seen from across a single railway track: a long worn stone platform runs along the station front, a large round station clock with a pale celadon-green enamel face, plain black baton markers, no numerals and two plain black hands sits in an ornate black wrought-iron ring bracket on the facade above a tall office window, beside it an empty black iron lantern hook, a long weathered wooden slatted bench with black cast-iron legs under a black cast-iron lamp post just right of the window, a blank wooden name board seen edge-on, at the far left end of the platform the dark arched granite mouth of a railway tunnel where the track disappears into a steep pine-covered mountainside, layered blue mountain ridges behind, no lettering anywhere
```

```locstate platform GOLD
the sun low behind the ridge above the tunnel at the far left, warm light raking along the platform from the left, long shadows stretching to the right, the clock face and the lamp post unlit
```

```locstate platform DAY
bright clear day, the clock face and lamp post unlit, short crisp shadows of the bench and lamp post falling toward the station wall
```

```locstate platform OVERCAST
low grey cloud on the ridges, the platform damp with a few shallow puddles, the lamp post dimly lit
```

```locstate platform DAWN
pale sky brightening from the right, mist drifting at the tunnel mouth, the lamp post still faintly lit, the clock face softly lit
```

```locstate platform DUSK
deep blue sky with a last warm glow along the ridge above the tunnel, the lamp post lit and casting a warm pool on the bench, the clock face glowing softly from within, a warm glow in the office window
```

```locstate platform MIDNIGHT
night sky with stars above the dark ridge, moonlight from the upper right, the clock face glowing softly from within like a pale moon, the lamp post casting a warm pool of light on the empty bench, the office window dark, the tunnel mouth a deep black arch
```

```locset platform CLOCK_OFF
the ornate iron ring bracket on the facade is empty, showing a round pale patch of unweathered stone where the clock used to be, and a large pale pine crate with black iron corner straps stands on a flat wooden baggage trolley in the middle of the platform
```

```locneg platform
clock missing, numerals on the clock, second clock, signs with text, modern train, overhead electric wires, double track, people on the platform
```

---

## 2. LOC_OFFICE — the lost-and-found office

**Master camera:** "doorway master". From the hall door on the west wall, eye level, 35 mm, looking **east**. The
back-wall shelves and the **Early Shelf** run along the **image left** (north wall). The tall window is at the
**image right** (south), with the desk and its green lamp in the far right corner. The narrow stair is in the far
left corner.

**Reverse "shelf master":** from in front of the Early Shelf looking **west** toward the hall door. Use it for shots
of a character in the doorway. In this view the shelf's glow comes from **low, image right** onto faces in the
doorway.

**Fixed features:**
- Honey floorboards and cream plaster.
- The counter in the foreground of the master.
- Floor-to-ceiling shelves of forgotten things in muted blues, greens, browns, and greys, grouped by color, with
  blank colored paper tags. **No yellow and no red on the shelves.**
- The **Early Shelf**: the bottom compartment of the back wall behind a brass diamond-lattice grille door with a
  simple latch, lined with faded green baize, empty except for arrivals.
- The **ledger** on the desk and the green-glass-shaded brass desk lamp.
- The tall window onto the platform.
- The **stair** up to a square ceiling hatch.

**Key light by state:**
- DAY: sun through the window from the image right.
- LAMP: the desk lamp, far right.
- MIDNIGHT: a cool moon shaft through the window from the image right, with the desk lamp off. During an arrival
  the amber glow comes from the Early Shelf, low on the image left in the master.

| Set state | Episodes | Description |
|---|---|---|
| `STAIR_INTACT` | Ep1 → Ep3 (until the collapse) | The narrow steep stair to the hatch |
| `STAIR_BROKEN` | Ep3 (Friday afternoon) | Broken treads and splintered stringers in a heap, with dust hanging in the air |
| `LADDER` | Ep4 → Ep6 | A plain wooden ladder propped up to the open hatch; the broken stair cleared away |

```location office
the lost-and-found office inside a small mountain railway station, seen from the hall doorway: worn honey-colored floorboards and cream plaster walls, a long worn wooden counter in the foreground, floor-to-ceiling worn wooden shelves along the left wall holding neatly arranged forgotten things such as hats, scarves, gloves, books, a violin case, bags and umbrellas in muted blues, greens, browns and greys, grouped by color with small blank colored paper tags, the bottom compartment of that shelf wall closed behind a small brass diamond-lattice grille door with a simple latch, its inside lined with faded green baize and empty, a heavy bottle-green clothbound ledger on a wooden desk with a green-glass-shaded brass desk lamp beside a tall window in the right wall looking out onto the platform, a narrow steep wooden staircase in the far left corner climbing to a square hatch in the ceiling, no lettering anywhere
```

```locstate office DAY
afternoon daylight streaming through the tall window on the right, warm sunlit patches on the floorboards, the desk lamp off
```

```locstate office LAMP
the green-shaded desk lamp lit, a warm pool of light on the desk and ledger, the rest of the room in soft shadow, dark blue dusk in the window
```

```locstate office MIDNIGHT
a cool blue shaft of moonlight falling through the tall window on the right across the floorboards, the desk lamp off, the shelves in deep blue shadow, the brass grille catching a faint glint
```

```locset office STAIR_BROKEN
the narrow staircase in the far left corner has collapsed into a heap of broken treads and splintered wood, fine dust hanging in the air
```

```locset office LADDER
a simple wooden ladder propped in the far left corner where a staircase used to be, reaching up to the open square hatch in the ceiling
```

```locneg office
yellow objects, red objects, items on the bottom shelf, text on tags, labels, computer, telephone, modern office furniture
```

---

## 3. LOC_CLOCKROOM — the clock room

**Master camera:** "hatch master". From beside the square floor hatch (north side), eye level, 35 mm, looking
**south** at the back of the clock face.

**Fixed features:**
- The back of the large round **translucent opal-glass face**, showing the baton markers in reverse and the central
  shaft of the hands.
- The heavy black iron **movement** of brass gears on a wooden stand.
- The long brass **pendulum** in a narrow open wooden case.
- The **Keeper's Drawer**: a small brass drawer with a larkspur-shaped keyhole set into the iron frame beneath the
  pendulum.
- A sloping timber roof, tools on hooks, cobwebs, and the floor hatch in the foreground.
- At night, a **single bare warm bulb** on a bracket behind the movement lights the face from inside. This is the
  "pale moon" seen from the platform.

**Key light by state:** in DAY, milky daylight glows through the face (a soft disc of light, dust motes). At MIDNIGHT
the bare bulb is the practical, the face is a luminous disc, the gears throw long shadows, and the corners are dark.
When the drawer is open, the memory-objects add a pale-gold glow from below.

| Set state | Episodes | Description |
|---|---|---|
| `DRAWER_CLOSED` | Default | — |
| `DRAWER_OPEN` | Ep4 (and Ep5 opening) | The drawer pulled open, lined with dark green velvet; dozens of small objects glowing faintly pale-gold |

```location clockroom
a small cramped clock room under a sloping timber roof, seen from beside a square hatch in the floor: directly ahead the back of a large round translucent opal-glass clock face set into the wall, showing plain baton markers in reverse and the central shaft of the hands, in front of it a heavy black iron clock movement of interlocking brass gears on a sturdy wooden stand, a long brass pendulum hanging in a narrow open wooden case below the movement, a small brass drawer with a single keyhole set into the iron frame beneath the pendulum, dusty floorboards, old tools on wall hooks, cobwebs in the rafters, no lettering anywhere
```

```locstate clockroom DAY
soft milky daylight glowing through the translucent clock face as a luminous disc, dust motes drifting in the light, the rest of the room dim
```

```locstate clockroom MIDNIGHT
a single bare warm bulb on a bracket behind the movement lighting the back of the clock face so it glows as a luminous disc, long shadows of the gears across the rafters, deep darkness in the corners
```

```locset clockroom DRAWER_OPEN
the small brass drawer is pulled open, lined with dark green velvet and holding dozens of small objects that each glow faintly from within with pale-gold light
```

```locneg clockroom
numerals on the clock face, readable dial text, electric wiring clutter, modern equipment, windows other than the clock face
```

---

## 4. LOC_KITCHEN — the station-house kitchen

**Master camera:** "door master". From the kitchen doorway, eye level, 35 mm, looking **south**. The window over the
sink on the far wall looks over the valley. The **interior window** is on the **image left** (east wall), with the
back of the clock face glowing through it at night. The stove is near on the left.

**Fixed features:**
- A worn table with two mismatched chairs at the center.
- A cream enamel stove.
- Open shelves of mismatched cups and jars with no labels.
- A deep sink under the valley window.
- The small interior window into the clock room.
- A fabric-shaded pendant lamp over the table, and a braided rag rug.

**Key light by state:** in DAY (morning) the sun comes through the far window; a kettle's steam is optional. In LAMP
the pendant pools light over the table, the window shows blue dusk, and the interior window glows pale with the lit
clock face.

```location kitchen
a small homely station-house kitchen upstairs, seen from the doorway: a worn wooden table with two mismatched chairs in the middle, an old cream enamel stove against the left wall, open wooden shelves of mismatched cups and jars without labels, a window over a deep sink in the far wall looking out over a valley of slate roofs and blue mountains, further along the left wall a small interior window looking into a dim neighboring room where the back of a large round clock face shows as a pale disc, a low fabric-shaded pendant lamp over the table, a braided rag rug on worn floorboards, no lettering anywhere
```

```locstate kitchen DAY
morning sunlight through the far window laying warm patches across the table, a thin curl of steam from a kettle on the stove
```

```locstate kitchen LAMP
the pendant lamp lit in a warm pool over the table, dusk blue in the far window, the small interior window glowing pale with the lit clock face beyond
```

```locneg kitchen
labels, text on jars, modern appliances, microwave, refrigerator, television, red objects
```

---

## 5. Location reference plan (PLANNED; the prompts are in `prompts.md`)

| Location | States to reference | Filenames |
|---|---|---|
| Platform | GOLD · DAY · OVERCAST · DAWN · DUSK · MIDNIGHT · OVERCAST + `CLOCK_OFF` | `E001_LOC_platform_<state>_wide_v01.png` |
| Office | DAY · LAMP · MIDNIGHT · DAY + `STAIR_BROKEN` · MIDNIGHT + `LADDER` | `E001_LOC_office_<state>_wide_v01.png` |
| Clock room | DAY · MIDNIGHT · MIDNIGHT + `DRAWER_OPEN` | `E001_LOC_clockroom_<state>_wide_v01.png` |
| Kitchen | DAY · LAMP | `E001_LOC_kitchen_<state>_wide_v01.png` |

Once approved, location references are series canon (the same rule as the characters). Reverse angles are made
in Prompt 06 from the approved masters.
