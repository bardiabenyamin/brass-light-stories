# Series Canon (Season 1)

Status: **APPROVED 2026-11-09**. Changes now need a backup and a dated note

Prompt 01 writes these files. Until the owner approves them, nothing downstream may spend credits.

| File | Contents | Status |
|---|---|---|
| `concept-options.md` | 2–3 series concepts inside the approved channel identity, with trade-offs and a recommendation | APPROVED 2026-11-09 |
| `series-bible.md` | Premise, cast, relationships, secrets, arcs, season question and intended answer, opposing force, world rules, what may and may not change | APPROVED 2026-11-09 |
| `six-episode-roadmap.md` | For each of Episodes 1–6: hook, goal, conflict, turning event, episode question and resolution, what the audience learns, what stays open, season movement, cliffhanger type and final beat, next opening payoff. Must show cause → effect | APPROVED 2026-11-09 |
| `cliffhanger-ledger.md` | One entry per episode; seeded by Prompt 01 and appended by Prompts 05 and 13 | Seeded: 6 PLANNED entries |

## Roadmap acceptance test (from the prompt book)

The roadmap is complete only if **all** of these hold:

- [x] A format decision (serialized or anthology) with reasons (`concept-options.md` Part A)
- [x] A season central question and the intended season-level answer (`series-bible.md` §6)
- [x] Arcs for the main characters, where each starts and where each ends (`series-bible.md` §4)
- [x] For each episode: its own conflict and an episode-level resolution (roadmap: "Conflict and stakes", "Episode question … resolved")
- [x] Clue → payoff pairs, each with the episode where it is planted and the episode where it pays off (`series-bible.md` §9, K1–K11)
- [x] A cliffhanger → next-opening chain for Episodes 1→2, 2→3, 3→4, 4→5, 5→6, with no cliffhanger abandoned (roadmap Part D; ledger)
- [x] Episode 2 responds to Episode 1's ending, Episode 3 to Episode 2's, and so on (roadmap "Causal spine")
- [x] Cliffhanger types rotate: impossible evidence → exposure → reversal → arrival → decision → finale
- [x] Episode 6 resolves the season question, and its final hook is declared as a Season 2 hook
- [x] Production feasibility: reused characters and locations, risky shots flagged, counts of speaking roles, locations, and keyframes per episode (roadmap Part E)
- [x] Episode 1 concept presented for approval (`06-EPISODES/EPISODE-001/STORY-BIBLE.md` §4; summary in chat 2026-11-09)
- [x] **Owner approval recorded** in `06-EPISODES/EPISODE-001/PLAN.md` (2026-11-09: "Series approved: The Early Shelf roadmap and Episode 1 concept, as written.")

**How this was checked (2026-11-09):**
- A script parsed the roadmap and ledger. It confirmed all Part C fields for Eps 1–6, all 14 ledger fields ×6, the
  chain rows 1→2 through 5→6, no repeated cliffhanger type back to back, K1–K11 referenced, rule references within
  R1–R10, an identical season question in the bible and roadmap, and that each opening answer matches the next
  entry's payoff. One mismatch (5→6 wording) was found and fixed.
- A manual logic pass then found and fixed two issues: R5's scale (see the bible change log) and Ep4 wording that
  conflicted with "knowingly" in R4.
- Remaining items to verify at script stage (Prompt 04/05): the Ep3 return adds jump #32 to Theo's log; Ida's ledger
  shows a fresh red thread for the night Wren arrived (the K2 "gained a minute last night").
