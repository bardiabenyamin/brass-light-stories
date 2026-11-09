# EDL tail for EPISODE-001: S08 (confrontation), S09 (cliffhanger), end card. Executed inside assemble.py.
SC.append(("S08", [
    still(KF("S08_SH01"), 4.6, (1.0, 1.06), (0.45, 0.5), fin=0.5),
    still(KF("S08_SH04"), 3.8, (1.0, 1.06), (0.5, 0.4)),
    still(KF("S08_SH03"), 4.8, (1.0, 1.08), (0.3, 0.5)),
    still(KF("S03_SH03"), 2.7, (1.2, 1.3), (0.5, 0.5)),
    still(KF("S08_SH02"), 4.1, (1.0, 1.08), (0.6, 0.4)),
    still(KF("S08_SH04"), 2.3, (1.1, 1.18), (0.5, 0.38)),
    still(KF("S08_SH02"), 3.5, (1.15, 1.22), (0.62, 0.35)),
    still(KF("S08_SH04"), 3.0, (1.18, 1.26), (0.5, 0.36)),
    still(KF("S08_SH01"), 5.7, (1.08, 1.0), (0.45, 0.5), fout=1.2)],
  [bed(SFX("roomtone"), 0, 34.5, -6),
   vo("wren_L024", 0.8), vo("ida_L025", 5.0), vo("wren_L026", 7.4), vo("ida_L027", 8.8, inn=2.18),
   vo("wren_L028", 20.4), vo("ida_L029", 23.0), vo("wren_L030", 26.6), vo("narr_L031", 29.8, inn=1.3),
   mus(MID, 8.0, 21.0, 20.0, -23, 3.0, 3.0)]))
SC.append(("S09", [
    still(PKF("POW001_SH01_KF_v01"), 5.5, (1.08, 1.16), (0.49, 0.38), fin=1.0),
    xf(PKF("POW001_SH03_KF_v02"), KF("S09_SH02"), 7.0, 1.2, 1.8, (1.0, 1.08), (0.3, 0.82)),
    still(KF("S09_SH03"), 4.0, (1.0, 1.06), (0.55, 0.55)),
    clip(CL("S09_SH05"), 0, 1.3, 0.6),
    clip(CL("S09_SH04"), 0, 3.0, 0.6),
    clip(CL("S09_SH05"), 1.3, 4.0, 0.6),
    black(2.0),
    card(["THE EARLY SHELF", "To be continued"], 6.0)],
  [bed(SFX("roomtone"), 0, 28.2, -6), sfx(SFX("bell"), 0.8, -2), vo("narr_L032", 1.5), sfx(SFX("shimmer"), 6.2, -2),
   sfx(SFX("shimmer"), 19.2, -4), vo("narr_L033", 24.1),
   mus(MID, 0.5, 27.7, 28.0, -17, 2.0, 0.6), mus(MID, 30.2, 6.0, 0.0, -20, 1.0, 2.0, duck=False)]))
