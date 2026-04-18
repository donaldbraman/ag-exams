# Fix Guidance for q10

The QA pipeline flagged this question. Rewrite `q10.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-opus

**Q10.** Prosecutors indict Avon under RICO, alleging he conducted the affairs of an enterprise through a pattern of racketeering activity. Avon argues that because Barksdale Logistics Corp. is a legally registered, legitimate commercial storage business, it cannot serve as a RICO "enterprise." Will Avon's argument succeed?

(a) Yes, because the federal RICO statute was specifically drafted to target exclusively illegitimate, underground criminal syndicates rather than legally registered, above-ground commercial entities.
(b) No, because RICO explicitly allows legally registered, legitimate corporations to serve as the structural enterprise if their operational affairs are conducted through a pattern of racketeering. <!-- correct -->
(c) Yes, because the traditional hub-and-spoke doctrine strictly requires a RICO enterprise to be completely separate from any formal, legally incorporated business structure or commercial identity.
(d) No, because any minor regulatory violation, such as operating an unregistered commercial storage facility, automatically qualifies a legitimate business as a corrupt RICO enterprise.
(e) Yes, because Avon's complete delegation of the illicit physical activities to Marlowe means he did not directly operate or manage the affairs of the enterprise.

**Answer:** (b)

**Explanation:** (b) is correct because RICO defines "enterprise" broadly. A legitimate, legally registered corporation can serve as the RICO enterprise when its officers conduct its affairs through a pattern of predicate racketeering acts (like illicit drug manufacturing). (a) is wrong because the Supreme Court has repeatedly held that RICO applies to both legitimate and illegitimate enterprises. (c) is wrong because "hub-and-spoke" refers to conspiracy structures, not a restriction on whether formal corporations can be RICO enterprises. (d) is wrong because mere regulatory violations are not enumerated predicate acts under RICO. (e) is wrong because as CEO who entered the agreement to restrict the warehouse for drug manufacturing, Avon clearly participated in the operation or management of the enterprise under the *Reves* test.

**Tags:** chapters: [20], topics: [RICO, enterprise liability, corporate enterprise], difficulty: medium, cognitive: application

**Grounding:** corporate-enterprise

<!-- argument-pass: MUST FIX
(a) Argument-for: A student could argue that RICO was historically aimed at the mafia and organized crime. The legislative history heavily emphasizes eradicating underground syndicates, leading a student to mistakenly conclude that a legally registered commercial business falls outside the statutory intent of a RICO "enterprise."
(b) Argument-for: This is the correct application of RICO doctrine, specifically established in *United States v. Turkette*. The Supreme Court ruled that "enterprise" encompasses both legitimate and illegitimate entities, so a registered corporation can successfully serve as the structural enterprise.
(c) Argument-for: A student might conflate conspiracy doctrines (hub-and-spoke) with the RICO enterprise distinctness requirement. They might mistakenly argue that to be sufficiently distinct from the defendant, an enterprise must be an informal association completely separate from a formal corporate identity.
(d) Argument-for: A student might recall that RICO is a sweeping statute and mistakenly assume that any repeated violation of law triggers it. They could believe that basic regulatory noncompliance automatically transforms an entity into a "corrupt" enterprise for RICO purposes.
(e) Argument-for: A student might rely on the *Reves v. Ernst & Young* "operation or management" test. They might argue that complete delegation of illicit activities to an underling shields a defendant from liability because they did not "directly" execute the affairs themselves.

Head-to-head: Option (b) correctly states the legal rule that legitimate corporations can be RICO enterprises. Option (a) explicitly contradicts the Supreme Court's holding in *Turkette*. Option (c) misapplies the hub-and-spoke conspiracy concept to incorrectly claim enterprises cannot be incorporated structures. Option (d) falsely claims minor regulatory violations automatically constitute RICO enterprises, ignoring the enumerated predicate acts requirement. Option (e) is legally false under *Reves* (delegating tasks still counts as operating/managing), but critically, it introduces completely new facts ("Marlowe", "illicit physical activities") that do not exist in the prompt, rendering it a broken distractor. Furthermore, (e)'s reasoning does not address the premise of Avon's specific argument. This earns a MUST FIX verdict.

Falsifiable claim per distractor:
- (a): "target exclusively illegitimate, underground criminal syndicates" — wrong because the Supreme Court explicitly held in *Turkette* that RICO applies to legitimate businesses.
- (c): "strictly requires a RICO enterprise to be completely separate from any formal, legally incorporated business structure" — wrong because an incorporated entity is explicitly included in the statutory definition of an enterprise.
- (d): "any minor regulatory violation... automatically qualifies a legitimate business as a corrupt RICO enterprise" — wrong because RICO requires a pattern of racketeering activity based on specific enumerated predicate crimes, not mere regulatory violations.
- (e): "complete delegation of the illicit physical activities to Marlowe means he did not directly operate or manage" — wrong because directing or delegating activities still satisfies the "operation or management" test, and heavily relies on facts entirely absent from the prompt.

Recommended fix: Rewrite (e) to rely only on the facts presented in the prompt while maintaining a falsifiable legal error. For example: "(e) Yes, because a corporate officer is categorically immune from RICO liability if the enterprise in question is their own legally registered, legitimate employer."
-->
