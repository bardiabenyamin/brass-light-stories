# Visual Style — *The Early Shelf* · Brass Light Stories

Status: **LOCKED v1 — Prompt 03, 2026-11-09** (owner: "Lock the master style prompt, the master negative prompt…").
The proof-of-work (`04-TESTS/POW-001/`) is the first test of this lock. If it fails a check, a v2 is proposed with a
dated note, after backing up v1. Original by design: this style does not imitate any named studio, artist,
franchise, or film, and none is named in any prompt.

Companion files:
- `locations.md`: the four core locations, their layouts, lighting states, and prompts.
- `props.md`: prop designs and prompts.
- `../06-EPISODES/EPISODE-001/characters.md`: the cast.
- `../06-EPISODES/EPISODE-001/continuity.md`: the inspection checklists.

---

## 1. Visual thesis: brass light in a blue hour

Two lights tell this story.
- **Amber** stands for keeping: home, memory, and the shelf's quiet magic.
- **Midnight blue** stands for tomorrow: the unknown, the night, loss.
- **Brass** is the series' material (the clock, key, whistle, grille, buttons, and clasp), and it catches both lights.
  It is also the channel's name.

The world should feel **handcrafted and holdable**: a place of small objects that matter. The camera is a patient
observer that watches through doorways, grilles, and glass, the way a keeper watches.

## 2. Rendering approach

| Aspect | Rule |
|---|---|
| Form | Stylized 3D; softly sculpted, simplified, slightly rounded forms. Detail is concentrated on faces, hands, and clue objects; backgrounds are simpler than foregrounds |
| Surface | Painterly, tactile texture: visible wood grain, brush-like color variation on plaster, weave on wool and corduroy, patina and wear on brass, chips on enamel. Nothing looks like glossy plastic |
| Shading | Soft, physically based light; subsurface skin; **no outlines, no cel shading, no toon ramps** |
| Realism | Stylized, never photorealistic; never flat 2D |
| Atmosphere | Light volumetric haze in beams; gentle bloom on practical lights. **No heavy film grain or chromatic aberration**, because both cause flicker in AI video |

## 3. Proportions

- **Characters:** see `characters.md` §0. Heads and eyes about 10–15% enlarged; realistic five-finger hands; a fixed
  height lineup.
- **Environments:** real-world scale, slightly simplified. Doors and furniture stay at true human scale so characters
  read correctly.
- **Clue props:** about 10% oversized so they read at 1080p.

## 4. Materials

| Material | Where | Look |
|---|---|---|
| Brass | Clock rim, Ida's key, whistle, shelf grille, buttons, case clasp, drawer | Warm and softly brushed; darker in crevices, bright on worn edges |
| Painted wood | Shelves, counter, bench slats, station trim | Worn cream and honey tones, with edges rubbed back to bare wood |
| Enamel | Clock face, stove, mugs | Pale and slightly chipped |
| Stone | Platform, station walls, tunnel mouth | Cool grey granite blocks with moss in the joints |
| Slate | Roof | Blue-grey |
| Iron | Clock ring bracket, lamp post, bench legs, clock movement frame | Black, slightly rusted at the joints |
| Fabric | Wool, corduroy, canvas, denim | Visible weave, soft folds |
| Glass | Office window, desk-lamp shade (green), clock face (translucent opal) | Soft reflections, never mirror-sharp |

## 5. Palette

| Name | Hex | Use |
|---|---|---|
| Midnight blue | `#1B2A44` | Night ambient, shadows |
| Blue-hour violet | `#3E3A5F` | Dusk sky, distant ridges |
| Lamplight amber | `#F2A541` | Practical lights, warm interiors |
| Honey wood | `#A8743F` | Floors, shelves |
| Brass | `#B8893A` | The motif metal |
| Station cream | `#E9DFC9` | Trim, plaster |
| Stone grey | `#8A8580` | Platform, walls |
| Slate | `#4C5866` | Roof |
| Pine green | `#2F4A3A` | Mountainside |
| Clock celadon | `#D6E3CF` | The clock face (glows pale celadon-white at night) |

**Reserved accents (only these uses):**
- Umbrella mustard `#E0B12F`: the Ep1 umbrella only.
- Memory red `#B22222`: Abe's lantern, the toy train, the mitten, Ida's cord `#8E2B2B`, and her thread `#B0302B`.
- Arrival amber glow `#FFB347`: arrivals and returns only.
- Memory pale-gold glow `#F7E2A1`: memory-objects only.

Character color anchors are in `characters.md` §0.

## 6. Lighting

### States (locked)

| State | When | Key light | Ambient / fill | Practicals |
|---|---|---|---|---|
| `GOLD` | The 6:14 arrivals and departures (Ep1, 2, 6) | Low warm sun from the west, down the platform from the tunnel end | Cool blue-violet shade | Lamp post off; clock face unlit |
| `DAY` | Daytime | High soft sun from the south | Sky-blue bounce | Off |
| `OVERCAST` | The Ep5 week | None (flat) | Soft grey sky | Lamp post dim in late afternoon |
| `DAWN` | Ep3 dawn | Pale peach horizon in the east | Cool blue | Lamp post still on |
| `DUSK` | Blue hour (Ep3 end; Ep6 after the train) | Last warm glow on the western ridge | Deep blue sky | Lamp post, office window, and clock face just lit |
| `LAMP` | Interior evenings | Warm tungsten practicals (desk lamp, pendant lamp) | Low, with deep falloff | — |
| `MIDNIGHT` | Every midnight scene | Cool moonlight from high in the south-east | Midnight blue | **One** warm practical: the lamp post, the glowing clock face, or the desk lamp |

### Effect overlays (mostly composited in the edit, not generated)

| Effect | Look |
|---|---|
| `ARRIVAL` | A soft amber glow blooming from an arriving or returned object. **It lights faces from below** (the series' signature) |
| `MEMORY` | A faint, steady pale-gold inner glow on memory-objects. They dissolve into light when returned |

### Rules

- One lighting state per scene. GOLD and MIDNIGHT never mix.
- Faces always get motivated fill and stay readable.
- The clock face is lit from within **only** in DUSK and MIDNIGHT.
- Key directions are fixed per location (`locations.md`). A scene keeps its key direction across all of its shots.

## 7. Contrast

Night scenes have medium-high contrast, with deep but not crushed blacks (shadow detail stays visible). Day scenes
are soft, with medium-low contrast. Highlights never clip on faces.

## 8. Lens feel and depth of field

| Shot | Lens feel (35 mm equivalent) | Depth of field |
|---|---|---|
| Establishing wide | 28–35 mm | Deep; the geography is legible |
| Medium / two-shot | 40–50 mm | Moderate |
| Close-up | 75–85 mm | Shallow; soft background |
| Clue insert | 100 mm macro feel | Very shallow; the object isolated |

Never wider than 24 mm. No fisheye, no tilt-shift miniature look.

## 9. Camera language and framing

- **Observational.** The camera sits at the eye level of the point-of-view character. Wren's point of view is slightly
  low, because the world is bigger than she is.
- **Frames within frames** are the series motif: doorways, the brass grille, the clock bezel, the railcar window, the
  kitchen's interior window.
- **Crane** is framed slightly from below, with a tall empty vertical beside him (Ep2–5). Once he is humanized (Ep6),
  he is framed at eye level.
- **Abe** sits small in frame on the long bench, with negative space toward the tunnel: waiting.
- **Composition:** rule of thirds; generous headroom in wides; 16:9 at 1920×1080. Key moments keep the subject in the
  centre third so a 9:16 Shorts crop still holds it.
- **Inserts:** one clue object per insert, with clear negative space around it.

## 10. Movement

- **Camera:** locked off by default. The allowed moves are a slow push-in (revelation), a slow pull-out (isolation),
  a slow lateral track along the platform, and a slow follow pan. **One move per shot.** No handheld, whip pans,
  aerials, or orbits.
- **Characters:** grounded, weighty, and restrained. One primary action per clip, using the signature gestures from
  `characters.md`. Natural blinks and breathing; gentle secondary motion on hair and coat hems. No exaggerated
  squash-and-stretch, no fast action.
- **Environment:** subtle only: drifting haze, slight lamp flicker, pine tops in the wind, dust motes, the pendulum.
- **Clip length:** 3–8 s.

## 11. Environment detail

- Lived-in, worn, and orderly-cluttered. Detail is densest near the story's objects.
- **No readable text anywhere.** The station-name board is blank or seen edge-on; there are no posters; shelf tags
  are blank colored paper.
- No phones, screens, logos, or modern vehicles on screen in Season 1, apart from the Ep6 car keys (no logos).

## 12. Mood progression (color script)

| Ep | Dominant light | Shift | Emotional temperature |
|---|---|---|---|
| 1 | GOLD arrival, then MIDNIGHT | The warmest opener; the amber glow appears for the first time | Wonder |
| 2 | GOLD; Crane's charcoal coat cuts a vertical through it; LAMP night | Charcoal intrudes | Unease |
| 3 | DAWN, a hot hazy DAY, then cold DUSK | The first harsh light; dust in sunbeams; it ends blue | Dread, then loss |
| 4 | MIDNIGHT clock room; bulb-lit face; pale-gold drawer | Gold sparks in darkness | Discovery |
| 5 | OVERCAST days; an empty iron ring on the facade; cold MIDNIGHT | The most desaturated episode | Grief |
| 6 | GOLD climax with the red lantern; DUSK resolution; MIDNIGHT hook | The full warm palette returns, plus red | Catharsis, then a new mystery |

## 13. Continuity rules (details in `continuity.md`)

| Area | Rule |
|---|---|
| Props | Designs follow `props.md`. One hero prop per insert. The Early Shelf holds nothing except that night's arrivals. State changes follow `continuity.md` |
| Wardrobe | States follow `continuity.md`. Night scenes use W2 (Wren) and I2 (Ida) |
| Time and weather | The episode timeline table in `continuity.md` sets them; the lighting state follows the time of day |
| Screen direction | The masters in `locations.md`. **The tunnel is west.** Trains arrive from the tunnel and leave back into it |
| Lighting | One state per scene, with the key direction fixed per location and state |
| Text | Never generated. Anything unavoidable is a Remotion overlay |

---

## 14. Master prompts (locked v1)

Prompt composition by asset type. Prompts are assembled by the build script; the blocks below are the single source.

| Asset | Prompt | Negative |
|---|---|---|
| Character reference | `STYLE_CORE + REF_PRESENTATION + view + character block` | `MASTER + character negative` |
| Location reference | `STYLE_CORE + lighting state + location base + location state + "wide establishing shot from the master camera position, eye level, no people"` | `MASTER + LOCATION + location negative` |
| Prop reference | `STYLE_CORE + PROP_PRESENTATION + prop block` | `MASTER + prop negative` |
| Keyframe (Prompt 06) | `STYLE_CORE + lighting state + location base + shot (framing, lens, action) + character blocks in their wardrobe state` | `MASTER + the relevant negatives` |
| Clip (Prompt 07) | The source keyframe + one motion description | `VIDEO` |

```style core
Original stylized 3D animation, film-quality render with a handcrafted feel: softly sculpted simplified forms, tactile painterly surface textures (brushed brass, worn painted wood, chipped enamel, wool and corduroy weave, weathered stone), appealing stylized proportions with slightly enlarged heads and eyes and realistic five-finger hands, soft subsurface skin, soft physically based lighting with gentle haze and bloom on light sources, rich but restrained color, natural lens perspective with soft depth of field, quiet cinematic atmosphere
```

```style refpres
character model reference image, single subject centered, plain seamless mid-grey background, even soft studio lighting with a gentle rim light, no environment, no props unless described
```

```style proppres
prop reference image, single object centered, plain seamless mid-grey background, even soft studio lighting with a gentle rim light, three-quarter view from slightly above, the whole object visible
```

```light GOLD
late-August golden hour, low warm sun raking across the scene, long soft shadows, honey-gold light on stone and brass, cool blue-violet shade, fine dust glowing in the air
```

```light DAY
clear late-summer day, soft high sunlight, crisp cool shadows, clean mountain air, gentle sky-blue bounce light
```

```light OVERCAST
flat overcast grey sky, soft shadowless light, muted desaturated colors, damp air, wet-looking stone
```

```light DAWN
early dawn, pale peach sky low on the horizon, cool blue shadows, thin mist lying in the valley, complete stillness, lamps still glowing faintly
```

```light DUSK
blue-hour dusk, deep blue sky with a last thin warm glow along the mountain ridge, lamps just switched on, cool shadows with warm pools of lamplight
```

```light LAMP
evening interior lit only by warm amber tungsten lamps, soft pools of light with deep gentle falloff into shadow, intimate and cozy
```

```light MIDNIGHT
midnight, cool moonlit midnight-blue ambient light, deep soft shadows with visible detail, a single warm amber practical light for contrast, faint haze
```

```fx ARRIVAL
a soft warm amber glow blooming around the object as if it is quietly arriving, the glow lighting nearby faces and surfaces from below, no sparkles, no beams, no lightning
```

```fx MEMORY
the small object glows faintly from within with a calm steady pale-gold light
```

```negative master
extra limbs, extra fingers, fused fingers, missing fingers, malformed hands, distorted anatomy, asymmetrical eyes, crossed eyes, face drift, identity change, inconsistent outfit, inconsistent props, duplicate characters, extra people, morphing, melting, warped geometry, bent straight lines, text, letters, words, numerals, captions, subtitles, signage, watermark, signature, logo, brand names, UI elements, photorealistic, live action, anime, cel shading, toon outlines, flat 2D, vector art, chibi, plastic toy look, video game render, low-poly, harsh HDR, oversaturated neon colors, fisheye distortion, tilt-shift, heavy film grain, chromatic aberration, low resolution, blurry, jpeg artifacts
```

```negative location
people, figures, silhouettes of people, animals, text, signs, lettering, posters, numerals on the clock face, logos, modern cars, phones, screens, power lines, yellow objects, red objects
```

```negative video
flicker, jitter, strobing, morphing, melting, warping, face drift, identity change, sudden camera shake, fast camera movement, sudden cuts, extra people appearing, objects appearing or disappearing, limbs passing through objects, text appearing, looping motion
```

## Change log

| Date | Change |
|---|---|
| 2026-11-09 | v1 locked (Prompt 03) |
