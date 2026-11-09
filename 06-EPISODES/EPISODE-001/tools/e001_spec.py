"""EPISODE-001 production spec: the single source for keyframe prompts, clip prompts, and voice lines.
Prompts are composed from the LOCKED blocks in 03-ART-DIRECTION/ and characters.md, so they cannot drift from canon.
Usage:  python3 e001_spec.py images ID [ID ...]   -> JSON requests for generate_image_batch
        python3 e001_spec.py clips ID [ID ...]    -> JSON requests for generate_video_batch
        python3 e001_spec.py lines                -> voice line table (JSON)
        python3 e001_spec.py words                -> word counts
Job IDs of finished generations are stored in jobs.json (shot ID -> job ID) and resolved as references."""
import re, sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
EP = HERE.parent; ROOT = EP.parent.parent; AD = ROOT / "03-ART-DIRECTION"

def blocks(path, kinds):
    t = path.read_text(); out = {}
    for m in re.finditer(r"```(" + "|".join(kinds) + r") ([\w ]+)\n(.*?)```", t, re.S):
        out[(m.group(1), m.group(2).strip())] = m.group(3).strip().replace("\n", " ")
    return out
VS = blocks(AD / "visual-style.md", ["style", "light", "fx", "negative"])
LO = blocks(AD / "locations.md", ["location", "locstate", "locset", "locneg"])
PR = blocks(AD / "props.md", ["prop", "propneg"])
CH = blocks(EP / "characters.md", ["prompt", "negative", "expressions"])
STYLE, REFP = VS[("style", "core")], VS[("style", "refpres")]
NEG, NEGV = VS[("negative", "master")], VS[("negative", "video")]
# Condensed master negative actually sent with Episode 1 keyframes (same intent, rarely-relevant items dropped to keep prompts short)
NEG_SHORT = "extra fingers, malformed hands, distorted anatomy, asymmetrical eyes, face drift, identity change, inconsistent outfit, duplicate characters, extra people, warped geometry, text, letters, words, numerals, captions, signage, watermark, logo, photorealistic, live action, anime, cel shading, toon outlines, flat 2D, plastic toy look, video game render, harsh HDR, oversaturated colors, fisheye, blurry"
GOLD, LAMP, MID = VS[("light", "GOLD")], VS[("light", "LAMP")], VS[("light", "MIDNIGHT")]
ARRIVAL = VS[("fx", "ARRIVAL")]
def C(k): return re.sub(r",[^,]*expression\s*$", "", CH[("prompt", k)])  # character block without its default expression
W1, W2, I1, I2, T1, ABE, CAT, PAS = C("wren"), CH[("prompt", "wren_w2")], C("ida"), CH[("prompt", "ida_i2")], C("theo"), C("abe"), C("ledger"), CH[("prompt", "passenger")]
UMB, WHI, LEDG, RAIL, WATCH, KEY, LANT = (PR[("prop", k)] for k in ["umbrella", "whistle", "ledger", "railcar", "watch", "idakey", "lantern"])
NW, NI, NT = CH[("negative", "wren")], CH[("negative", "ida")], CH[("negative", "theo")]

# Approved canon and reusable POW-001 jobs (see 04-TESTS/POW-001/run-log.md)
KNOWN = {"REF_WREN": "21ea2f37-44ef-47ea-82f8-616daf026597", "REF_IDA": "54574eff-0450-4488-9b09-d32079670dce",
         "REF_PLATFORM_MID": "9af21ca8-ada6-4cb5-aa85-dfd96f658e71", "POW_SH01": "78ae169f-f9f4-42a5-b810-d7c41661a53f",
         "POW_SH02": "b4b50218-8680-49cc-ae6e-196bfdb5c3d1", "POW_SH03": "f03ea6b7-3309-4102-a4f3-d1ca402c404d",
         "POW_SH04": "cc5480ba-7493-4206-9205-216dabcefbc9", "POW_SH05": "2f2aed20-d275-4d95-8bdf-86fe4dafcd28",
         "POW_SH06": "4bc8dda6-b7be-4c3f-b7f1-60b948b9e456", "POW_SH07": "f25f3ad3-9f40-4010-879c-ffbd9680be15"}
JOBS = HERE / "jobs.json"
def job(k):
    j = json.loads(JOBS.read_text()) if JOBS.exists() else {}
    j = {**KNOWN, **j}
    if k not in j: raise SystemExit(f"reference {k} has no job yet")
    return j[k]

STYLE_ONLY = "use it only for the rendering style, proportions and level of stylization, not for identity"
def kf(light, shot, chars="", refs_note="", neg_extra="", lightdir=""):
    parts = [STYLE, light] + ([lightdir] if lightdir else []) + [shot] + ([chars] if chars else []) + ([refs_note] if refs_note else [])
    return ". ".join(p.rstrip(". ") for p in parts) + f". Avoid: {NEG_SHORT}" + (f", {neg_extra}" if neg_extra else "") + "."

NO_YELLOW = "yellow objects, mustard objects"
NO_RED = "red objects other than those described"
NO_CLOCK = "station clock, clock face"

# ---------------------------------------------------------------- keyframes
# id: (quality, aspect, [ref keys], prompt)
IMG = {}
IMG["REF_THEO"] = ("high", "4:5", ["REF_WREN"], f"{STYLE}. {REFP}. waist-up portrait facing the camera straight on, arms relaxed at the sides. {CH[('prompt','theo')]}. The reference image is Wren from the same film: {STYLE_ONLY}. Avoid: {NEG}, {NT}.")

# S02 platform, Monday 6:14, GOLD
IMG["S02_SH01"] = ("medium", "16:9", ["REF_PLATFORM_MID"], kf(GOLD,
    "Wide shot of the same mountain railway station as the reference image, now at golden hour, framed on the far left end of the platform: the dark arched granite tunnel mouth in the steep pine-covered mountainside, the single track curving out of it along the long worn stone platform; the 6:14 train, " + RAIL + ", has just emerged from the tunnel and is gliding toward the right along the platform, its headlamps glowing; the grey granite corner of the station building with cream timber trim at the right edge of frame; the station clock is outside the frame; layered blue mountain ridges; no people",
    refs_note="The reference image shows this station at midnight: keep the architecture, tunnel, platform and track layout, but the time is now golden hour", neg_extra=f"{NO_CLOCK}, people, {NO_YELLOW}, double track, overhead wires, text on the train",
    lightdir="the sun low behind the ridge above the tunnel, warm light raking from the left, long shadows stretching to the right"))
IMG["S02_SH02"] = ("medium", "16:9", ["REF_WREN", "S02_SH01"], kf(GOLD,
    "Medium-wide shot, camera at chest height: Wren stands alone on the worn stone platform in front of the open door of the stopped two-car railcar, a worn navy canvas duffel bag in her right hand, looking up and to the right with a guarded, curious expression, the slate-teal and cream railcar filling the background",
    chars=W1, refs_note="Reference image 1 is Wren: match her face, hair, skin, outfit and whistle exactly. Reference image 2 shows the railcar: match its design and colors",
    neg_extra=f"{NW}, {NO_CLOCK}, other people, {NO_YELLOW}, text", lightdir="warm low sun from the left, long shadows to the right"))
IMG["S02_SH03"] = ("medium", "16:9", ["REF_PLATFORM_MID", "POW_SH02"], kf(GOLD,
    "Low-angle shot looking up at the station facade: grey granite blocks, cream-painted timber trim and the edge of the slate roof against a clear evening sky; the large round station clock in its ornate black wrought-iron ring bracket above the tall office window, beside it an empty black iron lantern hook; the clock has a pale celadon-green enamel face with plain black baton markers and no numerals; the clock reads 6:14: the short hour hand points down, just past the six o'clock marker, and the long minute hand points right, just above the three o'clock marker",
    refs_note="Reference image 1 shows the station and reference image 2 shows the clock face: keep their designs exactly, but the time of day is golden hour", neg_extra=f"numerals, roman numerals, second hand, people, {NO_YELLOW}",
    lightdir="warm golden sunlight from the left across the facade, the clock face lit by the sun"))
IMG["S02_SH04"] = ("medium", "16:9", ["REF_IDA", "REF_WREN"], kf(GOLD,
    "Medium shot, waist up: Ida stands upright on the stone platform, hands folded in front of her apron, looking toward the left of the frame with a dry, appraising expression, as if collecting a parcel; behind her the grey granite station wall with cream timber trim in soft focus",
    chars=I1, refs_note=f"Reference image 1 is Ida: match her face, hair, skin, outfit and key exactly. Reference image 2 is Wren from the same film: {STYLE_ONLY}",
    neg_extra=f"{NI}, {NO_CLOCK}, other people, {NO_YELLOW}", lightdir="warm low sun from the left, the right side of her face in soft cool shade"))
IMG["S02_SH05"] = ("medium", "16:9", ["REF_WREN"], kf(GOLD,
    "Close-up of Wren's face and shoulders on the platform, her chin lifted slightly, a guarded skeptical look up and to the right, lips closed, the blurred platform and stone wall behind her",
    chars=W1, refs_note="The reference image is Wren: match her face, hair, freckles, skin and outfit exactly", neg_extra=f"{NW}, other people, {NO_YELLOW}",
    lightdir="warm low sun from the left, a soft rim of gold on her hair"))
IMG["S02_SH06"] = ("medium", "16:9", ["REF_WREN", "REF_IDA", "S02_SH01"], kf(GOLD,
    "Medium-wide two-shot on the worn stone platform: Wren on the left of the frame, holding her navy duffel bag, looking up and to the right at Ida; Ida on the right of the frame facing her with her hands folded in front of her apron; an awkward arm's length of empty space between them, neither reaching out; the stopped slate-teal and cream railcar behind them",
    chars=f"Wren: {W1}. Ida: {I1}", refs_note="Reference image 1 is Wren and reference image 2 is Ida: match both exactly. Reference image 3 shows the railcar",
    neg_extra=f"{NW}, {NI}, hugging, touching, other people, {NO_CLOCK}, {NO_YELLOW}", lightdir="warm low sun from the left, long shadows stretching to the right"))
IMG["S02_SH07"] = ("medium", "16:9", ["REF_WREN"], kf(GOLD,
    "Medium shot of a long weathered wooden slatted bench with black cast-iron legs on the stone platform, against the granite station wall: an old railwayman sits on it, holding out a small morsel of food on his open palm to a grey tabby cat sitting beside him on the bench, which eats from his hand; an old red signal hand lantern stands on the stone at his feet",
    chars=f"The man: {ABE}. The cat: {CAT}. The lantern: {LANT}", refs_note=f"The reference image is Wren from the same film: {STYLE_ONLY}",
    neg_extra=f"{NO_CLOCK}, other people, {NO_YELLOW}, collar on the cat", lightdir="warm low sun from the left, long shadows to the right"))
IMG["S02_SH08"] = ("medium", "16:9", ["REF_THEO", "REF_WREN"], kf(GOLD,
    "Medium shot, waist up: Theo stands on the stone platform holding his open silver pocket watch in his left palm, looking up from it toward the upper left of the frame with a skeptical deadpan frown, as if comparing it with a clock out of frame; the granite station wall behind him in soft focus",
    chars=f"{T1}. The watch: {WATCH}", refs_note=f"Reference image 1 is Theo: match his face, hair, glasses and outfit exactly. Reference image 2 is Wren from the same film: {STYLE_ONLY}",
    neg_extra=f"{NT}, {NO_CLOCK}, other people, {NO_YELLOW}, numerals on the watch", lightdir="warm low sun from the left"))

IMG["S02_SH03_FIX"] = ("medium", "16:9", ["S02_SH03"], f"{STYLE}. Edit of the reference image: keep everything exactly the same (the station, the golden light, the wrought-iron bracket, the celadon clock face and its twelve black baton markers) and fix only the clock hands: the clock must have exactly two plain black hands, a short thick hour hand pointing down just past the six o'clock marker, and a long thin minute hand pointing right just above the three o'clock marker. Remove the third hand that points toward ten o'clock, and remove the small number at the top of the clock bracket. Avoid: numerals, third hand, second hand, text, letters, any other change.")

# S03 office, Monday evening, LAMP
OFFICE = LO[("location", "office")]
IMG["S03_SH01"] = ("medium", "16:9", ["REF_IDA", "REF_WREN"], kf(LAMP,
    f"Wide shot from the hall doorway into {OFFICE}, the desk lamp lit, dark blue dusk in the window: Ida walks into the room ahead of Wren, both seen from behind in three-quarter view, Ida on the right gesturing toward the shelves, Wren on the left carrying her navy duffel bag and looking up at the shelves",
    chars=f"Ida: {I1}. Wren: {W1}", refs_note="Reference image 1 is Ida and reference image 2 is Wren: match both exactly",
    neg_extra=f"{NI}, {NW}, {NO_YELLOW}, items on the bottom shelf, text on tags, labels, computer, telephone", lightdir="the green-shaded desk lamp is the only light, warm on the right side of the room"))
IMG["S03_SH02"] = ("medium", "16:9", ["S03_SH01"], kf(LAMP,
    "Close view along the floor-to-ceiling worn honey-colored wooden shelves of the lost-and-found office from the reference image: neatly arranged forgotten things grouped by color, a row of felt hats, folded gloves and scarves, a battered violin case, books and bags in muted blues, greens, browns and greys, each with a small blank colored paper tag on a string; no people",
    refs_note="The reference image shows this room: keep its shelves, materials and lighting", neg_extra=f"people, {NO_YELLOW}, {NO_RED}, text on tags, labels, writing",
    lightdir="warm lamplight from the right, shadows deepening to the left"))
IMG["S03_SH03"] = ("medium", "16:9", ["S03_SH01"], kf(LAMP,
    f"Close-up insert, camera looking down at the desk: {LEDG}, under the warm pool of light from a green-glass-shaded brass desk lamp at the edge of frame; a brass-nibbed dip pen lies beside it; no hands, no people",
    refs_note="The reference image shows this room and its desk", neg_extra="people, hands, legible writing, letters, words, numbers, " + NO_YELLOW,
    lightdir="warm lamplight from the upper right"))
IMG["S03_SH04"] = ("medium", "16:9", ["REF_WREN", "S03_SH01"], kf(LAMP,
    "Medium close-up: Wren leans on the long worn wooden counter of the lost-and-found office, looking down to the right at an open ledger just outside the frame, curious and intent, lips closed; behind her the shelves of forgotten things in soft shadow",
    chars=W1, refs_note="Reference image 1 is Wren: match her exactly. Reference image 2 shows the room", neg_extra=f"{NW}, other people, {NO_YELLOW}",
    lightdir="warm amber lamplight on her face from the right, soft shadow on the left"))
IMG["S03_SH05"] = ("medium", "16:9", ["POW_SH03"], kf(LAMP,
    "Edit of the reference image: keep the camera, the composition, the shelf unit, the brass diamond-lattice grille door with its latch, the faded green baize and the empty compartment exactly the same; change only the lighting and materials: it is now evening and the room is lit by a warm amber desk lamp behind the camera, the lamp itself not visible; the shelves are worn honey-colored wood, the moonlight and the window-bar shadows are gone; the compartment stays completely empty",
    neg_extra=f"objects in the compartment, {NO_YELLOW}, moonlight, blue light, visible lamp, people", lightdir="warm lamplight from behind the camera"))
IMG["S03_SH06"] = ("medium", "16:9", ["REF_IDA"], kf(LAMP,
    f"Close-up insert at chest height: Ida's weathered right hand closing around the small brass key that hangs on its dark red waxed cord over the bib of her bottle-green apron, her oatmeal cardigan sleeve pushed to the elbow; her face is out of frame above, only the edge of her chin visible. The key: {KEY}",
    refs_note="The reference image is Ida: match her hands, skin, clothing and key exactly", neg_extra=f"{NI}, extra fingers, malformed hand, rings, other keys, {NO_YELLOW}",
    lightdir="warm lamplight from the right"))

# S04 kitchen, Monday night, LAMP
KITCHEN = LO[("location", "kitchen")]
IMG["S04_SH01"] = ("medium", "16:9", ["REF_IDA", "REF_WREN"], kf(LAMP,
    f"Wide shot from the doorway into {KITCHEN}, the pendant lamp lit in a warm pool over the table, dusk blue in the far window, the small interior window on the left wall glowing pale with the lit clock face beyond: Ida sits at the right side of the table and Wren at the left side, eating soup from plain bowls, a loaf of bread on a board between them",
    chars=f"Ida: {I1}. Wren: {W1}", refs_note="Reference image 1 is Ida and reference image 2 is Wren: match both exactly",
    neg_extra=f"{NI}, {NW}, labels, text on jars, modern appliances, {NO_YELLOW}, {NO_RED}", lightdir="the pendant lamp is the main light, overhead and warm"))
IMG["S04_SH02"] = ("medium", "16:9", ["REF_IDA", "S04_SH01"], kf(LAMP,
    "Medium shot in profile, facing the left of the frame: Ida at the kitchen table, a spoon in her hand above her bowl of soup, eyes lowered, absent-minded and far away; behind her the kitchen shelves in soft shadow",
    chars=I1, refs_note="Reference image 1 is Ida: match her exactly. Reference image 2 shows the kitchen", neg_extra=f"{NI}, other people, {NO_YELLOW}, {NO_RED}",
    lightdir="warm pendant-lamp light from above"))
IMG["S04_SH03"] = ("medium", "16:9", ["REF_WREN", "S04_SH01"], kf(LAMP,
    "Medium close-up: Wren at the kitchen table, her spoon paused above her bowl of soup, looking across the table toward the right of the frame, quietly hurt, lips closed; the small interior window on the wall behind her glowing pale",
    chars=W1, refs_note="Reference image 1 is Wren: match her exactly. Reference image 2 shows the kitchen", neg_extra=f"{NW}, other people, {NO_YELLOW}, {NO_RED}",
    lightdir="warm pendant-lamp light from above and the right"))

# S05 kitchen and hall, Monday midnight
IMG["S05_SH01"] = ("medium", "16:9", ["REF_WREN", "POW_SH05", "S04_SH01"], kf(MID,
    "Medium shot in the dark station-house kitchen at midnight, the pendant lamp off: Wren stands at the small interior window in the left wall, playing the tiny brass pipe-whistle softly, her fingertips on its three holes, eyes half closed; beyond the glass the large round clock face glows as a pale celadon disc, lighting her face with a soft cool glow; faint blue moonlight from the far window",
    chars=W2, refs_note="Reference image 1 is Wren: match her face exactly. Reference image 2 shows her night clothes. Reference image 3 shows the kitchen",
    neg_extra=f"{NW}, lit lamps, other people, {NO_YELLOW}, {NO_RED}, numerals", lightdir="all lamps unlit; the glow of the clock face from the left is the key light"))
IMG["S05_SH02"] = ("medium", "16:9", ["POW_SH03"], kf(MID,
    "A narrow dark hallway inside the old stone station at midnight: worn honey-colored floorboards, cream plaster walls, at the far end a closed wooden panel door with a thin bright line of warm amber light glowing in the gap under it and spilling across the floorboards; no people",
    refs_note="The reference image is from the same film: use it only for the rendering style and the night lighting", neg_extra=f"people, lit lamps, {NO_YELLOW}, {NO_RED}, text",
    lightdir="all lamps unlit; faint blue moonlight from a small window on the right; the only warm light comes from under the door"))
IMG["S05_SH02_FIX"] = ("medium", "16:9", ["S05_SH02"], f"{STYLE}. {MID}. Edit of the reference image: keep the camera, the hallway, the closed door at the far end with the warm amber light glowing under it, the floorboards, the moonlit window on the right and the lighting exactly the same; change only the left wall: remove all the shelves, the folded clothes, the bags and the brass lattice grille, and replace them with a bare cream plaster wall above dark wooden wainscoting, in moonlit shadow. Avoid: shelves, grille, lattice, objects on the left wall, people, text, lit lamps, any other change.")
IMG["S05_SH03"] = ("medium", "16:9", ["POW_SH04"], kf(MID,
    f"Extreme close-up insert inside the bottom shelf compartment, behind the brass diamond-lattice grille, on faded green baize: the tip of the closed mustard-yellow umbrella with its short mended tear stitched in a small zigzag of dark brown thread near one rib tip, and the small brass sparrow charm hanging from its wrist strap; {ARRIVAL}. The umbrella: {UMB}",
    refs_note="The reference image shows this umbrella on this shelf: match its design and color exactly", neg_extra="text, lettering, maker's mark, logos, other yellow objects, people, hands",
    lightdir="the amber glow from the umbrella itself is the key light; the room around is midnight blue"))

# S06 platform, Tuesday 6:14, GOLD after rain
IMG["S06_SH01"] = ("medium", "16:9", ["S02_SH03_FIX"], kf(GOLD,
    "Edit of the reference image: keep the same camera, the same station building, tunnel, track, bench, lamp post and the clock with its two hands exactly as they are; change only the weather: it is just after a rain shower, the long stone platform is dark and wet with shallow puddles mirroring the golden light, rain drops on the bench and the lamp post, wet slate roof, the sky clearing with breaking grey clouds; no train, no people",
    neg_extra=f"people, train, numerals, third clock hand, {NO_YELLOW}, umbrella", lightdir="the low sun breaking through the clouds above the tunnel at the far left, wet glints"))
IMG["S06_SH02"] = ("medium", "16:9", ["REF_WREN", "S02_SH01"], kf(GOLD,
    "Shot from behind the long wet wooden bench on the stone platform, looking out across the track: a woman sits on the bench seen only from behind, a closed mustard-yellow umbrella lying across her knees with its handle to the right; beyond her the stopped slate-teal and cream railcar on the track, and beyond it the valley with slate roofs and blue mountains; the platform is wet after rain",
    chars=f"The woman: {PAS.replace(', holding a closed mustard-yellow umbrella with a small brass bird charm on its strap, standing posture', ', seated')}. The umbrella: {UMB}", refs_note=f"Reference image 1 is Wren from the same film: {STYLE_ONLY}. Reference image 2 shows the railcar",
    neg_extra="her face, profile, other people, other yellow objects, text", lightdir="the low sun at the far right behind the tunnel end, warm backlight, glints on the wet stone"))
IMG["S06_SH03"] = ("medium", "16:9", ["REF_WREN"], kf(GOLD,
    "Medium shot: Wren stands on the wet stone platform half-hidden behind a black cast-iron lamp post, watching something to the right of the frame with intense, suspicious focus, lips pressed together; the granite station wall behind her, puddles at her feet",
    chars=W1, refs_note="The reference image is Wren: match her exactly", neg_extra=f"{NW}, other people, {NO_YELLOW}, umbrella",
    lightdir="warm low sun from the left, wet glints"))
IMG["S06_SH04"] = ("medium", "16:9", ["S06_SH02"], kf(GOLD,
    "Edit of the reference image: the same shot from behind the wet bench, but the woman is gone; the closed mustard-yellow umbrella lies alone on the wet bench slats where she sat, its brass sparrow charm hanging from the strap; the railcar beyond the bench is starting to pull away toward the right; keep everything else exactly the same",
    chars=f"The umbrella: {UMB}", neg_extra="people, other yellow objects, text", lightdir="same light as the reference"))
IMG["S06_SH05"] = ("medium", "16:9", ["S03_SH05", "POW_SH04"], kf(LAMP,
    "Edit of reference image 1: keep the camera, the composition, the shelf unit with every object on it, the brass lattice grille doors, the green baize and the lamplight exactly the same; add only one thing: the closed mustard-yellow umbrella from reference image 2, lying horizontally inside the bottom compartment on the green baize, seen through the brass lattice; no glow",
    chars=f"The umbrella: {UMB}", neg_extra="other yellow objects, glow, sparkles, people, text, lettering, any other change", lightdir="same lamplight as reference image 1"))

# S07 office, Tuesday evening, LAMP
IMG["S07_SH01"] = ("medium", "16:9", ["REF_THEO", "S03_SH01"], kf(LAMP,
    "Medium-wide shot inside the lost-and-found office: Theo stands just inside the hall doorway, holding the closed wet mustard-yellow umbrella out in front of him by its handle, drops of rain water falling from its tip onto the floorboards, deadpan; the counter in the foreground, the shelves to the side",
    chars=f"{T1}. The umbrella: {UMB}", refs_note="Reference image 1 is Theo: match him exactly. Reference image 2 shows the room",
    neg_extra=f"{NT}, other people, other yellow objects, text", lightdir="warm lamplight from the desk lamp on the right"))
IMG["S07_SH02"] = ("medium", "16:9", ["REF_WREN", "S03_SH01"], kf(LAMP,
    "Medium close-up: Wren behind the long wooden counter in the lamplit office, staring at something just right of the frame with slowly dawning recognition, eyes widening, lips closed; the shelves of forgotten things behind her",
    chars=W1, refs_note="Reference image 1 is Wren: match her exactly. Reference image 2 shows the room", neg_extra=f"{NW}, other people, {NO_YELLOW}",
    lightdir="warm lamplight from the right"))
IMG["S07_SH03"] = ("medium", "16:9", ["REF_THEO", "S03_SH01"], kf(LAMP,
    "Medium shot in the lamplit lost-and-found office: Theo in profile on the left of the frame, facing right, pointing with his thumb over his shoulder toward the narrow steep wooden staircase in the far corner behind him that climbs to a dark square hatch in the ceiling; a deadpan warning look",
    chars=T1, refs_note="Reference image 1 is Theo: match him exactly. Reference image 2 shows the room and its staircase", neg_extra=f"{NT}, other people, {NO_YELLOW}, broken stairs",
    lightdir="warm lamplight from the right, the staircase in shadow"))
IMG["S07_SH04"] = ("medium", "16:9", ["S05_SH03", "REF_WREN"], kf(LAMP,
    "Extreme close-up insert: a girl's hands, warm light-brown skin, the sleeves of a burnt-orange corduroy jacket, holding the tip of the closed wet mustard-yellow umbrella under warm lamplight, her thumb beside the short mended tear stitched in a small zigzag of dark brown thread, the small brass sparrow charm hanging from the wrist strap; rain droplets on the canopy; framing matching reference image 1",
    chars=f"The umbrella: {UMB}", refs_note="Reference image 1 shows this umbrella's tear and charm: match them exactly. Reference image 2 is the girl (Wren), for her skin tone and jacket",
    neg_extra="extra fingers, malformed hands, text, lettering, maker's mark, other yellow objects, faces", lightdir="warm lamplight from the upper right"))

# S08 office, Tuesday evening, LAMP — the confrontation
IMG["S08_SH01"] = ("medium", "16:9", ["REF_WREN", "REF_IDA", "S03_SH01"], kf(LAMP,
    "Medium-wide two-shot across the long worn wooden counter of the lamplit lost-and-found office: Wren on the left of the frame lays the closed wet mustard-yellow umbrella on the counter between them and looks up and to the right at Ida, challenging; Ida on the right of the frame behind the counter, calm and unsurprised, hands resting on the counter; the shelves of forgotten things behind them",
    chars=f"Wren: {W1}. Ida: {I1}. The umbrella: {UMB}", refs_note="Reference image 1 is Wren and reference image 2 is Ida: match both exactly. Reference image 3 shows the room",
    neg_extra=f"{NW}, {NI}, other people, other yellow objects, text", lightdir="warm lamplight from the desk lamp at the right"))
IMG["S08_SH02"] = ("medium", "16:9", ["REF_IDA", "S03_SH01"], kf(LAMP,
    "Close-up, three-quarter view: Ida in the lamplit office looking steadily toward the left of the frame, grave and quiet, lips closed, the brass key on its dark red cord at her chest; shelves in soft shadow behind her",
    chars=I1, refs_note="Reference image 1 is Ida: match her exactly. Reference image 2 shows the room", neg_extra=f"{NI}, other people, {NO_YELLOW}",
    lightdir="warm lamplight from the right, deep shadow on the left of her face"))
IMG["S08_SH03"] = ("medium", "16:9", ["REF_IDA", "S03_SH05"], kf(LAMP,
    "Medium shot in profile: Ida stands beside the low bottom shelf compartment with the brass diamond-lattice grille, looking down at it, her right hand closed around the brass key at her chest, solemn; the compartment behind its grille is empty, lined with green baize",
    chars=I1, refs_note="Reference image 1 is Ida: match her exactly. Reference image 2 shows the grille compartment: keep its design", neg_extra=f"{NI}, other people, {NO_YELLOW}, objects in the compartment",
    lightdir="warm lamplight from behind the camera and the right"))
IMG["S08_SH04"] = ("medium", "16:9", ["REF_WREN", "S03_SH01"], kf(LAMP,
    "Close-up: Wren in the lamplit office looking up and to the right, earnest and searching, lips closed, her brass whistle on its chain at her chest; shelves soft behind her",
    chars=W1, refs_note="Reference image 1 is Wren: match her exactly. Reference image 2 shows the room", neg_extra=f"{NW}, other people, {NO_YELLOW}",
    lightdir="warm lamplight from the right"))

# S09 office, Tuesday midnight — the cliffhanger
IMG["S09_SH02"] = ("medium", "16:9", ["POW_SH03"], kf(MID,
    f"Edit of the reference image: keep the camera, the composition, the shelf, the brass grille, the moonlight and every object exactly the same; add only one thing: a tiny brass pipe-whistle about five centimeters long with a flared mouthpiece and three finger holes, no chain, lying on the green baize in the middle of the compartment, with {ARRIVAL}; the glow lights the inside of the compartment and the grille bars from within",
    neg_extra=f"chain, second whistle, {NO_YELLOW}, {NO_RED}, people, lit lamps, sparkles, beams", lightdir="all lamps unlit; the whistle's own warm glow is the only warm light"))
IMG["S09_SH03"] = ("medium", "16:9", ["REF_WREN", "POW_SH05", "S09_SH02"], kf(MID,
    "Medium shot in the moonlit office at midnight: Wren kneels on the floorboards in front of the low compartment, its brass grille door swung open, reaching in with one hand toward the small glowing whistle on the green baize; the warm amber glow from inside the compartment lights her face from below; her own brass whistle hangs on its chain at her chest",
    chars=W2, refs_note="Reference image 1 is Wren: match her face exactly. Reference image 2 shows her night clothes. Reference image 3 shows the compartment and the glowing whistle",
    neg_extra=f"{NW.replace(', second whistle', '')}, other people, lit lamps, {NO_YELLOW}, {NO_RED}", lightdir="all lamps unlit; the warm light comes only from the compartment below frame right; cool moonlight elsewhere"))
IMG["S09_SH04"] = ("high", "16:9", ["REF_WREN", "POW_SH06"], kf(MID,
    "Extreme close-up of a girl's two open hands held out side by side, palms up, warm light-brown skin, the sleeves of a burnt-orange corduroy jacket at the edges of frame; in each palm lies an identical tiny brass pipe-whistle about five centimeters long with a flared mouthpiece and three finger holes; the whistle in her left-hand palm (on the right of the image) is still attached to its thin brass chain, which rises out of the top of the frame toward her neck; the whistle in the other palm has no chain and glows faintly with a soft warm amber light; dark moonlit background",
    refs_note="Reference image 1 is the girl (Wren): match her skin tone and jacket. Reference image 2 shows the whistle and the night lighting of this scene",
    neg_extra="extra fingers, fused fingers, malformed hands, a third whistle, face, text, sparkles, beams, " + NO_YELLOW, lightdir="all lamps unlit; warm amber glow from the loose whistle and from below; cool blue moonlight on the background"))
IMG["S09_SH05"] = ("medium", "16:9", ["REF_WREN", "POW_SH06"], kf(MID,
    "Close-up of Wren at midnight, lit warmly from below by a glow just out of frame, her wonder turning to fear: eyes wide and glistening, brows drawn, lips closed and pressed together, her brass whistle on its chain at her chest; dark moonlit office behind her",
    chars=W2, refs_note="Reference image 1 is Wren: match her face exactly. Reference image 2 shows this scene's night lighting and her night clothes",
    neg_extra=f"{NW}, other people, lit lamps, visible lamp, {NO_YELLOW}, {NO_RED}", lightdir="all lamps unlit; the warm light comes from an unseen source below frame right; cool moonlight from the left"))

# ---------------------------------------------------------------- clips (grok_video_v15_lite, start image = keyframe)
VAVOID = f" Avoid: {NEGV}."
CLIP = {
 "S02_SH01": (4, "The vintage two-car railcar glides slowly out of the dark tunnel mouth toward the right along the platform and begins to slow down; dust glows in the low golden sunlight; the camera holds still." + VAVOID),
 "S02_SH02": (3, "The girl slowly lifts her gaze up and to the right; a light breeze stirs her bangs; the railcar behind her stays still; the camera pushes in very slightly." + VAVOID),
 "S02_SH07": (3, "The grey tabby cat eats the morsel from the old man's open palm; he smiles gently and strokes its back once with his other hand; the camera holds still." + VAVOID),
 "S03_SH06": (3, "The weathered hand slowly closes around the small brass key and holds it tight against her chest; the camera holds still." + VAVOID),
 "S05_SH01": (4, "The girl plays the tiny whistle softly, her fingertips lifting and covering its three holes in a slow melody, eyes half closed, swaying slightly; the clock glow beyond the glass stays steady; the camera holds still." + VAVOID),
 "S06_SH04": (4, "The railcar beyond the bench pulls away to the right and rolls off toward the tunnel; the yellow umbrella lies completely still on the wet bench in the foreground; the camera holds still." + VAVOID),
 "S07_SH01": (3, "The tall boy steps forward one pace and holds out the wet yellow umbrella; rain water drips from its tip onto the floorboards; the camera holds still." + VAVOID),
 "S09_SH04": (3, "The loose whistle in one palm glows a little brighter and softer, pulsing once like a slow breath; the hands tremble very slightly; both whistles stay in place; the camera holds still." + VAVOID),
 "S09_SH05": (4, "The girl's eyes widen as her wonder turns to fear; her breath catches; the warm glow from below flickers softly on her face; the camera pushes in very slowly." + VAVOID),
}

# ---------------------------------------------------------------- voice (seed_audio). NARR and WREN = Annie.
VOICES = {"NARR": ("Annie", "f2801b0f-e345-598e-86f5-8364d886d96b", 0), "WREN": ("Annie", "f2801b0f-e345-598e-86f5-8364d886d96b", 0),
          "IDA": ("Vera", "0c51919f-0756-5f8d-8169-026a339d8fd7", -8), "THEO": ("Archie", "bd072316-f77c-588b-b6e5-e46b9b03d008", 0)}
# (audio job id, scene, speaker, text). L001 is reused from POW-001.
LINES = [
 ("A00", "S01", "NARR", "In Larkspur, things get lost the day before they go missing."),
 ("A01", "S02", "NARR", "The summer my parents needed to sort some things out, they put me on a train to the end of the line.\n\nLarkspur Junction. One station, one clock, and one train a day.\n\nGrandma met me on the platform like she was collecting a parcel."),
 ("A02", "S02", "IDA", "You have your mother's chin."),
 ("A03", "S02", "NARR", "She didn't hug me. Grandma wasn't a hugger.\n\nThere was an old man on the bench, feeding a cat that clearly belonged to no one, and a boy checking his pocket watch against the station clock, like one of them was lying."),
 ("A04", "S03", "IDA", "Everything lost in Larkspur ends up here. Sooner or later."),
 ("A05", "S03", "NARR", "Hats. Gloves. A violin case. Every one of them waiting for somebody to remember.\n\nGrandma wrote each one down in a big green ledger. Some of the lines had red thread stitched right through them."),
 ("A06", "S03", "WREN", "What's that for?"),
 ("A07", "S03", "IDA", "Mending."),
 ("A08", "S03", "WREN", "And the bottom shelf?"),
 ("A09", "S03", "IDA", "Is mine. Don't touch it."),
 ("A10", "S03", "NARR", "Grandma had exactly one rule. Naturally, I broke it the first night."),
 ("A11", "S04", "IDA", "Eat your soup, Nora."),
 ("A12", "S04", "WREN", "It's Wren, Grandma."),
 ("A13", "S04", "IDA", "Wren. I know that."),
 ("A14", "S04", "NARR", "Nora is my mom. Grandma had never mixed us up before."),
 ("A15", "S05", "NARR", "I couldn't sleep, so I did what I always do. I played Mom's song on her whistle."),
 ("A16", "S05", "NARR", "Then the station clock struck twelve, and the light under the office door turned gold."),
 ("A17", "S05", "NARR", "The bottom shelf had been empty when I went to bed.\n\nNow there was an umbrella on it. Yellow. Mended near the tip. A little brass bird on the strap.\n\nI didn't know someone was watching me watch it."),
 ("A18", "S06", "NARR", "It rained all Tuesday afternoon. At six-fourteen the sky cleared, the train came in, and a woman in a camel coat sat down on the bench with a yellow umbrella.\n\nMended near the tip. A little brass bird on the strap."),
 ("A19", "S06", "NARR", "When the train left, she was on it. The umbrella wasn't.\n\nI ran to the office.\n\nThe bottom shelf was empty again. Like it had never been there at all."),
 ("A20", "S07", "THEO", "Someone left this on the bench."),
 ("A21", "S07", "NARR", "Theo. He keeps the station clock running, and apparently he hands in umbrellas."),
 ("A22", "S07", "THEO", "Clock gained a minute again last night. No reason. And don't go up the tower, by the way. The stairs are rotten."),
 ("A23", "S07", "NARR", "Same tear. Same bird. Same umbrella."),
 ("A24", "S08", "WREN", "This was on your shelf last night. Before she lost it."),
 ("A25", "S08", "IDA", "I know. I saw you."),
 ("A26", "S08", "WREN", "What is it?"),
 ("A27", "S08", "IDA", "The shelf shows what Larkspur will lose tomorrow. We watch. We write it down. And we never, ever give anything back early."),
 ("A28", "S08", "WREN", "Why not?"),
 ("A29", "S08", "IDA", "Promise me, Wren."),
 ("A30", "S08", "WREN", "I promise."),
 ("A31", "S08", "NARR", "I meant it. For about six hours."),
 ("A32", "S09", "NARR", "At midnight, the clock struck twelve, and the shelf turned gold again.\n\nThis time I recognized what was on it.\n\nMy mom's whistle.\n\nWhich was strange, because my mom's whistle was hanging around my neck."),
 ("A33", "S09", "NARR", "Tomorrow, I lose the only thing my mom ever gave me."),
]

def img_requests(ids):
    out = []
    for i, k in enumerate(ids):
        q, ar, refs, p = IMG[k]
        params = {"model": "gpt_image_2_6", "prompt": p, "quality": q, "resolution": "1k", "aspect_ratio": ar}
        if refs: params["medias"] = [{"value": job(r), "role": "image_references"} for r in refs]
        out.append({"index": i, "params": params})
    return out

def clip_requests(ids):
    return [{"index": i, "params": {"model": "grok_video_v15_lite", "prompt": CLIP[k][1], "duration": CLIP[k][0], "resolution": "720p",
             "aspect_ratio": "16:9", "medias": [{"value": job(k), "role": "start_image"}]}} for i, k in enumerate(ids)]

def line_requests(ids):
    out = []
    for i, a in enumerate(ids):
        _, sc, spk, text = next(l for l in LINES if l[0] == a)
        name, vid, rate = VOICES[spk]
        p = {"model": "seed_audio", "prompt": text, "voice_type": "preset", "voice_id": vid, "sample_rate": 48000, "format": "wav"}
        if rate: p["speech_rate"] = rate
        out.append({"index": i, "params": p})
    return out

if __name__ == "__main__":
    cmd, ids = sys.argv[1], sys.argv[2:]
    if cmd == "images": print(json.dumps(img_requests(ids)))
    elif cmd == "clips": print(json.dumps(clip_requests(ids)))
    elif cmd == "audio": print(json.dumps(line_requests(ids)))
    elif cmd == "words":
        tot = {}
        for _, sc, spk, t in LINES: tot[spk] = tot.get(spk, 0) + len(re.findall(r"[\w'-]+", t))
        print(tot, "total", sum(tot.values()))
    elif cmd == "list":
        for k, v in IMG.items(): print(k, v[0], v[1], v[2], len(v[3].split()), "words")
