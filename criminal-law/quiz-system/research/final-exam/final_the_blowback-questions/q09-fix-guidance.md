# Fix Guidance for q09

The QA pipeline flagged this question. Rewrite `q09.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

```
<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The question applies the "vendor" exception (mere knowledge + flat fee = no purpose) to negate specific intent. However, this doctrine (from cases like *Peoni* or *Lauria*) applies to providers of ordinary, legitimate goods or services. Leo is actively serving as a getaway driver waiting at the scene of an armed robbery. Courts overwhelmingly hold that acting as a getaway driver constitutes direct participation with no legitimate commercial use, inherently satisfying the specific intent/purpose standard. Concluding Leo lacked purpose simply because he charged a flat fee is doctrinally flawed.
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: This question concludes Leo is NOT an accomplice to the attempted hijacking. If Leo is not guilty of the underlying felony, he is categorically immune from felony murder. This completely breaks Q13, which evaluates Leo's felony murder liability for Wendy's death as a "major participant" under SB 1437. He cannot be a major participant in a felony he is legally deemed not to have committed.
Recommended fix: Since Leo must be the getaway driver for the subsequent police chase and Q13/Q14 to work, he MUST be guilty of the underlying felony. Rewrite an option to be the correct "Yes" answer, explaining that Leo's active participation as a getaway driver at the scene goes beyond mere knowledge and demonstrates a purpose to facilitate the crime, satisfying specific intent.
-->
```

## Issue 3 — argpass-sonnet

**Q9.** Assume the jurisdiction follows the traditional specific intent (purpose) standard for accomplice liability. Is Leo guilty as an accomplice to Dom's attempted hijacking?

(a) Yes, because he knew Dom intended to commit the hijacking and provided a necessary instrument by driving him to the location.
(b) Yes, because his presence in the idling car provided psychological encouragement to Dom, satisfying the mens rea requirement for accomplice liability.
(c) No, because his refusal to help plan the operation and his acceptance of a flat fee demonstrate he lacked the purpose to facilitate. <!-- correct -->
(d) No, because Dom failed to complete the target substantive offense, entirely precluding any derivative accomplice liability for the waiting getaway driver.
(e) No, because an accomplice must actively participate in the physical commission of the core offense directly at the scene of the crime.

**Answer:** (c)

**Explanation:** Under the traditional specific intent standard (e.g., *Peoni*), an accomplice must have the purpose of facilitating the target offense. Providing minor assistance for a flat fee, while refusing to plan, demonstrates knowledge of the crime but not a purposeful stake in its success. Option (a) is wrong because it relies on mere knowledge rather than the required specific intent to facilitate. Option (b) is wrong because passive presence in an idling car without shared intent does not automatically constitute psychological encouragement. Option (d) is wrong because an accomplice can be liable for an attempted substantive offense, not just a completed one. Option (e) is wrong because an accomplice can provide remote assistance and need not be physically present at the active crime scene.

**Tags:** chapters: [18], topics: [accomplice liability, specific intent, purpose vs knowledge], difficulty: medium, cognitive: application

**Grounding:** Chapter 18: mr-purpose-not-knowledge / *United States v. Peoni*

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that driving a getaway vehicle is an indispensable service, and under doctrines derived from cases like *Lauria*, a jury is sometimes permitted to infer purpose from mere knowledge when the defendant provides uniquely vital goods or services for a severe felony (like hijacking). Thus, Leo's provision of the getaway car with full knowledge of Dom's violent intent satisfies the mens rea for accomplice liability.
(b) Argument-for: A student could argue that sitting in an idling getaway car is the ultimate form of backup, providing crucial psychological encouragement to the principal. By choosing to be present and ready to aid, Leo demonstrates a shared psychological stake in the outcome, effectively satisfying both the actus reus (encouragement) and blurring into the mens rea requirement for accomplice liability.
(c) Argument-for: Under the strict specific intent standard of *United States v. Peoni*, an accomplice must associate himself with the venture and participate in it as something he wishes to bring about. Accepting a simple flat fee and expressly refusing to help plan the crime demonstrate that Leo viewed the act as a mere transaction; he had knowledge, but lacked the purposeful stake in the hijacking's success required for liability.
(d) Argument-for: A student might argue that accomplice liability is strictly derivative of the principal's completed actions. Since Dom only committed an *attempted* hijacking and failed the target substantive offense, a student could mistakenly conclude that Leo cannot be convicted of the target offense, thus precluding derivative liability for the waiting driver.
(e) Argument-for: A student could argue that accomplice liability requires actual participation in the core elements of the crime, distinguishing it from mere facilitation or accessory-after-the-fact liability. Under this view, sitting remotely in a car means Leo did not actively participate at the scene of the hijacking itself.

Head-to-head: Option (c) is the unequivocally correct application of the *Peoni* standard, successfully linking the flat fee and refusal to plan to a lack of purpose. Option (d) contains an explicit false claim ("entirely precluding any") because one can be an accomplice to an attempt. Option (e) contains an explicit false claim ("must actively participate... directly at the scene") because remote accomplices exist. Option (b) makes a clear category error by stating psychological encouragement "satisfies the mens rea requirement," but lacks a strict absolute locking word. Option (a) relies on an inference that is highly plausible in some jurisdictions (inferring purpose from knowledge for severe felonies), making it dangerous without an absolute locking word like "solely because" to render it cleanly falsifiable.

Falsifiable claim per distractor:
- (a): "because he knew Dom intended... and provided a necessary instrument" — implicitly argues this is always legally sufficient to establish specific intent, but lacks an absolute lock, leaving it vulnerable to the "serious felony inference" argument.
- (b): "satisfying the mens rea requirement" — wrong because psychological encouragement is an *actus reus* concept, not mens rea, but would be stronger with an absolute lock.
- (d): "entirely precluding any derivative accomplice liability" — wrong because a defendant can absolutely be liable as an accomplice to an attempted crime.
- (e): "must actively participate... directly at the scene" — wrong because accessories and co-conspirators can provide remote assistance and still face accomplice liability.

Recommended fix: Add absolute locking words to (a) and (b) to ensure they fail the strict close-call standard. 
Change (a) to: "Yes, solely because he knew Dom intended to commit the hijacking and provided a necessary instrument..."
Change (b) to: "Yes, because his presence in the idling car provided psychological encouragement to Dom, which automatically satisfies the mens rea requirement for accomplice liability."
-->
