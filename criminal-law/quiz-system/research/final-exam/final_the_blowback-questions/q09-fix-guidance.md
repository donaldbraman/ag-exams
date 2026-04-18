# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q9.** Assume Oscar and Penelope are charged with possession of the 20 kilograms of methamphetamine found in the stash house. Based on the principles of constructive possession, how should a court assess their liability?

(a) Only Oscar is guilty, because as the sole leaseholder of the property, he is the only person who can legally exercise dominion.
(b) Only Penelope is guilty, because her physical presence in the apartment is a strict prerequisite for establishing constructive possession of contraband.
(c) Both may be guilty, because Oscar's lease establishes his control over the premises, and Penelope's personal items establish her connection to the drugs. <!-- correct -->
(d) Neither is guilty, because the drugs were found in a common area rather than on either defendant's physical person, precluding actual possession.
(e) Neither is guilty, because the law dictates that multiple people cannot simultaneously exercise constructive possession over the exact same cache of narcotics.

**Answer:** (c)

**Explanation:** Constructive possession requires the power and intent to exercise dominion and control over contraband, which can be joint and inferred from circumstantial evidence. Oscar's status as the sole leaseholder establishes his control over the premises, while Penelope's personal items resting directly next to the drugs establish her immediate connection to and dominion over the contraband. (a) is wrong because exclusive leasing does not preclude others from exercising joint constructive possession. (b) is wrong because physical presence is not strictly required; constructive possession relies on dominion and control, not mere presence. (d) is wrong because constructive possession was specifically developed to prosecute individuals when drugs are found in common areas rather than on their physical person. (e) is wrong because the law explicitly recognizes that multiple individuals can hold joint constructive possession over the same items simultaneously.

**Tags:** chapters: [4, 10], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** General possession doctrine; constructive possession can be joint and is established by the power and intent to exercise dominion over the premises or the items.

<!-- GROUNDING-FAIL: constructive possession is not in any chapter map. The closest taught doctrines are: none (meta-map artifact is missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q9.** Assume Oscar and Penelope are charged with possession of the 20 kilograms of methamphetamine found in the stash house. Based on the principles of constructive possession, how should a court assess their liability?

(a) Only Oscar is guilty, because as the sole leaseholder of the property, he is the only person who can legally exercise dominion.
(b) Only Penelope is guilty, because her physical presence in the apartment is a strict prerequisite for establishing constructive possession of contraband.
(c) Both may be guilty, because Oscar's lease establishes his control over the premises, and Penelope's personal items establish her connection to the drugs. <!-- correct -->
(d) Neither is guilty, because the drugs were found in a common area rather than on either defendant's physical person, precluding actual possession.
(e) Neither is guilty, because the law dictates that multiple people cannot simultaneously exercise constructive possession over the exact same cache of narcotics.

**Answer:** (c)

**Explanation:** Constructive possession requires the power and intent to exercise dominion and control over contraband, which can be joint and inferred from circumstantial evidence. Oscar's status as the sole leaseholder establishes his control over the premises, while Penelope's personal items resting directly next to the drugs establish her immediate connection to and dominion over the contraband. (a) is wrong because exclusive leasing does not preclude others from exercising joint constructive possession. (b) is wrong because physical presence is not strictly required; constructive possession relies on dominion and control, not mere presence. (d) is wrong because constructive possession was specifically developed to prosecute individuals when drugs are found in common areas rather than on their physical person. (e) is wrong because the law explicitly recognizes that multiple individuals can hold joint constructive possession over the same items simultaneously.

**Tags:** chapters: [4, 10], topics: [constructive possession, dominion and control], difficulty: easy, cognitive: application

**Grounding:** General possession doctrine; constructive possession can be joint and is established by the power and intent to exercise dominion over the premises or the items.

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: pass
check 4: The stem fails to provide the necessary facts. It refers to "the stash house" as if previously established, and the correct answer/explanation rely on facts (Oscar being the leaseholder, Penelope's items being next to the drugs) that do not appear anywhere in the question text. Assumes a missing macro fact pattern.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: If this is meant to be a standalone question, incorporate the missing facts into the stem: "Police find 20 kilograms of methamphetamine in a stash house. Oscar is the sole leaseholder of the property, and Penelope's personal items are found resting directly next to the drugs. Assume Oscar and Penelope are charged with possession. Based on..."
-->
