# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q4.** Assume the prosecution charges Marlowe with felony murder for Greggs's death, using his unpermitted chemical storage—a strict-liability felony under a state public welfare statute—as the predicate offense. In a jurisdiction following the modern common law approach, is this charge likely to succeed?

(a) Yes, because a strict-liability regulatory felony completely substitutes for the malice aforethought required for a common law felony-murder conviction.
(b) Yes, because the storage of volatile chemicals without a permit is an inherently dangerous act that proximately caused the lethal chemical fire.
(c) No, because courts generally prohibit the use of strict-liability regulatory or public welfare felonies as predicate offenses for the felony-murder rule. <!-- correct -->
(d) No, because the felony-murder rule only applies when the defendant is physically present at the scene of the underlying felony when the death occurs.
(e) No, because the death of a first responder is categorically classified as a dependent intervening cause that breaks the causal chain of the predicate felony.

**Answer:** (c)

**Explanation:** The modern common law heavily restricts the felony-murder rule to prevent unjust applications. Courts universally reject using strict-liability regulatory or *malum prohibitum* offenses (like unpermitted storage) as felony-murder predicates because they lack the inherent blameworthiness required to fairly impute malice. (a) fails because strict-liability crimes cannot supply the requisite malice for murder. (b) fails because failing to file a permit is a regulatory omission, not a life-threatening act in the abstract. (d) fails because felony murder does not require physical presence at the scene (e.g., getaway drivers). (e) fails because first-responder deaths are generally foreseeable dependent causes that preserve the causal chain, not break it.

**Tags:** chapters: [14], topics: [felony murder, strict liability, limitations], difficulty: medium, cognitive: application

**Grounding:** Chapter 14 (mm-strict-liability-structure; regulatory-gap)

<!-- audit: MUST FIX
check 1: fails. The limitation on felony murder predicates under modern common law relies on the "inherently dangerous felony" test (elements/abstract vs. facts approach) and merger doctrine, not a categorical rule against malum prohibitum offenses. The malum in se vs. malum prohibitum distinction is a limitation on Misdemeanor Manslaughter.
check 2: pass. 
check 3: fails. The explanation explicitly conflates Misdemeanor Manslaughter limitations with Felony Murder. Additionally, the author appears to have misunderstood the `strict-liability-substitution` doctrine, which describes how the FM rule *itself* functions as strict liability for homicide (substituting the felony's mens rea for malice), rather than addressing whether the predicate offense itself can be strict liability.
check 4: pass.
check 5: pass.
check 6: pass.
check 7: fails. Coverage mismatch. The author grounded the question in `mm-strict-liability-structure`, an explicit Misdemeanor Manslaughter doctrine (denoted by the `mm-` prefix in the chapter map tags), but wrote a question about Felony Murder.
Recommended fix: Either change the charge to Misdemeanor Manslaughter (and the predicate to a misdemeanor) to properly test the malum prohibitum / strict liability limitations, OR keep the charge as Felony Murder but rewrite the options and explanation to test FM's actual limitation (e.g., how the unpermitted storage predicate fails the inherently dangerous felony test in the abstract).
-->

## Issue 2 — edge-case

**Q4.** Assume the prosecution charges Marlowe with felony murder for Greggs's death, using his unpermitted chemical storage—a strict-liability felony under a state public welfare statute—as the predicate offense. In a jurisdiction following the modern common law approach, is this charge likely to succeed?

(a) Yes, because a strict-liability regulatory felony completely substitutes for the malice aforethought required for a common law felony-murder conviction.
(b) Yes, because the storage of volatile chemicals without a permit is an inherently dangerous act that proximately caused the lethal chemical fire.
(c) No, because courts generally prohibit the use of strict-liability regulatory or public welfare felonies as predicate offenses for the felony-murder rule. <!-- correct -->
(d) No, because the felony-murder rule only applies when the defendant is physically present at the scene of the underlying felony when the death occurs.
(e) No, because the death of a first responder is categorically classified as a dependent intervening cause that breaks the causal chain of the predicate felony.

**Answer:** (c)

**Explanation:** The modern common law heavily restricts the felony-murder rule to prevent unjust applications. Courts universally reject using strict-liability regulatory or *malum prohibitum* offenses (like unpermitted storage) as felony-murder predicates because they lack the inherent blameworthiness required to fairly impute malice. (a) fails because strict-liability crimes cannot supply the requisite malice for murder. (b) fails because failing to file a permit is a regulatory omission, not a life-threatening act in the abstract. (d) fails because felony murder does not require physical presence at the scene (e.g., getaway drivers). (e) fails because first-responder deaths are generally foreseeable dependent causes that preserve the causal chain, not break it.

**Tags:** chapters: [14], topics: [felony murder, strict liability, limitations], difficulty: medium, cognitive: application

**Grounding:** Chapter 14 (mm-strict-liability-structure; regulatory-gap)

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Q4 explicitly declares the unpermitted storage violation to be "a strict-liability felony under a state public welfare statute." This directly spoils Q7, which tests the student on evaluating whether that exact statute qualifies as a public-welfare offense. 
Recommended fix: Frame the classification as a hypothetical assumption for this specific question to avoid establishing it as an objective fact for the whole exam. Change the prompt to: "Assume for the purposes of this question that Marlowe's unpermitted chemical storage is classified as a strict-liability regulatory felony. If the prosecution uses this violation as the predicate offense for felony murder..."
-->

## Issue 3 — argpass-sonnet

**Q4.** Assume the prosecution charges Marlowe with felony murder for Greggs's death, using his unpermitted chemical storage—a strict-liability felony under a state public welfare statute—as the predicate offense. In a jurisdiction following the modern common law approach, is this charge likely to succeed?

(a) Yes, because a strict-liability regulatory felony completely substitutes for the malice aforethought required for a common law felony-murder conviction.
(b) Yes, because the storage of volatile chemicals without a permit is an inherently dangerous act that proximately caused the lethal chemical fire.
(c) No, because courts generally prohibit the use of strict-liability regulatory or public welfare felonies as predicate offenses for the felony-murder rule. <!-- correct -->
(d) No, because the felony-murder rule only applies when the defendant is physically present at the scene of the underlying felony when the death occurs.
(e) No, because the death of a first responder is categorically classified as a dependent intervening cause that breaks the causal chain of the predicate felony.

**Answer:** (c)

**Explanation:** The modern common law heavily restricts the felony-murder rule to prevent unjust applications. Courts universally reject using strict-liability regulatory or *malum prohibitum* offenses (like unpermitted storage) as felony-murder predicates because they lack the inherent blameworthiness required to fairly impute malice. (a) fails because strict-liability crimes cannot supply the requisite malice for murder. (b) fails because failing to file a permit is a regulatory omission, not a life-threatening act in the abstract. (d) fails because felony murder does not require physical presence at the scene (e.g., getaway drivers). (e) fails because first-responder deaths are generally foreseeable dependent causes that preserve the causal chain, not break it.

**Tags:** chapters: [14], topics: [felony murder, strict liability, limitations], difficulty: medium, cognitive: application

**Grounding:** Chapter 14 (mm-strict-liability-structure; regulatory-gap)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that the fundamental purpose of the felony-murder rule is to hold individuals strictly liable for deaths occurring during felonies. Because the state legislature has explicitly defined unpermitted chemical storage as a felony, it satisfies the basic structural requirement of the doctrine. Therefore, one could reason that this statutory classification completely substitutes for malice aforethought, enabling the charge to succeed regardless of the predicate's regulatory nature.
(b) Argument-for: A student could argue that modern courts apply the "inherently dangerous felony" limitation by looking at the specific acts committed rather than the offense in the abstract. Storing volatile chemicals without proper safety oversight is factually a highly dangerous activity that directly threatens human life. Under this factual approach, a student could conclude that the unpermitted storage constitutes an inherently dangerous act that proximately caused the fire, rendering the felony-murder charge appropriate.
(c) Argument-for: A student could argue that modern common law jurisdictions heavily restrict the felony-murder rule to avoid disproportionate punishment for relatively minor offenses. The "inherently dangerous felony" limitation requires the predicate offense to carry an inherent risk to human life and intrinsic moral blameworthiness. Purely regulatory, *malum prohibitum*, or strict-liability public welfare felonies fundamentally lack the requisite inherent danger or culpable intent in the abstract, meaning courts prohibit their use as predicates.
(d) Argument-for: A student could argue that the res gestae requirement of felony murder strictly limits liability to the immediate temporal and geographical zone of the crime. To prevent endless, remote causal liability for regulatory offenses occurring off-site, the law requires a tight nexus between the felon's actions and the resulting death. Thus, a student might reason that the felony-murder rule only applies when the defendant is physically present at the scene, shielding Marlowe from liability.
(e) Argument-for: A student could argue that criminal causation requires avoiding the attribution of deaths to remote or superseding intervening actors. First responders assume the risk of their duties, and their deliberate intervention into a dangerous situation can be viewed as superseding the original felonious act. A student could therefore conclude that the death of a first responder is categorically classified as an intervening cause that breaks the causal chain.

Head-to-head: Option (c) is clearly the correct statement of modern common law doctrine regarding strict-liability predicates. Option (a) is thoroughly falsifiable because strict-liability offenses do *not* substitute for malice aforethought in modern jurisdictions. Option (d) contains an explicitly falsifiable absolute ("only applies when the defendant is physically present"), which is legally false due to accomplice and co-felon liability rules. Option (e) uses an absolute ("categorically classified") and asserts a glaring doctrinal contradiction: "dependent" intervening causes typically *preserve* the causal chain rather than breaking it. However, Option (b) lacks an absolute locking word (like "per se" or "automatically"), making its claim that the storage "is an inherently dangerous act" potentially vulnerable to arguments under the "factual / as-committed" inherently dangerous test used in some states, risking a mixed question of fact and law rather than an explicitly false legal claim.

Falsifiable claim per distractor:
- (a): "completely substitutes for the malice aforethought required" — wrong because modern common law categorically rejects strict-liability/public-welfare felonies as predicates capable of substituting for malice.
- (b): "is an inherently dangerous act" — wrong because courts view the failure to obtain a permit as a regulatory omission rather than an inherently dangerous act, but this distractor lacks an absolute modifier to lock it as an explicitly false legal rule.
- (d): "only applies when the defendant is physically present" — wrong because felony murder routinely applies to off-site actors, such as masterminds or getaway drivers, under complicity theories.
- (e): "categorically classified as a dependent intervening cause that breaks the causal chain" — wrong because it misstates doctrine; dependent intervening causes (like foreseeable rescue attempts) preserve rather than break causal chains.

Recommended fix: Add an absolute locking phrase to option (b) to ensure it asserts a falsifiable legal claim rather than a debatable factual one. Change (b) to: "Yes, because any unpermitted storage of volatile chemicals is per se an inherently dangerous act that proximately caused the lethal chemical fire."
-->

## Issue 4 — argpass-opus

**Q4.** Assume the prosecution charges Marlowe with felony murder for Greggs's death, using his unpermitted chemical storage—a strict-liability felony under a state public welfare statute—as the predicate offense. In a jurisdiction following the modern common law approach, is this charge likely to succeed?

(a) Yes, because a strict-liability regulatory felony completely substitutes for the malice aforethought required for a common law felony-murder conviction.
(b) Yes, because the storage of volatile chemicals without a permit is an inherently dangerous act that proximately caused the lethal chemical fire.
(c) No, because courts generally prohibit the use of strict-liability regulatory or public welfare felonies as predicate offenses for the felony-murder rule. <!-- correct -->
(d) No, because the felony-murder rule only applies when the defendant is physically present at the scene of the underlying felony when the death occurs.
(e) No, because the death of a first responder is categorically classified as a dependent intervening cause that breaks the causal chain of the predicate felony.

**Answer:** (c)

**Explanation:** The modern common law heavily restricts the felony-murder rule to prevent unjust applications. Courts universally reject using strict-liability regulatory or *malum prohibitum* offenses (like unpermitted storage) as felony-murder predicates because they lack the inherent blameworthiness required to fairly impute malice. (a) fails because strict-liability crimes cannot supply the requisite malice for murder. (b) fails because failing to file a permit is a regulatory omission, not a life-threatening act in the abstract. (d) fails because felony murder does not require physical presence at the scene (e.g., getaway drivers). (e) fails because first-responder deaths are generally foreseeable dependent causes that preserve the causal chain, not break it.

**Tags:** chapters: [14], topics: [felony murder, strict liability, limitations], difficulty: medium, cognitive: application

**Grounding:** Chapter 14 (mm-strict-liability-structure; regulatory-gap)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could choose this option by relying on the traditional, unrestricted definition of felony murder, which historically allowed any felony to serve as a predicate. Since the statute defines the unpermitted storage as a felony, the student might reason that its strict-liability nature is irrelevant because the felony-murder rule is specifically designed to substitute the commission of a felony for malice aforethought.
(b) Argument-for: A student might select this option by focusing on the "inherently dangerous felony" limitation and concluding that storing volatile chemicals is factually highly dangerous. The student could argue that because the chemicals are volatile and actually caused a lethal fire, the act satisfies the inherent danger test, making it a valid predicate offense regardless of its regulatory nature.
(c) Argument-for: This is the correct answer. The modern common law approach heavily restricts the felony-murder rule to prevent disproportionate punishment. As part of this restriction, courts generally hold that strict-liability or public welfare offenses (malum prohibitum) cannot serve as predicate felonies because they lack the inherent blameworthiness and criminal intent required to fairly impute malice aforethought.
(d) Argument-for: A student might choose this option if they misremember the spatial and temporal limits (res gestae) of the felony-murder doctrine. They might mistakenly believe that to establish a direct causal nexus—especially in cases involving passive regulatory omissions like storage—the defendant must be physically present at the scene when the death actually occurs.
(e) Argument-for: A student could select this option by confusing the concepts of proximate cause and intervening causes. They might incorrectly recall the "firefighter's rule" from torts or mistakenly believe that a first responder's voluntary entrance into a dangerous situation acts as a superseding event that definitively cuts off criminal liability.

Head-to-head: Option (c) is clearly the strongest because it correctly applies the modern common law limitation barring strict-liability public welfare offenses as felony-murder predicates. Option (a) explicitly contradicts this limitation by claiming strict-liability completely substitutes for malice. Option (d) invents a non-existent physical presence requirement, ignoring accomplice liability and standard res gestae rules. Option (e) uses contradictory legal terminology, asserting that a "dependent" cause breaks the causal chain (dependent causes preserve it; superseding causes break it). Option (b) is the most tempting distractor because volatile chemicals sound dangerous factually, but legally fails because courts assess inherent danger in the abstract based on statutory elements (where failing to obtain a permit is merely a regulatory omission). However, (b) lacks an absolute word to firmly lock its falsifiable claim, making it slightly softer than ideal.

Falsifiable claim per distractor:
- (a): "completely substitutes for the malice aforethought" — wrong because modern courts restrict felony-murder predicates and categorically reject strict-liability regulatory offenses from substituting for malice.
- (b): "is an inherently dangerous act" — wrong because modern courts assess inherent danger in the abstract based on statutory elements (unpermitted storage is a regulatory omission, not inherently dangerous), but the option currently lacks an absolute trigger word.
- (d): "only applies when the defendant is physically present" — wrong because felony-murder liability regularly extends to absent co-felons or perpetrators who have left the scene (e.g., getaway drivers), provided the death occurs within the res gestae.
- (e): "categorically classified as a dependent intervening cause that breaks the causal chain" — wrong because dependent intervening causes (like a first responder's foreseeable reaction) *preserve* the causal chain; it is *superseding* (independent) causes that break it.

Recommended fix: Edit (b) to include absolute phrasing to lock in the false claim. Change (b) to: "Yes, because any felony resulting in a lethal chemical fire automatically satisfies the inherently dangerous act requirement."
-->
