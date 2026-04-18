# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q9.** The State charges Brenda with felony murder predicated on her operation of the illicit pharmaceutical lab. Brenda argues that Charles's sleepwalking was the true cause of the fire. Assuming the jurisdiction applies standard felony murder rules, will this defense succeed?

(a) No, because the death occurred during the commission of an inherently dangerous predicate felony. Brenda's hazardous lab setup directly contributed to the fatal fire, satisfying the causal requirements. <!-- correct -->
(b) Yes, because the felony murder rule requires the prosecution to prove that the defendant harbored express malice. She must have specifically desired the death of the tenant.
(c) Yes, because the physical intervention of an unconscious actor legally downgrades any resulting homicide. The charge must be reduced from felony murder to involuntary manslaughter.
(d) No, because felony murder only requires demonstrating that the victim was a foreseeable target of the underlying crime. The actual mechanism of death is entirely irrelevant to the conviction.
(e) No, because the "agency rule" of felony murder explicitly makes defendants strictly liable for the actions of third parties. This applies even to the autonomous, unforeseeable actions of unconscious employees.

**Answer:** (a)

**Explanation:** Option (a) is correct because felony murder applies when a death occurs during the commission or attempted commission of an inherently dangerous predicate felony, provided there is a causal connection. The operation of an illicit chemical lab is an inherently dangerous felony, and the fire resulted directly from the hazardous setup. Charles's sleepwalking does not sever this causal chain. Option (b) is incorrect because the primary feature of the felony murder rule is that it dispenses with the need to prove express malice. Option (c) is incorrect because third-party intervention does not automatically downgrade felony murder. Option (d) is incorrect because causation between the felony and the death must still be established. Option (e) is incorrect because the "agency rule" generally limits felony murder to killings committed by the felons themselves, rather than making them strictly liable for all third-party actions.

**Tags:** chapters: [14], topics: [felony murder, inherently dangerous felony, causation], difficulty: easy, cognitive: application

**Grounding:** Felony Murder Rule (causal connection to an inherently dangerous predicate felony)

<!-- GROUNDING-FAIL: Felony murder is not in any chapter map. The closest taught doctrines are: none (meta-map artifact is missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q9.** The State charges Brenda with felony murder predicated on her operation of the illicit pharmaceutical lab. Brenda argues that Charles's sleepwalking was the true cause of the fire. Assuming the jurisdiction applies standard felony murder rules, will this defense succeed?

(a) No, because the death occurred during the commission of an inherently dangerous predicate felony. Brenda's hazardous lab setup directly contributed to the fatal fire, satisfying the causal requirements. <!-- correct -->
(b) Yes, because the felony murder rule requires the prosecution to prove that the defendant harbored express malice. She must have specifically desired the death of the tenant.
(c) Yes, because the physical intervention of an unconscious actor legally downgrades any resulting homicide. The charge must be reduced from felony murder to involuntary manslaughter.
(d) No, because felony murder only requires demonstrating that the victim was a foreseeable target of the underlying crime. The actual mechanism of death is entirely irrelevant to the conviction.
(e) No, because the "agency rule" of felony murder explicitly makes defendants strictly liable for the actions of third parties. This applies even to the autonomous, unforeseeable actions of unconscious employees.

**Answer:** (a)

**Explanation:** Option (a) is correct because felony murder applies when a death occurs during the commission or attempted commission of an inherently dangerous predicate felony, provided there is a causal connection. The operation of an illicit chemical lab is an inherently dangerous felony, and the fire resulted directly from the hazardous setup. Charles's sleepwalking does not sever this causal chain. Option (b) is incorrect because the primary feature of the felony murder rule is that it dispenses with the need to prove express malice. Option (c) is incorrect because third-party intervention does not automatically downgrade felony murder. Option (d) is incorrect because causation between the felony and the death must still be established. Option (e) is incorrect because the "agency rule" generally limits felony murder to killings committed by the felons themselves, rather than making them strictly liable for all third-party actions.

**Tags:** chapters: [14], topics: [felony murder, inherently dangerous felony, causation], difficulty: easy, cognitive: application

**Grounding:** Felony Murder Rule (causal connection to an inherently dangerous predicate felony)

<!-- audit: MUST FIX
Check 1: pass (assuming the missing facts support the conclusion)
Check 2: pass
Check 3: pass
Check 4: Fails. The stem provides no factual background, making it an orphaned question. It references Brenda, Charles's sleepwalking, an illicit lab, a fire, and a tenant without introducing any of these elements. Students cannot evaluate causation without the actual facts.
Check 5: Fails. The phrase "standard felony murder rules" is a legal fiction. Jurisdictions split on how to evaluate "inherently dangerous" felonies (in the abstract vs. as-committed) and how to attribute causation for third-party acts (agency approach vs. proximate cause approach). 
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the missing master fact pattern into the stem. Additionally, explicitly stipulate the jurisdiction's rules regarding inherently dangerous felonies and causation rather than relying on ambiguous "standard" rules.
-->

## Issue 3 — edge-case

**Q9.** The State charges Brenda with felony murder predicated on her operation of the illicit pharmaceutical lab. Brenda argues that Charles's sleepwalking was the true cause of the fire. Assuming the jurisdiction applies standard felony murder rules, will this defense succeed?

(a) No, because the death occurred during the commission of an inherently dangerous predicate felony. Brenda's hazardous lab setup directly contributed to the fatal fire, satisfying the causal requirements. <!-- correct -->
(b) Yes, because the felony murder rule requires the prosecution to prove that the defendant harbored express malice. She must have specifically desired the death of the tenant.
(c) Yes, because the physical intervention of an unconscious actor legally downgrades any resulting homicide. The charge must be reduced from felony murder to involuntary manslaughter.
(d) No, because felony murder only requires demonstrating that the victim was a foreseeable target of the underlying crime. The actual mechanism of death is entirely irrelevant to the conviction.
(e) No, because the "agency rule" of felony murder explicitly makes defendants strictly liable for the actions of third parties. This applies even to the autonomous, unforeseeable actions of unconscious employees.

**Answer:** (a)

**Explanation:** Option (a) is correct because felony murder applies when a death occurs during the commission or attempted commission of an inherently dangerous predicate felony, provided there is a causal connection. The operation of an illicit chemical lab is an inherently dangerous felony, and the fire resulted directly from the hazardous setup. Charles's sleepwalking does not sever this causal chain. Option (b) is incorrect because the primary feature of the felony murder rule is that it dispenses with the need to prove express malice. Option (c) is incorrect because third-party intervention does not automatically downgrade felony murder. Option (d) is incorrect because causation between the felony and the death must still be established. Option (e) is incorrect because the "agency rule" generally limits felony murder to killings committed by the felons themselves, rather than making them strictly liable for all third-party actions.

**Tags:** chapters: [14], topics: [felony murder, inherently dangerous felony, causation], difficulty: easy, cognitive: application

**Grounding:** Felony Murder Rule (causal connection to an inherently dangerous predicate felony)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Q9 heavily overlaps with and spoils Q4. Q4 specifically tests whether Charles's sleepwalking is an independent superseding cause that severs Brenda's liability for the fire. Q9 currently tests the exact same causal chain for the felony murder charge, and Option (a) explicitly reveals that Brenda's setup "satisfies the causal requirements," giving away the correct conclusion for Q4. 
Recommended fix: Shift Brenda's defense in Q9 away from causation. Have her argue a lack of mens rea for the death (e.g., "Brenda argues she never intended to harm anyone and took precautions"). This allows you to test the core malice-substitution function of felony murder (making a corrected version of Option B the right answer) without spoiling the intervening cause analysis required for Q4.
-->
