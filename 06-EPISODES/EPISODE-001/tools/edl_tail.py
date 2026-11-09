# EDL tail for EPISODE-001: S08 (confrontation), S09 (cliffhanger), end card. Executed inside assemble.py.
# v02 (owner QC v01): every line in S08 is heard over the LISTENER (shot / reverse shot); no still face "speaks".
SC.append(("S08", [
    still(KF("S08_SH01"), 1.5, (1.0, 1.03), (0.45, 0.5), fin=0.5),
    still(KF("S08_SH02"), 3.5, (1.0, 1.05), (0.6, 0.4)),            # Ida listens: "This was on your shelf last night..."
    still(KF("S08_SH04"), 2.2, (1.0, 1.05), (0.5, 0.4)),            # Wren listens: "I know. I saw you."
    still(KF("S08_SH02"), 1.4, (1.06, 1.1), (0.6, 0.4)),            # Ida listens: "What is it?"
    still(KF("S03_SH05"), 4.6, (1.0, 1.1), (0.5, 0.8)),             # the shelf: "The shelf shows what Larkspur will lose tomorrow."
    still(KF("S03_SH03"), 2.7, (1.2, 1.3), (0.5, 0.5)),             # the ledger: "We watch. We write it down."
    still(KF("S08_SH04"), 4.1, (1.1, 1.18), (0.5, 0.38)),           # Wren listens: "And we never, ever give anything back early."
    still(KF("S08_SH02"), 2.3, (1.15, 1.22), (0.62, 0.35)),         # Ida listens: "Why not?"
    still(KF("S08_SH04"), 3.5, (1.18, 1.26), (0.5, 0.36)),          # Wren listens: "Promise me, Wren."
    clip(CL("S03_SH06"), 0, 3.0, 1.0),                              # Ida's hand closes on the key: "I promise."
    still(KF("S08_SH01"), 5.7, (1.08, 1.0), (0.45, 0.5), fout=1.2)],
  [vo("wren_L024", 1.7), vo("ida_L025", 5.3), vo("wren_L026", 7.5), vo("ida_L027", 8.8, inn=2.18),
   vo("wren_L028", 20.4), vo("ida_L029", 23.0), vo("wren_L030", 26.6), vo("narr_L031", 29.8, inn=1.3),
   mus(MID, 8.0, 21.0, 20.0, -23, 3.0, 3.0)]))
SC.append(("S09", [
    still(PKF("POW001_SH01_KF_v01"), 5.5, (1.08, 1.16), (0.49, 0.38), fin=1.0),
    xf(PKF("POW001_SH03_KF_v02"), KF("S09_SH02", "v02"), 7.0, 1.2, 1.8, (1.0, 1.08), (0.3, 0.82)),   # v02: one shared grille
    still(KF("S09_SH03"), 4.0, (1.0, 1.06), (0.55, 0.55)),
    clip(CL("S09_SH05"), 0, 1.3, 0.6),
    clip(CL("S09_SH04"), 0, 3.0, 0.6),
    clip(CL("S09_SH05"), 1.3, 4.0, 0.6),
    black(2.0),
    card(["THE EARLY SHELF", "To be continued"], 6.0)],
  [sfx(SFX("bell"), 0.8, -2), vo("narr_L032", 1.5), sfx(SFX("shimmer"), 6.2, -2),
   sfx(SFX("shimmer"), 19.2, -4), vo("narr_L033", 24.1),
   mus(MID, 0.5, 27.7, 28.0, -17, 2.0, 0.6), mus(MID, 30.2, 6.0, 0.0, -20, 1.0, 2.0, duck=False)]))
