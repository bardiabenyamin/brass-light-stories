"""Single-source prompt builder: regenerates EPISODE-001/prompts.md from the locked blocks.
Sources: 03-ART-DIRECTION/{visual-style,locations,props}.md, EPISODE-001/characters.md. Statuses: EPISODE-001/assets.md."""
import re, sys, json, pathlib
ROOT = pathlib.Path(sys.argv[1]); EP = ROOT/"06-EPISODES/EPISODE-001"; AD = ROOT/"03-ART-DIRECTION"
def blocks(path, kinds):
    t = path.read_text(); out = {}
    for m in re.finditer(r"```(" + "|".join(kinds) + r") ([\w ]+)\n(.*?)```", t, re.S):
        out[(m.group(1), m.group(2).strip())] = m.group(3).strip().replace("\n", " ")
    return out
VS = blocks(AD/"visual-style.md", ["style","light","fx","negative"])
LO = blocks(AD/"locations.md", ["location","locstate","locset","locneg"])
PR = blocks(AD/"props.md", ["prop","propneg"])
CH = blocks(EP/"characters.md", ["prompt","negative","expressions"])
STYLE, REFP, PROPP = VS[("style","core")], VS[("style","refpres")], VS[("style","proppres")]
NEG, NEG_LOC, NEG_VID = VS[("negative","master")], VS[("negative","location")], VS[("negative","video")]
LIGHT = {k: v for (kind, k), v in VS.items() if kind == "light"}

# statuses from assets.md (Asset ID -> Status)
A = (EP/"assets.md").read_text()
status = {m.group(1): m.group(2) for m in re.finditer(r"^\| (E001_[A-Za-z0-9_]+) \|[^|]*\|[^|]*\|[^|]*\|[^|]*\| ([A-Z]+) \|", A, re.M)}
def st(aid): return status.get(aid, "PLANNED")

def entry(code, fname, meta, prompt, neg):
    aid = fname.rsplit("_v", 1)[0]
    return (f"#### {code} · `{fname}`\n- {meta}\n- Status: **{st(aid)}**\n```text\n{prompt}\n```\nNegative:\n```text\n{neg}\n```\n"), aid

rows, out_cr, out_lr, out_pr = [], [], [], []
# ---------- Characters ----------
HUMAN = [("front","waist-up","4:5","waist-up portrait facing the camera straight on, arms relaxed at the sides"),
 ("side","waist-up","4:5","waist-up side view in full profile facing the left of the image"),
 ("34","waist-up","4:5","waist-up three-quarter view, body and face turned 45 degrees toward the left of the image"),
 ("full","full body","2:3","full-body head-to-toe standing pose facing the camera, relaxed A-pose with arms slightly away from the body, both feet visible on the floor"),
 ("expr","6-panel grid","3:2","expression sheet of this same character: six head-and-shoulders portraits arranged in a 3-by-2 grid, identical design, lighting and camera angle in every panel; top row: panel 1 {0}; panel 2 {1}; panel 3 {2}; bottom row: panel 4 {3}; panel 5 {4}; panel 6 {5}")]
CAT = [("front","full figure","1:1","front view, the cat sitting upright facing the camera"),
 ("side","full figure","4:3","side view, the cat standing on all four paws facing the left of the image"),
 ("34","full figure","1:1","three-quarter view, the cat sitting and turned 45 degrees toward the left of the image"),
 ("full","full figure","4:3","full body, the cat standing on all four paws in a front three-quarter view"),
 ("expr","6-panel grid","3:2","pose sheet of this same cat: six poses arranged in a 3-by-2 grid, identical markings, lighting and camera in every panel; top row: panel 1 {0}; panel 2 {1}; panel 3 {2}; bottom row: panel 4 {3}; panel 5 {4}; panel 6 {5}")]
OVR = {("abe","full"): "full-body head-to-toe standing pose facing the camera with his natural slight stoop, arms relaxed, the red signal lantern standing on the floor beside his right foot, both feet visible"}
NAMES = {"wren":"Wren Halloway","ida":"Ida Halloway","theo":"Theo Marsh","crane":"Ansel Crane","abe":"Abe Crane","ledger":"Ledger (cat)"}
SECT = {"wren":"§1","ida":"§2","theo":"§3","crane":"§4","abe":"§5","ledger":"§6"}
n = 0
for cid in ["wren","ida","theo","crane","abe","ledger"]:
    ex = [e.strip() for e in CH[("expressions", cid)].split(";")]; assert len(ex) == 6
    out_cr.append(f"\n### {NAMES[cid]} (`{cid}`): characters.md {SECT[cid]}\n")
    for view, framing, ar, vt in (CAT if cid == "ledger" else HUMAN):
        n += 1
        cb = CH[("prompt", cid)]
        if view == "expr": cb = re.sub(r",[^,]*expression\s*$", "", cb)
        src = "none (first image of this character)" if view == "front" else (f"approved `E001_CHR_{cid}_front` + `_34`" if view == "expr" else f"approved `E001_CHR_{cid}_front`")
        e, aid = entry(f"CR-{n:02d}", f"E001_CHR_{cid}_{view}_v01.png",
            f"View **{view}** · {framing} · AR **{ar}** · Image reference: {src} · Checks: characters.md {SECT[cid]} + continuity.md §A2 `{cid}`",
            f"{STYLE}. {REFP}. {OVR.get((cid, view), vt).format(*ex)}. {cb}.", f"{NEG}, {CH[('negative', cid)]}")
        out_cr.append(e); rows.append((aid, f"references/characters/E001_CHR_{cid}_{view}_v01.png", "Character ref", src.replace('`','')))
n += 1
e, aid = entry(f"CR-{n:02d}", "E001_PRP_keeperphoto_v01.png", "AR **3:2** · Image reference: approved Ida, Crane, Wren fronts (likeness) · Checks: characters.md §7.1 + continuity.md §A2 `keeperphoto`",
    f"{STYLE}. {CH[('prompt','keeperphoto')]}.", f"{NEG.replace('photorealistic, live action, ', '')}, {CH[('negative','keeperphoto')]}")
out_cr.append("\n### Photo variant and extra\n" + e); rows.append((aid, "references/props/E001_PRP_keeperphoto_v01.png", "Prop (photo variants)", "approved Ida, Crane, Wren fronts"))
n += 1
e, aid = entry(f"CR-{n:02d}", "E001_CHR_passenger_back_v01.png", "AR **2:3** · Image reference: none · Checks: characters.md §7.2 + continuity.md §A2 `passenger`",
    f"{STYLE}. {REFP}. full-body back view, head to toe. {CH[('prompt','passenger')]}.", f"{NEG}, {CH[('negative','passenger')]}")
out_cr.append(e); rows.append((aid, "references/characters/E001_CHR_passenger_back_v01.png", "Extra ref", "none"))

# ---------- Locations ----------
LREFS = [("platform","GOLD",None),("platform","DAY",None),("platform","OVERCAST",None),("platform","DAWN",None),("platform","DUSK",None),("platform","MIDNIGHT",None),("platform","OVERCAST","CLOCK_OFF"),
         ("office","DAY",None),("office","LAMP",None),("office","MIDNIGHT",None),("office","DAY","STAIR_BROKEN"),("office","MIDNIGHT","LADDER"),
         ("clockroom","DAY",None),("clockroom","MIDNIGHT",None),("clockroom","MIDNIGHT","DRAWER_OPEN"),("kitchen","DAY",None),("kitchen","LAMP",None)]
m = 0; cur = None
for loc, state, sset in LREFS:
    if loc != cur: out_lr.append(f"\n### LOC_{loc.upper()} (locations.md)\n"); cur = loc
    m += 1
    parts = [STYLE, LIGHT[state], LO[("location", loc)], LO[("locstate", f"{loc} {state}")]]
    if sset: parts.append(LO[("locset", f"{loc} {sset}")])
    parts.append("wide establishing shot from the master camera position, eye level, 35mm lens, no people")
    neg = f"{NEG}, {NEG_LOC}, {LO[('locneg', loc)]}"
    if sset == "DRAWER_OPEN": neg = neg.replace(", red objects", "")
    if sset == "CLOCK_OFF": neg = neg.replace("clock missing, ", "")
    tag = state.lower() + (("_" + sset.lower().replace("_","")) if sset else "")
    fname = f"E001_LOC_{loc}_{tag}_wide_v01.png"
    e, aid = entry(f"LR-{m:02d}", fname, f"Lighting **{state}**" + (f" · Set state **{sset}**" if sset else "") + " · AR **16:9** · Checks: locations.md fixed features + visual-style.md §6",
                   ". ".join(parts) + ".", neg)
    out_lr.append(e); rows.append((aid, f"references/locations/{fname}", "Location ref", "none (master)"))

# ---------- Props ----------
PORDER = ["umbrella","whistle","idakey","ledger","redthread","watch","watchcracked","notebook","clock","earlyshelf","drawer","memset","toytrain","mitten","lantern","case","crate","trolley","carkeys","railcar"]
AR = {"ledger":"4:3","earlyshelf":"16:9","drawer":"4:3","memset":"16:9","crate":"4:3","trolley":"4:3","railcar":"16:9"}
k = 0
for pid in PORDER:
    k += 1
    pres = PROPP if pid != "railcar" else PROPP.replace("prop reference image, single object", "vehicle reference image, single vehicle")
    e, aid = entry(f"PR-{k:02d}", f"E001_PRP_{pid}_v01.png", f"AR **{AR.get(pid,'1:1')}** · Checks: props.md register row `{pid}`",
                   f"{STYLE}. {pres}. {PR[('prop', pid)]}.", f"{NEG}, {PR[('propneg', pid)]}")
    out_pr.append(e); rows.append((aid, f"references/props/E001_PRP_{pid}_v01.png", "Prop ref", "none"))

lights = "\n".join(f"- `{k}`: {v}" for k, v in LIGHT.items())
doc = f"""# Prompts — EPISODE-001 (series reference batches + episode batches)

Status: **Style LOCKED v1 (Prompt 03, 2026-11-09).** The series gate is approved. Generation is allowed **only for the
proof-of-work** (`04-TESTS/POW-001/`) until full-episode spend is approved.
Each entry's status below is read from `assets.md`, the status source of truth.

**Do not hand-edit the batch sections.** Edit the source blocks in `03-ART-DIRECTION/visual-style.md`,
`locations.md`, `props.md`, or `characters.md`, then rebuild with `python3 03-ART-DIRECTION/build_prompts.py .` from the project root. That keeps every copy identical to
the locked canon.

Generation order once a batch is approved: **character references → location references → prop references →
storyboard keyframes → clips → audio.** Inspect identity and consistency on a small batch before generating the full
set.

---

## Master style prompt (LOCKED v1)

```text
{STYLE}
```

Lighting state blocks (append exactly one per image; see `visual-style.md` §6):
{lights}

## Master negative prompt (LOCKED v1)

```text
{NEG}
```

Add-ons: **location** `{NEG_LOC}` · **video (clips)** `{NEG_VID}`

---

## Character reference batch (CR-01 to CR-{n:02d})

Composition: `STYLE_CORE + REF_PRESENTATION + view + character block`. Order: each character's front first → inspect
(continuity.md §A2) → the other views using the approved front as the image reference → the expression sheet last.
{''.join(out_cr)}
---

## Location reference batch (LR-01 to LR-{m:02d})

Composition: `STYLE_CORE + lighting state + location base + location state (+ set state) + "wide establishing shot…"`.
{''.join(out_lr)}
---

## Prop reference batch (PR-01 to PR-{k:02d})

Composition: `STYLE_CORE + PROP_PRESENTATION + prop block`. The keepers' photo is CR-31.
{''.join(out_pr)}
---

## Image batch sheet (Prompt 06)

| # | Asset ID / filename | Source refs | Pose / expression | Wardrobe / props | Environment / lighting | Composition / camera / framing | AR | Prompt | Negative | Continuity checks | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | _None yet_ | — | — | — | — | — | — | — | — | — | BLOCKED (full-episode spend not yet approved) |

## Clip batch sheet (Prompt 07, may move to `animation-batch.md`)

| Shot ID | Source image | Primary action | Secondary motion | Camera | Duration | Start → end state | Prompt | Negative | Status |
|---|---|---|---|---|---|---|---|---|---|
| — | _None yet_ | — | — | — | — | — | — | — | BLOCKED |

## Audio batch sheet (Prompt 08)

See `dialogue.md` for line IDs. Music and SFX go in `audio-cue-sheet.md` (Prompt 08).
"""
(EP/"prompts.md").write_text(doc)

# add missing PLANNED rows to assets.md
A = (EP/"assets.md").read_text()
add = [f"| {aid} | `{path}` | {typ} | {src} | — | PLANNED | — | 0 | 0 | 0 | prompts.md |" for aid, path, typ, src in rows if f"| {aid} |" not in A]
if add:
    A = A.replace("\n\n**Episode total:", "\n" + "\n".join(add) + "\n\n**Episode total:", 1)
    planned = len(re.findall(r"\| PLANNED \|", A))
    A = re.sub(r"Planned: \*\*\d+\*\*[^·]*·", f"Planned: **{planned}** (reference prompts written, not submitted) ·", A)
    (EP/"assets.md").write_text(A)
print(json.dumps({"CR": n, "LR": m, "PR": k, "rows_added_to_assets": len(add)}))
