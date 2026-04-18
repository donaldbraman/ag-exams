# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q13.** Assume Silas's shooting is evaluated in a jurisdiction that generally imposes a duty to retreat before using deadly force. Did Silas have a duty to retreat from his porch?

(a) In a traditional retreat jurisdiction, Silas's porch likely falls under the castle doctrine exception, which removes the duty to retreat when a person is attacked at home. <!-- correct -->
(b) In a traditional retreat jurisdiction, Silas was legally required to retreat into his house because the castle doctrine only applies when an attacker breaches the interior walls.
(c) In a stand-your-ground jurisdiction, Silas had a mandatory duty to retreat because his active participation in gang warfare stripped him of the right to stand his ground.
(d) In any jurisdiction, Silas had a strict duty to retreat because the duty applies universally whenever a safe avenue of escape is available, even on private property.
(e) In a traditional retreat jurisdiction, Silas had no duty to retreat because the legal duty to retreat only applies to non-deadly force, not to deadly defensive force.

**Answer:** (a)

**Explanation:** (a) is correct. Even in jurisdictions that generally impose a duty to retreat before using deadly force, the universally recognized "castle doctrine" exception removes this duty when a person is attacked at their own dwelling, which typically includes the porch. (b) is wrong because the castle doctrine generally extends to the immediate curtilage of the home, such as a porch, not just the interior walls. (c) is wrong because gang involvement does not legally strip a person of their constitutional right to self-defense or stand their ground. (d) is wrong because the castle doctrine explicitly overrides the duty to retreat when the defender is at home. (e) is wrong because the duty to retreat (and the castle exception) only applies to the use of deadly force.

**Tags:** chapters: [22], topics: [self-defense, duty-to-retreat, castle-doctrine], difficulty: easy, cognitive: application

**Grounding:** Chapter 22; castle doctrine exception to the duty to retreat

<!-- argument-pass: SHOULD FIX
(a) Argument-for: In jurisdictions that generally require retreat before using deadly force, the castle doctrine serves as the primary exception. This doctrine removes the duty to retreat when a defender is attacked in their own home. Courts widely interpret "dwelling" to include the immediate curtilage, such as an attached porch. Therefore, Silas would not have a duty to retreat from his own porch before lawfully defending himself.
(b) Argument-for: While the castle doctrine protects the home, jurisdictions differ on how strictly "dwelling" is defined. A student could argue that an unenclosed exterior space like a porch lacks the physical boundaries required for the home exception to attach. Consequently, they might conclude that Silas must retreat inside the actual physical structure of the home before the castle doctrine protects his use of deadly force.
(c) Argument-for: Many modern "stand-your-ground" statutes (such as those in Florida or Texas) explicitly revoke the statutory right to stand one's ground if the defender is engaged in unlawful activity at the time of the incident. If Silas is participating in gang warfare, a student could argue he falls under this statutory exclusion. Under this reasoning, he would lose his stand-your-ground protections and revert to a mandatory duty to retreat.
(d) Argument-for: The fundamental policy underlying the duty to retreat is the absolute preservation of human life. A student could argue that if a perfectly safe avenue of escape exists, deadly force can never be deemed truly "necessary." Relying on older, exceptionally strict interpretations of retreat, a student might argue the duty applies globally to avoid bloodshed, regardless of whether the defender is on private property.
(e) Argument-for: A student might become confused about the boundaries between deadly and non-deadly force. They could incorrectly argue that the extreme exigency of a deadly threat inherently precludes any safe retreat, meaning the law waives the duty entirely for deadly encounters. Under this flawed logic, the legal duty to retreat would realistically only apply to non-deadly altercations where the defender has ample time to walk away.

Head-to-head: Option (a) is the strongest and correctly applies the majority rule extending the castle doctrine to the porch/curtilage. Option (b) locks into a falsifiable claim by stating the doctrine "only applies" when interior walls are breached, which is overly narrow and factually false in virtually all castle doctrine applications. Option (c) relies on a premise ("In a stand-your-ground jurisdiction") that directly contradicts the prompt's instruction to evaluate the scenario in a traditional retreat jurisdiction. Option (d) uses absolute phrasing ("In any jurisdiction," "universally") that completely ignores the widely accepted castle doctrine. Option (e) explicitly flips the legal rule; the duty to retreat applies strictly to *deadly* force, not non-deadly force. The distractors all effectively lock into legally or factually false claims, but the explanation for (c) relies on a blatantly incorrect statement of law that must be revised.

Falsifiable claim per distractor:
- (b): "...because the castle doctrine only applies when an attacker breaches the interior walls." — wrong because the doctrine broadly protects the exterior threshold and curtilage (like porches), not just the interior footprint.
- (c): "In a stand-your-ground jurisdiction..." — wrong because it explicitly contradicts the prompt's assumption that the jurisdiction generally imposes a duty to retreat. 
- (d): "In any jurisdiction... universally whenever a safe avenue of escape is available" — wrong because the universally recognized castle doctrine provides an explicit exception to this duty in the home.
- (e): "...because the legal duty to retreat only applies to non-deadly force..." — wrong because the duty to retreat is explicitly a doctrinal limitation on the use of deadly force.

Recommended fix: Update the explanation for (c). The current explanation claims "gang involvement does not legally strip a person of their constitutional right to self-defense or stand their ground." This is legally false; many states statutorily strip stand-your-ground rights if the defender is engaged in criminal activity (e.g., gang warfare). Revise the explanation for (c) to instead focus on the fact that the option contradicts the prompt's premise (which establishes a duty-to-retreat jurisdiction, not a stand-your-ground jurisdiction).
-->
