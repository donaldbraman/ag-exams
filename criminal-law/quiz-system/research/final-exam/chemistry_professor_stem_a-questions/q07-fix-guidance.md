# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q7.** Assume the jurisdiction uses the "facts-as-committed" approach, and the court finds that Arthur's distribution of the drug was inherently dangerous. Arthur's defense counsel argues that the felony murder charge must be dismissed because the predicate felony merges with the homicide. Will the merger argument succeed?

(a) Yes, because the drug distribution directly caused Marcus's death, meaning the two offenses must merge.
(b) No, because the drug distribution had an independent felonious purpose—financial gain—beyond the commission of the injury or death. <!-- correct -->
(c) Yes, because the drug distribution was an assaultive act that lacked any purpose independent of harming the victim.
(d) No, because the merger doctrine only applies to specific intent crimes, and drug distribution is a general intent offense.
(e) Yes, because the act of handing the drugs to Marcus was simultaneous with the conduct that caused his death.

**Answer:** (b)

**Explanation:** The merger doctrine bars felony murder only when the predicate felony is assaultive and has no independent felonious purpose beyond the violence itself. Drug distribution does not merge because it has an independent purpose (e.g., financial gain from the $500 sale), unlike an assault. (a) is wrong because causation alone does not trigger merger; there must be a lack of independent purpose. (c) is wrong because drug distribution is not an inherently assaultive act intended only to cause harm. (d) is wrong because the merger doctrine's application depends on independent purpose, not the specific/general intent distinction. (e) is wrong because temporal proximity does not trigger merger if the independent purpose test is satisfied.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine, independent purpose], difficulty: hard, cognitive: application

**Grounding:** merger-independent-purpose

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: FAIL - The explanation references a "$500 sale" that is nowhere in the question stem.
check 4: FAIL - The stem is completely missing its underlying fact pattern. It drops the student into a scenario referencing "Arthur," "Marcus's death," and a drug distribution without ever establishing these facts. Because the stem explicitly stipulates a "facts-as-committed" approach, the student fundamentally requires the actual facts of how the crime was committed (e.g., was it a sale for profit, or did he forcefully inject Marcus?) to determine if there was an independent purpose. 
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Insert a short factual setup at the beginning of the stem. Example: "Arthur sold Marcus $500 worth of heroin. Marcus injected the drugs and died of an overdose."
-->

## Issue 2 — argpass-opus

**Q7.** Assume the jurisdiction uses the "facts-as-committed" approach, and the court finds that Arthur's distribution of the drug was inherently dangerous. Arthur's defense counsel argues that the felony murder charge must be dismissed because the predicate felony merges with the homicide. Will the merger argument succeed?

(a) Yes, because the drug distribution directly caused Marcus's death, meaning the two offenses must merge.
(b) No, because the drug distribution had an independent felonious purpose—financial gain—beyond the commission of the injury or death. <!-- correct -->
(c) Yes, because the drug distribution was an assaultive act that lacked any purpose independent of harming the victim.
(d) No, because the merger doctrine only applies to specific intent crimes, and drug distribution is a general intent offense.
(e) Yes, because the act of handing the drugs to Marcus was simultaneous with the conduct that caused his death.

**Answer:** (b)

**Explanation:** The merger doctrine bars felony murder only when the predicate felony is assaultive and has no independent felonious purpose beyond the violence itself. Drug distribution does not merge because it has an independent purpose (e.g., financial gain from the $500 sale), unlike an assault. (a) is wrong because causation alone does not trigger merger; there must be a lack of independent purpose. (c) is wrong because drug distribution is not an inherently assaultive act intended only to cause harm. (d) is wrong because the merger doctrine's application depends on independent purpose, not the specific/general intent distinction. (e) is wrong because temporal proximity does not trigger merger if the independent purpose test is satisfied.

**Tags:** chapters: [14], topics: [felony murder, merger doctrine, independent purpose], difficulty: hard, cognitive: application

**Grounding:** merger-independent-purpose

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Causation is the crux of the homicide actus reus. If the distribution directly caused the death, the distribution and the homicide share the exact same physical conduct. Under the "integral part of the homicide" test (often associated with *People v. Ireland*), an offense that is inseparable from the act causing death merges with the homicide. Therefore, a student could argue that direct causation of death by the predicate felony means the offenses must categorically merge.
(b) Argument-for: The merger doctrine limits felony murder so that assaultive crimes don't automatically become murder if the victim dies. Courts use the "independent felonious purpose" test (the *Burton* test) to determine if merger applies. Drug distribution typically involves the independent purpose of transferring narcotics, often for financial gain, which is distinct from a purpose to injure or kill. Because this independent purpose exists, the offenses do not merge.
(c) Argument-for: If a court uses the "facts-as-committed" approach and finds the drug distribution inherently dangerous, it may view the act as a direct physical assault on the victim's bodily integrity. Administering a dangerous substance is routinely classified as an assaultive act. If the transaction is viewed solely as an act that physically harms the victim without a legally recognized separate protective purpose, a student could argue it merges under the assaultive-act standard.
(d) Argument-for: The merger doctrine traditionally applies to crimes involving violence or the intent to cause physical injury, which are often specific intent crimes (like assault with intent to kill). Drug distribution is typically a general intent crime. A student might logically (though incorrectly) deduce that the doctrine's historical focus on intent-based harm categorically excludes general intent regulatory or drug offenses from the merger doctrine.
(e) Argument-for: Temporal and spatial proximity are key factors in analyzing whether two acts are part of the same transaction. If the distribution and the lethal effect are entirely simultaneous, there is no separate actus reus to support an independent felony. This complete overlap in time and conduct strongly supports the argument that the felony is an integral part of the homicide, compelling merger.

Head-to-head: 
Option (b) correctly states the legal standard—the independent felonious purpose test—and properly applies it to drug distribution, which inherently possesses a purpose distinct from causing injury. Option (a) relies on a false legal premise; direct causation does not categorically compel merger if an independent purpose exists. Option (c) fails because it asserts a factual/legal falsity: drug distribution does not categorically lack an independent purpose. Option (d) introduces a completely fabricated legal rule, falsely claiming the merger doctrine hinges strictly on the specific vs. general intent distinction. Option (e) relies on the false legal assumption that temporal simultaneity alone requires merger, ignoring the primary requirement of an independent purpose. 

Falsifiable claim per distractor:
- (a): "meaning the two offenses must merge" — wrong because direct causation does not categorically mandate merger; an independent felonious purpose defeats merger regardless of direct causation.
- (c): "lacked any purpose independent of harming the victim" — wrong because drug distribution inherently involves the independent purpose of transferring narcotics (usually for compensation), unlike a pure assault.
- (d): "merger doctrine only applies to specific intent crimes" — wrong because the doctrine's application turns on whether the felony has an independent felonious purpose, not on the specific/general intent dichotomy.
- (e): "because the act of handing the drugs to Marcus was simultaneous with the conduct that caused his death" — wrong because simultaneous temporal proximity does not categorically trigger merger if the underlying felony retains an independent felonious purpose.

Recommended fix: The prompt assumes facts not in evidence (Marcus's identity and the financial motive). Add a brief factual sentence to the prompt to properly ground the options, such as: "Arthur sold a lethal dose of drugs to Marcus for $500."
-->
