# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q9.** Leo is charged as an accomplice to Dom's attempted armed hijacking. In a jurisdiction requiring that an accomplice act with the strict purpose of promoting the underlying offense, is Leo guilty?

(a) Yes, because providing a ride with actual knowledge of Dom's criminal plan establishes the required specific intent mens rea for standard accomplice liability.
(b) Yes, because accepting the $500 premium payment gave Leo a financial stake in the venture, supporting an inference that his purpose was to facilitate the crime. <!-- correct -->
(c) No, because Leo explicitly refused to help plan the operation, which completely negates the purpose requirement and shields him from any accomplice liability.
(d) No, because merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance to satisfy the actus reus of accomplice liability.
(e) No, because mere presence at the scene of the crime is legally insufficient, and an accomplice must actively participate in the execution of the hijacking itself.

**Answer:** (b)

**Explanation:** Accomplice liability typically requires the purpose to promote or facilitate the crime. While mere knowledge is insufficient, courts (as in *People v. Lauria*) hold that purpose can be inferred if the provider of services charges a premium or has a financial stake in the venture. (b) is correct because Leo was paid $500 specifically for a ride to a hijacking, constituting a premium that permits the inference of purpose. (a) fails because in a strict purpose jurisdiction, mere knowledge of the crime without a stake is insufficient. (c) fails because refusing to plan does not negate purpose if he simultaneously takes money to drive the getaway car to facilitate the crime. (d) fails because driving a getaway car is a classic form of physical assistance satisfying the actus reus. (e) fails because Leo was not merely present; he provided transportation and waited as the designated getaway driver.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: mr-purpose-not-knowledge

<!-- audit: MUST FIX
check 1: pass (the legal rule derived from *Lauria* regarding the inference of purpose via a financial premium is correctly applied)
check 2: pass (distractors are well-calibrated misapplications of actus reus and mens rea standards, provided the facts were present)
check 3: pass (the explanation correctly aligns with the doctrine mapped to `mr-purpose-not-knowledge` and `lauria-three-inferences`)
check 4: MUST FIX (The stem is entirely missing the factual scenario. It leaps straight to the call of the question without establishing that Leo drove the car, accepted a $500 premium, or refused to help plan the operation. Students have no facts to apply the law to.)
check 5: pass (the jurisdiction is cleanly stipulated as a "strict purpose" jurisdiction)
check 6: pass (attempted hijacking does not violate the excluded-topic boundaries)
check 7: pass (doctrine is securely grounded in Chapter 18/19 maps under `lauria-three-inferences` and `mr-purpose-not-knowledge`)
Recommended fix: Add the missing fact pattern to the stem. For example: "Dom plans an armed hijacking and asks Leo to drive the getaway car. Leo explicitly refuses to help plan the operation but agrees to wait in an idling vehicle and drive Dom away afterward, provided Dom pays him a $500 premium—far above his normal rate. Leo is charged..."
-->

## Issue 2 — edge-case

**Q9.** Leo is charged as an accomplice to Dom's attempted armed hijacking. In a jurisdiction requiring that an accomplice act with the strict purpose of promoting the underlying offense, is Leo guilty?

(a) Yes, because providing a ride with actual knowledge of Dom's criminal plan establishes the required specific intent mens rea for standard accomplice liability.
(b) Yes, because accepting the $500 premium payment gave Leo a financial stake in the venture, supporting an inference that his purpose was to facilitate the crime. <!-- correct -->
(c) No, because Leo explicitly refused to help plan the operation, which completely negates the purpose requirement and shields him from any accomplice liability.
(d) No, because merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance to satisfy the actus reus of accomplice liability.
(e) No, because mere presence at the scene of the crime is legally insufficient, and an accomplice must actively participate in the execution of the hijacking itself.

**Answer:** (b)

**Explanation:** Accomplice liability typically requires the purpose to promote or facilitate the crime. While mere knowledge is insufficient, courts (as in *People v. Lauria*) hold that purpose can be inferred if the provider of services charges a premium or has a financial stake in the venture. (b) is correct because Leo was paid $500 specifically for a ride to a hijacking, constituting a premium that permits the inference of purpose. (a) fails because in a strict purpose jurisdiction, mere knowledge of the crime without a stake is insufficient. (c) fails because refusing to plan does not negate purpose if he simultaneously takes money to drive the getaway car to facilitate the crime. (d) fails because driving a getaway car is a classic form of physical assistance satisfying the actus reus. (e) fails because Leo was not merely present; he provided transportation and waited as the designated getaway driver.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: mr-purpose-not-knowledge

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: Derivative accomplice liability requires the principal to have actually committed the offense. Dom's attempt is legally borderline (he never touched the truck and fled when he saw police). If Dom's actions fall short of attempt, Leo cannot be guilty as an accomplice to attempt.
3. Cross-Question Spoilers: Q8 explicitly tests whether Dom's actions satisfy the actus reus for attempt (proximity vs. substantial step), and another question tests Dom's abandonment. Because Dom's guilt for the underlying attempt is highly debatable and actively tested elsewhere in the exam, this question cannot force a definitive "Yes" for Leo's guilt without stipulating that the principal's crime was legally established.
Recommended fix: Add "Assume Dom's actions legally constitute attempted armed hijacking." to the end of the question stem to isolate the mens rea analysis.
-->

## Issue 3 — argpass-sonnet

**Q9.** Leo is charged as an accomplice to Dom's attempted armed hijacking. In a jurisdiction requiring that an accomplice act with the strict purpose of promoting the underlying offense, is Leo guilty?

(a) Yes, because providing a ride with actual knowledge of Dom's criminal plan establishes the required specific intent mens rea for standard accomplice liability.
(b) Yes, because accepting the $500 premium payment gave Leo a financial stake in the venture, supporting an inference that his purpose was to facilitate the crime. <!-- correct -->
(c) No, because Leo explicitly refused to help plan the operation, which completely negates the purpose requirement and shields him from any accomplice liability.
(d) No, because merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance to satisfy the actus reus of accomplice liability.
(e) No, because mere presence at the scene of the crime is legally insufficient, and an accomplice must actively participate in the execution of the hijacking itself.

**Answer:** (b)

**Explanation:** Accomplice liability typically requires the purpose to promote or facilitate the crime. While mere knowledge is insufficient, courts (as in *People v. Lauria*) hold that purpose can be inferred if the provider of services charges a premium or has a financial stake in the venture. (b) is correct because Leo was paid $500 specifically for a ride to a hijacking, constituting a premium that permits the inference of purpose. (a) fails because in a strict purpose jurisdiction, mere knowledge of the crime without a stake is insufficient. (c) fails because refusing to plan does not negate purpose if he simultaneously takes money to drive the getaway car to facilitate the crime. (d) fails because driving a getaway car is a classic form of physical assistance satisfying the actus reus. (e) fails because Leo was not merely present; he provided transportation and waited as the designated getaway driver.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: mr-purpose-not-knowledge

<!-- argument-pass: MUST FIX
(a) Argument-for: Leo provided a ride with actual knowledge of Dom's criminal plan. In some minority interpretations (e.g., *Fountain* or *Luparello*), "knowing" facilitation of a highly serious felony can sometimes blur into purpose or be deemed legally sufficient to establish accomplice liability. A student could argue that actual knowledge of a severe crime like armed hijacking automatically establishes the necessary mens rea.
(b) Argument-for: Leo accepted a $500 premium payment for his services. Under the widely accepted doctrine of *People v. Lauria*, when a defendant provides lawful goods or services but charges a premium knowing they will be used for a crime, the jury can infer that the defendant had the specific purpose to facilitate the crime. This financial stake elevates his mens rea from mere knowledge to the required strict purpose.
(c) Argument-for: Accomplice liability requires the strict purpose to promote or facilitate the offense. Leo explicitly refused to help plan the operation. This explicit refusal serves as factual evidence demonstrating a lack of the requisite specific intent or purpose to see the crime succeed, acting as a negation of the mens rea element and shielding him from liability under a strict purpose standard.
(d) Argument-for: Accomplice liability actus reus requires actual assistance or encouragement that genuinely aids the principal. Merely sitting in an idling car without participating in the primary conduct of the hijacking could be characterized as failing to provide sufficient physical assistance, meaning the actus reus is not met.
(e) Argument-for: Mere presence at the scene of a crime is legally insufficient to establish accomplice liability. Since Leo did not actively participate in the execution of the hijacking itself, his waiting in the car could be construed as mere presence, failing to satisfy the active participation requirement mandated for conviction.

Head-to-head: The keyed answer (b) correctly applies the *Lauria* standard that a financial stake/premium permits an inference of purpose. The distractors feature properly locked falsifiable claims. However, this question is a MUST FIX because the question stem is entirely missing the fact pattern! It mentions Leo is charged, but omits that he provided a ride, was paid $500, refused to plan, or waited in the car. Without the facts, the question is unanswerable. 

Falsifiable claim per distractor:
- (a): "establishes the required specific intent mens rea" — wrong because in a strict purpose jurisdiction, mere knowledge alone categorically does not establish specific intent (purpose) without an additional factor like a stake in the venture.
- (c): "completely negates the purpose requirement and shields him from any accomplice liability" — wrong because refusing to plan does not completely negate purpose if the defendant then purposefully aids the crime (e.g., by driving the getaway car for a premium).
- (d): "merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance" — wrong because driving a getaway vehicle is categorically established as sufficient physical assistance (actus reus) for accomplice liability.
- (e): "an accomplice must actively participate in the execution of the hijacking itself" — wrong because an accomplice does not have to actively participate in the actual execution of the principal act; rendering aid before or during the escape is legally sufficient.

Recommended fix: Insert the missing fact pattern into the question stem. Change the stem to: "Dom plans to commit an armed hijacking. Leo explicitly refuses to help plan the operation, but he agrees to drive the getaway vehicle and wait in an idling car after Dom offers him a $500 premium payment for the ride. Leo is subsequently charged as an accomplice. In a jurisdiction requiring that an accomplice act with the strict purpose of promoting the underlying offense, is Leo guilty?"
-->

## Issue 4 — argpass-opus

**Q9.** Leo is charged as an accomplice to Dom's attempted armed hijacking. In a jurisdiction requiring that an accomplice act with the strict purpose of promoting the underlying offense, is Leo guilty?

(a) Yes, because providing a ride with actual knowledge of Dom's criminal plan establishes the required specific intent mens rea for standard accomplice liability.
(b) Yes, because accepting the $500 premium payment gave Leo a financial stake in the venture, supporting an inference that his purpose was to facilitate the crime. <!-- correct -->
(c) No, because Leo explicitly refused to help plan the operation, which completely negates the purpose requirement and shields him from any accomplice liability.
(d) No, because merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance to satisfy the actus reus of accomplice liability.
(e) No, because mere presence at the scene of the crime is legally insufficient, and an accomplice must actively participate in the execution of the hijacking itself.

**Answer:** (b)

**Explanation:** Accomplice liability typically requires the purpose to promote or facilitate the crime. While mere knowledge is insufficient, courts (as in *People v. Lauria*) hold that purpose can be inferred if the provider of services charges a premium or has a financial stake in the venture. (b) is correct because Leo was paid $500 specifically for a ride to a hijacking, constituting a premium that permits the inference of purpose. (a) fails because in a strict purpose jurisdiction, mere knowledge of the crime without a stake is insufficient. (c) fails because refusing to plan does not negate purpose if he simultaneously takes money to drive the getaway car to facilitate the crime. (d) fails because driving a getaway car is a classic form of physical assistance satisfying the actus reus. (e) fails because Leo was not merely present; he provided transportation and waited as the designated getaway driver.

**Tags:** chapters: [18], topics: [accomplice liability, mens rea, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: mr-purpose-not-knowledge

<!-- argument-pass: MUST FIX
(a) Argument-for: In some jurisdictions, the line between knowledge and purpose blurs for exceptionally serious crimes like armed hijacking. A student might argue that under doctrines derived from cases like *Fountain*, actual knowledge of a violently dangerous felony is enough to establish the requisite mens rea, even in a jurisdiction that generally requires purpose. Thus, providing a ride while actually knowing of the hijacking could be seen as legally satisfying the specific intent for standard accomplice liability.
(b) Argument-for: A student could rely on the *Lauria* standard, which addresses the mens rea of service providers in strict purpose jurisdictions. While mere knowledge is insufficient, *Lauria* holds that purpose can be inferred if the provider has a financial stake in the venture, such as charging a premium. Accepting a $500 premium for a single ride strongly implies a financial stake, legally supporting the inference that Leo's purpose was to facilitate the crime's success.
(c) Argument-for: A student might assert that strict purpose requires a conscious object to see the crime succeed, which is negated by explicitly distancing oneself from the crime's preparation. Leo's explicit refusal to help plan the operation demonstrates a lack of true purpose or investment in the hijacking's success. Therefore, this refusal factually and completely negates the strict purpose requirement, shielding him from liability.
(d) Argument-for: A student could argue that the actus reus of accomplice liability requires actual assistance that contributes to the crime. If the hijacking was only "attempted" and Leo merely sat in an idling car without successfully driving Dom away, his physical acts might be viewed as mere preparation or insufficient assistance. Therefore, driving the car to the scene and waiting does not satisfy the actus reus.
(e) Argument-for: A student could argue that accomplice liability distinguishes between actual aid and mere presence. Waiting in a car outside the scene could be mischaracterized as "mere presence," which is legally insufficient. The student might conclude that unless Leo actively participated in the execution of the hijacking elements (e.g., holding the weapon), his conduct does not rise to the level of accomplice actus reus.

Head-to-head: Option (b) correctly applies *Lauria*, identifying that a premium payment creates a financial stake allowing an inference of purpose. Option (a) makes the legally false claim that mere actual knowledge establishes specific intent mens rea categorically in a strict-purpose jurisdiction. Option (c) falsely claims that a refusal to plan "completely negates" purpose, ignoring that taking a premium and driving the getaway car overrides this. Option (d) falsely asserts that driving a getaway car is insufficient physical assistance. Option (e) includes the demonstrably false claim that an accomplice "must actively participate in the execution of the hijacking itself." However, the question contains a critical structural flaw: the entire fact pattern is missing from the question stem. The student must improperly infer the facts (a $500 premium, driving the getaway car, refusing to plan) entirely from the answer choices, rendering the question unanswerable as drafted.

Falsifiable claim per distractor:
- (a): "providing a ride with actual knowledge of Dom's criminal plan establishes the required specific intent mens rea" — wrong because in a strict purpose jurisdiction, actual knowledge without more (such as a stake in the venture) does not establish purpose.
- (c): "which completely negates the purpose requirement" — wrong because refusing to plan does not categorically negate the purpose requirement if the defendant otherwise manifests purpose by charging a premium and providing aid.
- (d): "merely driving the getaway vehicle while waiting in an idling car does not constitute sufficient physical assistance" — wrong because waiting in an idling getaway car is a classic, universally recognized and legally sufficient actus reus for accomplice liability.
- (e): "an accomplice must actively participate in the execution of the hijacking itself" — wrong because an accomplice does not need to participate in the actus reus of the underlying offense; aiding from the periphery (e.g., acting as a getaway driver) is completely sufficient.

Recommended fix: Insert the missing facts into the question stem. For example: "Dom plans an armed hijacking and asks Leo to drive the getaway car. Leo explicitly refuses to help plan the operation but agrees to drive the car and wait idling at the scene in exchange for a $500 premium payment, which Dom pays. Leo fully knows of Dom's plan and drives Dom as agreed. Leo is charged..."
-->
