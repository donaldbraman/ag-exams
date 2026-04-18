# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Damon is charged with first-degree felony murder based on the attempted robbery of the stash house. Damon's defense argues that because he abandoned the robbery upon seeing Vic and shot him out of personal animus, the felony murder rule does not apply. How will a court likely rule?

(a) Damon is guilty of felony murder because the murder occurred during the *res gestae* of the attempted robbery, and an unintended death during an attempted predicate felony is graded upward as first-degree murder. <!-- correct -->
(b) Damon is not guilty of felony murder because he did not take any drugs or demand money, meaning the underlying felony was never completed.
(c) Damon is not guilty of felony murder under the merger doctrine, because his independent personal purpose to assault Vic means the assault merges with the homicide.
(d) Damon is guilty of felony murder, but only in the second degree, because the underlying predicate crime was merely an attempt rather than a completed felony.
(e) Damon is not guilty of felony murder because the felony murder rule only applies when the killing is caused strictly to facilitate the predicate felony, not for personal reasons.

**Answer:** (a)

**Explanation:** Under the felony murder rule, a death caused during the attempt to perpetrate a predicate felony (such as robbery) triggers first-degree murder liability. The killing occurred as part of the continuous transaction (res gestae) of the attempted robbery. The fact that the robbery was incomplete or that Damon had a secondary personal motive does not defeat the charge. (b) is wrong because an *attempted* predicate felony still triggers felony murder. (c) is wrong because the predicate is robbery, which has an independent felonious purpose from the killing itself, so it does not merge. (d) is wrong because deaths resulting from attempted predicate felonies are still graded as first-degree murder. (e) is wrong because strict causal facilitation is not required so long as the killing is part of the res gestae.

**Tags:** chapters: [14, 17], topics: [felony_murder, attempt, grading], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 17 (Attempts), grading-felony-murder-attempt

<!-- audit: MUST FIX
<check 1>: Fails. Option (a) justifies liability by referencing an "unintended death," but the prompt explicitly states Damon "shot him out of personal animus," which heavily implies an intentional killing rather than an accidental one.
<check 2>: Fails. A well-prepared student could argue for (e) because many jurisdictions require a logical nexus (the killing must be "in furtherance" of the felony). In those jurisdictions, a killing driven entirely by independent personal animus that does not facilitate the felony falls outside the felony murder rule. Furthermore, if Damon legally "abandoned" the attempt prior to the shot, the res gestae would have ended.
<check 3>: Fails. The explanation categorically dismisses the requirement for causal facilitation ("strict causal facilitation is not required so long as the killing is part of the res gestae"), which ignores the substantial jurisdictional split between pure temporal/spatial res gestae tests and those requiring an "in furtherance" causal/logical nexus.
<check 4>: Fails. The stem attributes the "abandonment" merely to a defense argument ("Damon's defense argues that because he abandoned...") rather than stating the objective facts of what Damon did, leaving it ambiguous whether he actually met the rigorous legal requirements for voluntary abandonment before pulling the trigger.
<check 5>: Fails. The question turns entirely on a classic jurisdictional split (whether felony murder requires an "in furtherance" nexus or merely temporal res gestae overlap) without stipulating the applicable rule in the stem.
<check 6>: Pass.
<check 7>: Pass. The interaction of attempt and felony murder grading maps to `grading-felony-murder-attempt`.
Recommended fix: Provide the jurisdiction's rule directly in the stem (e.g., "The jurisdiction's statute defines first-degree felony murder as any death, intended or unintended, occurring within the temporal and spatial res gestae of an attempted robbery, regardless of the killer's independent motives."). Additionally, remove the "unintended death" phrasing from option (a), as Damon's act of shooting out of animus was intentional.
-->

## Issue 2 — edge-case

**Q11.** Damon is charged with first-degree felony murder based on the attempted robbery of the stash house. Damon's defense argues that because he abandoned the robbery upon seeing Vic and shot him out of personal animus, the felony murder rule does not apply. How will a court likely rule?

(a) Damon is guilty of felony murder because the murder occurred during the *res gestae* of the attempted robbery, and an unintended death during an attempted predicate felony is graded upward as first-degree murder. <!-- correct -->
(b) Damon is not guilty of felony murder because he did not take any drugs or demand money, meaning the underlying felony was never completed.
(c) Damon is not guilty of felony murder under the merger doctrine, because his independent personal purpose to assault Vic means the assault merges with the homicide.
(d) Damon is guilty of felony murder, but only in the second degree, because the underlying predicate crime was merely an attempt rather than a completed felony.
(e) Damon is not guilty of felony murder because the felony murder rule only applies when the killing is caused strictly to facilitate the predicate felony, not for personal reasons.

**Answer:** (a)

**Explanation:** Under the felony murder rule, a death caused during the attempt to perpetrate a predicate felony (such as robbery) triggers first-degree murder liability. The killing occurred as part of the continuous transaction (res gestae) of the attempted robbery. The fact that the robbery was incomplete or that Damon had a secondary personal motive does not defeat the charge. (b) is wrong because an *attempted* predicate felony still triggers felony murder. (c) is wrong because the predicate is robbery, which has an independent felonious purpose from the killing itself, so it does not merge. (d) is wrong because deaths resulting from attempted predicate felonies are still graded as first-degree murder. (e) is wrong because strict causal facilitation is not required so long as the killing is part of the res gestae.

**Tags:** chapters: [14, 17], topics: [felony_murder, attempt, grading], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 17 (Attempts), grading-felony-murder-attempt

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: Option (a) uses the phrase "an unintended death." However, the facts explicitly establish that Damon *intentionally* shot Vic out of revenge ("shoots Vic dead, yelling..."). A sharp student will correctly note the killing was intentional and may eliminate the correct answer (a) because it seems to mischaracterize the facts or falsely imply felony murder only applies to accidental deaths.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: In option (a), change "an unintended death" to "any death" or simply "a death" so it does not contradict Damon's clear intent to kill.
-->

## Issue 3 — argpass-sonnet

**Q11.** Damon is charged with first-degree felony murder based on the attempted robbery of the stash house. Damon's defense argues that because he abandoned the robbery upon seeing Vic and shot him out of personal animus, the felony murder rule does not apply. How will a court likely rule?

(a) Damon is guilty of felony murder because the murder occurred during the *res gestae* of the attempted robbery, and an unintended death during an attempted predicate felony is graded upward as first-degree murder. <!-- correct -->
(b) Damon is not guilty of felony murder because he did not take any drugs or demand money, meaning the underlying felony was never completed.
(c) Damon is not guilty of felony murder under the merger doctrine, because his independent personal purpose to assault Vic means the assault merges with the homicide.
(d) Damon is guilty of felony murder, but only in the second degree, because the underlying predicate crime was merely an attempt rather than a completed felony.
(e) Damon is not guilty of felony murder because the felony murder rule only applies when the killing is caused strictly to facilitate the predicate felony, not for personal reasons.

**Answer:** (a)

**Explanation:** Under the felony murder rule, a death caused during the attempt to perpetrate a predicate felony (such as robbery) triggers first-degree murder liability. The killing occurred as part of the continuous transaction (res gestae) of the attempted robbery. The fact that the robbery was incomplete or that Damon had a secondary personal motive does not defeat the charge. (b) is wrong because an *attempted* predicate felony still triggers felony murder. (c) is wrong because the predicate is robbery, which has an independent felonious purpose from the killing itself, so it does not merge. (d) is wrong because deaths resulting from attempted predicate felonies are still graded as first-degree murder. (e) is wrong because strict causal facilitation is not required so long as the killing is part of the res gestae.

**Tags:** chapters: [14, 17], topics: [felony_murder, attempt, grading], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 17 (Attempts), grading-felony-murder-attempt

<!-- argument-pass: MUST FIX
(a) Argument-for: This correctly states the prevailing rule regarding the *res gestae* doctrine. Even if Damon formed an independent intent or decided to abandon the robbery, the shooting occurred during the continuous transaction of the attempted robbery. Furthermore, the rule correctly notes that attempted predicate felonies (like robbery) are graded as first-degree felony murder, making Damon fully liable.
(b) Argument-for: This option correctly identifies that the actus reus of a completed robbery requires taking and asportation. Because Damon never demanded money or took drugs, the robbery was never completed. In jurisdictions strictly construing the felony murder predicate to completed acts, this lack of completion absolutely bars the felony murder charge.
(c) Argument-for: This argument relies on the merger doctrine. Because Damon abandoned the robbery, his only active felonious intent at the moment of the shooting was the personal animus to assault Vic. This independent assaultive purpose completely merges with the resulting homicide, precluding a felony murder conviction and requiring the state to prove malice aforethought directly.
(d) Argument-for: This relies on the grading distinctions present in some jurisdictions for inchoate offenses. While a completed robbery automatically triggers first-degree felony murder under BARRK statutes, an *attempted* robbery represents a lesser grade of felony. Consequently, a death resulting from an attempt falls into the residuary catch-all of second-degree felony murder.
(e) Argument-for: This correctly applies the requirement for a logical nexus between the felony and the death. The felony murder rule requires the killing to be in furtherance of the felony. Since Damon abandoned the robbery and shot Vic solely for personal reasons, the killing was an independent, intervening act, failing the strict requirement for felonious facilitation.

Head-to-head: Option (a) correctly applies the *res gestae* rule, noting that temporal and spatial proximity suffices even if the original plan is abandoned. However, (a) justifies the conviction by referencing "an unintended death," whereas Damon's shooting of Vic out of "personal animus" clearly implies an intentional killing. This makes the keyed answer factually mismatched to the prompt. Option (b) fails because attempt is a sufficient predicate. Option (c) misapplies merger; while the assault might merge, the attempted robbery does not. Option (d) fails because an attempt to commit an enumerated felony like robbery still triggers first-degree murder. Option (e) fails because strict causal facilitation is not required under the *res gestae* standard. Because the keyed answer (a) includes a confusing and potentially factually false premise ("an unintended death") to justify an intentional shooting, the question requires a fix.

Falsifiable claim per distractor:
- (b): "...meaning the underlying felony was never completed." — wrong because completion of the underlying felony is categorically not required; an attempted predicate felony automatically suffices to trigger the felony murder rule.
- (c): "...because his independent personal purpose to assault Vic means the assault merges with the homicide." — wrong because, regardless of whether the assault merges, the attempted robbery remains an independent, non-merging predicate felony that sustains the charge.
- (d): "...but only in the second degree, because the underlying predicate crime was merely an attempt..." — wrong because deaths resulting from attempted enumerated felonies are automatically graded as first-degree murder, not categorically relegated to second degree.
- (e): "...because the felony murder rule only applies when the killing is caused strictly to facilitate the predicate felony..." — wrong because "strictly to facilitate" is a false absolute; killings during the *res gestae* trigger the rule regardless of whether they strictly facilitate the felony.

Recommended fix: In option (a), change "an unintended death during an attempted predicate felony" to "a death resulting from an attempted predicate felony" or "even an unintended death during an attempted predicate felony".
-->

## Issue 4 — argpass-opus

**Q11.** Damon is charged with first-degree felony murder based on the attempted robbery of the stash house. Damon's defense argues that because he abandoned the robbery upon seeing Vic and shot him out of personal animus, the felony murder rule does not apply. How will a court likely rule?

(a) Damon is guilty of felony murder because the murder occurred during the *res gestae* of the attempted robbery, and an unintended death during an attempted predicate felony is graded upward as first-degree murder. <!-- correct -->
(b) Damon is not guilty of felony murder because he did not take any drugs or demand money, meaning the underlying felony was never completed.
(c) Damon is not guilty of felony murder under the merger doctrine, because his independent personal purpose to assault Vic means the assault merges with the homicide.
(d) Damon is guilty of felony murder, but only in the second degree, because the underlying predicate crime was merely an attempt rather than a completed felony.
(e) Damon is not guilty of felony murder because the felony murder rule only applies when the killing is caused strictly to facilitate the predicate felony, not for personal reasons.

**Answer:** (a)

**Explanation:** Under the felony murder rule, a death caused during the attempt to perpetrate a predicate felony (such as robbery) triggers first-degree murder liability. The killing occurred as part of the continuous transaction (res gestae) of the attempted robbery. The fact that the robbery was incomplete or that Damon had a secondary personal motive does not defeat the charge. (b) is wrong because an *attempted* predicate felony still triggers felony murder. (c) is wrong because the predicate is robbery, which has an independent felonious purpose from the killing itself, so it does not merge. (d) is wrong because deaths resulting from attempted predicate felonies are still graded as first-degree murder. (e) is wrong because strict causal facilitation is not required so long as the killing is part of the res gestae.

**Tags:** chapters: [14, 17], topics: [felony_murder, attempt, grading], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 17 (Attempts), grading-felony-murder-attempt

<!-- argument-pass: SHOULD FIX
(a) Argument-for: The *res gestae* doctrine treats the attempted robbery and the killing as a continuous transaction since they occurred at the same location. First-degree felony murder statutes (such as those based on enumerated BARRK crimes) explicitly elevate homicides committed during both completed and attempted predicate felonies. Thus, Damon is guilty of first-degree felony murder despite his personal animus.
(b) Argument-for: A student could argue that the actus reus for robbery requires the taking of property or a direct demand. Because Damon did neither, the felony was incomplete. If a jurisdiction strictly construed felony murder to require a completed offense, Damon would be not guilty. 
(c) Argument-for: Under the merger doctrine (*Ireland* rule), an assault that results in death merges with the homicide and cannot serve as a felony murder predicate. If Damon completely abandoned the robbery before shooting, a student could argue his only remaining felonious intent was assault out of personal animus, which merges and precludes felony murder liability.
(d) Argument-for: Some grading schemes distinguish between completed crimes and attempts. A student might reason that while a completed robbery triggers first-degree felony murder, an attempted robbery is a lesser offense that only triggers a catch-all second-degree felony murder charge.
(e) Argument-for: The "in furtherance" test in some jurisdictions requires a logical nexus between the felony and the killing. If Damon shot Vic entirely out of personal animus rather than to advance the robbery, a student could argue that the strict facilitation requirement is not met and the felony murder rule does not apply.

Head-to-head: Option (a) correctly applies the *res gestae* rule: the attempted robbery and the killing occurred during the same transaction, and attempts to commit enumerated felonies like robbery categorically trigger first-degree felony murder. However, (a) awkwardly refers to "an unintended death," which creates tension with the fact that Damon shot Vic out of "personal animus" (implying an intentional killing). Option (b) fails because attempted enumerated felonies are legally sufficient for felony murder. Option (c) fails because the charge is predicated on attempted robbery, which has an independent felonious purpose (property deprivation) that does not merge, rendering the assault merger irrelevant. Option (d) incorrectly states attempts are categorically downgraded to second degree; attempts of BARRK crimes remain first-degree. Option (e) uses the easily falsifiable absolute "strictly to facilitate," ignoring that temporal/spatial proximity generally satisfies the *res gestae* requirement regardless of mixed motives.

Falsifiable claim per distractor:
- (b): "meaning the underlying felony was never completed [and therefore he is not guilty]" — wrong because attempted predicate felonies are categorically sufficient to trigger the felony murder rule.
- (c): "his independent personal purpose to assault Vic means the assault merges" — wrong because the felony murder charge is explicitly predicated on the attempted robbery, which has an independent purpose and does not merge.
- (d): "only in the second degree, because the underlying predicate crime was merely an attempt" — wrong because first-degree felony murder statutes explicitly encompass attempts to commit enumerated felonies.
- (e): "only applies when the killing is caused strictly to facilitate the predicate felony" — wrong because strict causal facilitation is not universally required; a killing within the *res gestae* is sufficient even with personal motives.

Recommended fix: In (a), change "an unintended death" to "a death" or "even an unintended death" to avoid contradicting the fact pattern's implication that Damon intentionally shot Vic out of personal animus.
-->
