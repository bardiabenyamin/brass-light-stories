"""Compose POW-001 prompts from the locked blocks (single source). Usage: python3 -I compose_pow.py <project_root>"""
import re, sys, json, pathlib
ROOT = pathlib.Path(sys.argv[1]); AD = ROOT/"03-ART-DIRECTION"; EP = ROOT/"06-EPISODES/EPISODE-001"
def blocks(path, kinds):
    t = path.read_text(); return {(m.group(1), m.group(2).strip()): m.group(3).strip().replace("\n"," ")
        for m in re.finditer(r"```(" + "|".join(kinds) + r") ([\w ]+)\n(.*?)```", t, re.S)}
VS = blocks(AD/"visual-style.md", ["style","light","negative"]); LO = blocks(AD/"locations.md", ["location","locstate"])
PR = blocks(AD/"props.md", ["prop"]); CH = blocks(EP/"characters.md", ["prompt"])
S, MID = VS[("style","core")], VS[("light","MIDNIGHT")]
P = (EP/"prompts.md").read_text()
def cr(code): return re.search(rf"#### {code} .*?```text\n(.*?)\n```", P, re.S).group(1)
shots = {
 "REF_WREN": {"file": "06-EPISODES/EPISODE-001/references/characters/E001_CHR_wren_front_v01.png", "ar": "4:5", "refs": [], "prompt": cr("CR-01")},
 "REF_IDA":  {"file": "06-EPISODES/EPISODE-001/references/characters/E001_CHR_ida_front_v01.png",  "ar": "4:5", "refs": [], "prompt": cr("CR-06")},
 "SH01": {"file": "06-EPISODES/EPISODE-001/references/locations/E001_LOC_platform_midnight_wide_v01.png", "ar": "16:9", "refs": [], "prompt": cr("LR-06")},
 "SH02": {"file": "04-TESTS/POW-001/keyframes/POW001_SH02_KF_v01.png", "ar": "16:9", "refs": [], "prompt":
   f"{S}. {MID}. Extreme close-up insert of the large round station clock on a mountain station facade at night: a pale celadon-green translucent enamel face glowing softly from within like a pale moon, twelve plain black baton markers that are thicker at the twelve, three, six and nine positions, no numerals, the short black hour hand pointing straight up at the twelve-o'clock marker and the long black minute hand one small step before it, a polished brass rim, part of an ornate black wrought-iron ring bracket, dark midnight-blue sky and the edge of a slate roof behind, 100mm lens, very shallow depth of field, no lettering."},
 "SH03": {"file": "04-TESTS/POW-001/keyframes/POW001_SH03_KF_v01.png", "ar": "16:9", "refs": [], "prompt":
   f"{S}. {MID}. Inside the lost-and-found office of a small mountain railway station at midnight, a medium shot facing the back wall: floor-to-ceiling worn wooden shelves holding neatly arranged forgotten things such as hats, scarves, gloves, books and bags in muted blues, greens, browns and greys with small blank colored paper tags, and in the lower third the bottom compartment closed behind a small brass diamond-lattice grille door with a simple latch, its inside lined with faded green baize and completely empty, a cool blue shaft of moonlight falling across the shelves from the right, the brass grille catching a faint glint, honey-colored floorboards, 40mm lens, no people, no lettering."},
 "SH04": {"file": "04-TESTS/POW-001/keyframes/POW001_SH04_KF_v01.png", "ar": "16:9", "refs": ["SH03"], "prompt":
   f"Edit the reference image. Keep everything exactly the same: the same shelves, framing, camera, moonlight, colors and style. Add only one object: on the empty green baize behind the brass grille lies {PR[('prop','umbrella')]}. A soft warm amber glow blooms around the umbrella, lighting the inside of the compartment and the grille bars from within. No people, no lettering."},
 "SH05": {"file": "04-TESTS/POW-001/keyframes/POW001_SH05_KF_v01.png", "ar": "16:9", "refs": ["REF_WREN"], "prompt":
   f"{S}. {MID}. Inside a dark lost-and-found office at midnight, a medium shot of an open doorway in a cream plaster wall leading to a dark hall: the girl from the reference image, {CH[('prompt','wren_w2')]}, peeks around the edge of the wooden door frame from the dark hall, only her head, one shoulder and one hand on the frame visible, her face lit warmly from low on the right by a soft amber glow coming from off-screen, wide grey-green eyes full of wonder, cool moonlit blue everywhere else, 50mm lens, shallow depth of field, no lettering."},
 "SH06": {"file": "04-TESTS/POW-001/keyframes/POW001_SH06_KF_v01.png", "ar": "16:9", "refs": ["REF_WREN"], "prompt":
   f"{S}. {MID}. Close-up portrait at midnight in a dark room: the girl from the reference image, {CH[('prompt','wren_w2')]}, her face lit softly from below by a warm amber glow from off-screen right, eyes wide with awe with the amber light reflected in them, lips slightly parted, her right hand raised to hold the tiny brass pipe-whistle at her throat, cool midnight-blue shadow behind her, 85mm lens, very shallow depth of field, no lettering."},
 "SH07": {"file": "04-TESTS/POW-001/keyframes/POW001_SH07_KF_v01.png", "ar": "16:9", "refs": ["REF_IDA"], "prompt":
   f"{S}. {MID}. Inside a dark lost-and-found office at midnight, a medium-wide shot of an open doorway to a dark hall: the woman from the reference image, {CH[('prompt','ida_i2')]}, stands still in the doorway watching, half in shadow, her face lit faintly from low on the right by a soft amber glow from off-screen, one hand closing around the brass key at her chest, cool moonlit blue in the hall behind her, 40mm lens, no lettering."},
}
clips = {
 "C01": {"src": "SH01", "prompt": "Very slow steady push-in toward the station front at midnight. The round clock face glows softly; faint haze drifts; pine tops sway gently; the lamp light flickers very slightly. No people, no text, nothing else moves."},
 "C02": {"src": "SH02", "prompt": "Locked camera. The long minute hand moves one small step forward to meet the hour hand exactly at twelve, then stays still. Faint haze drifts past the glowing clock face. No text, nothing else moves."},
 "C05": {"src": "SH05", "prompt": "Locked camera. The girl slowly leans a little further around the door frame, her eyes widening in wonder; the warm amber light on her face pulses gently; her hair moves slightly; she blinks once. Her face and clothes stay exactly the same. No other movement, no text."},
 "C06": {"src": "SH06", "prompt": "Locked camera, close-up. The girl slowly tightens her hand around the small brass whistle at her throat and holds her breath, eyes fixed off-screen right; the amber glow flickers gently on her face; subtle breathing. Her face stays exactly the same. No other movement, no text."},
 "C07": {"src": "SH07", "prompt": "Locked camera. The old woman stands still in the doorway, watching; her hand slowly closes around the brass key at her chest; her long silver braid shifts slightly; the amber glow pulses gently on her face. Her face stays exactly the same. No other movement, no text."},
}
vo = {"VO1": "In Larkspur, things get lost the day before they go missing.", "VO2": "Grandma had exactly one rule. The bottom shelf was hers."}
neg = VS[("negative","master")]
json.dump({"shots": shots, "clips": clips, "vo": vo, "negative": neg}, open(ROOT/"04-TESTS/POW-001/pow_prompts.json","w"), indent=1)
print(json.dumps({k: len(v["prompt"]) for k, v in shots.items()}))
