# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q12.** Prosecutors want to charge Marcus under the federal RICO statute, alleging the Court Kings constitute an association-in-fact enterprise. Under the Supreme Court's Boyle standard, which of the following best supports the existence of such an enterprise?

(a) Evidence that Marcus, Darius, and Silas all committed unrelated predicate acts of violence within the same calendar year, demonstrating a temporal pattern of racketeering activity without needing a shared overarching structure.
(b) Evidence that the group shared a common purpose of drug distribution, had an ongoing relationship shown by meetings, and possessed a structure distinct from the individual predicate acts themselves. <!-- correct -->
(c) The finding of baking soda in the safe, which demonstrates the group's specific intent to engage in interstate commerce through fraudulent narcotics transactions targeting rival crews and street-level buyers.
(d) Evidence that the enterprise operated exclusively to commit predicate offenses, meaning the enterprise structure and the pattern of racketeering activity were legally and functionally identical in the eyes of the law.
(e) The fact that the group's street-level dealers acted entirely independently but occasionally purchased their supply from Marcus as mere buyers operating in an open, unstructured illicit narcotics market.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under the Supreme Court's *Boyle* standard, an association-in-fact enterprise requires three structural features: a purpose, relationships among those associated with the enterprise, and longevity sufficient to permit the associates to pursue the enterprise's purpose. (a) is wrong because a pattern of racketeering alone does not automatically prove an enterprise structure. (c) is wrong because possessing baking soda relates to a specific fraud or attempt, not the structural requirements of the enterprise itself. (d) is wrong because *Turkette* and *Boyle* require the enterprise to be an entity separate and apart from the pattern of activity in which it engages. (e) is wrong because mere buyer-seller relationships do not establish the shared purpose and structure of a RICO enterprise.

**Tags:** chapters: [20], topics: [RICO, enterprise, Boyle standard], difficulty: medium, cognitive: application

**Grounding:** Chapter 20: boyle-three-part, predicate-acts-relatedness

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might rely on the Supreme Court's holding in *Boyle*, which clarified that an association-in-fact enterprise does not require a formal hierarchy, chain of command, or business-like structure. By emphasizing the looseness permitted by the doctrine, the student could argue that mere temporal proximity of violent acts is sufficient. They might take this to the extreme conclusion that no overarching structure whatsoever is needed if predicate acts are temporally linked. This line of reasoning treats the pattern of activity as inherently establishing the enterprise itself.
(b) Argument-for: A student would correctly identify this as the exact articulation of the *Boyle* standard. The Supreme Court in *Boyle v. United States* explicitly held that an association-in-fact enterprise must have at least three structural features. These features are a shared purpose, relationships among associates, and sufficient longevity to achieve that purpose. Option (b) captures these elements precisely, while also acknowledging *Turkette*'s foundational rule that the enterprise must possess a structure distinct from the individual predicate acts.
(c) Argument-for: A student might focus heavily on the jurisdictional requirements of the federal RICO statute, recognizing that the enterprise must engage in or affect interstate commerce. They might associate baking soda with cutting agents for crack cocaine or fraud schemes. From this, they could conclude that possession of such materials is the crucial factual hook required to establish the interstate commerce element. They might argue this physical evidence inherently proves the structural intent required for an enterprise.
(d) Argument-for: A student might recall the Supreme Court's important evidentiary note in *Turkette* and *Boyle* regarding the overlap of proof. The Court stated that evidence proving the enterprise and the pattern of racketeering activity may frequently "coalesce." A student might mistakenly interpret this evidentiary overlap to mean that the substantive elements are indistinguishable. Thus, they could argue the two concepts are legally and functionally identical in the eyes of the law.
(e) Argument-for: A student might confuse a decentralized buyer-seller market with a large-scale hub-and-spoke conspiracy. They could assume that the mere act of Marcus repeatedly supplying independent street-level dealers provides the requisite continuity and relationships. In drug conspiracy cases, loose networks can sometimes satisfy conspiracy requirements. A student might incorrectly import this standard, arguing that an open, unstructured illicit narcotics market automatically satisfies the association-in-fact enterprise standard under federal law.

Head-to-head: Option (b) is unequivocally correct as it mirrors the doctrinal requirements from *Boyle*. Option (d) presents a strong distractor with an explicit false legal claim (that the enterprise and pattern are legally identical elements). Option (a) contains a false legal claim by asserting no overarching structure is needed. However, options (c) and (e) merely describe factual scenarios that fail to support an enterprise, rather than asserting explicit, identifiable false legal rules directly within their text. Under the close-call standard, distractors should contain locked falsifiable propositions, making (c) and (e) structurally weak because they rely on implicit omissions rather than explicit legal errors.

Falsifiable claim per distractor:
- (a): "without needing a shared overarching structure" — wrong because *Boyle* explicitly requires at least some ascertainable structure, specifically a shared purpose, relationships, and longevity.
- (c): "demonstrates the group's specific intent to engage in interstate commerce" — wrong because finding baking soda factually and legally cannot on its own demonstrate an intent to engage in interstate commerce, but it lacks an absolute categorical legal trigger.
- (d): "legally and functionally identical in the eyes of the law" — wrong because *Turkette* mandates that the enterprise is an entity separate and apart from the pattern of activity, even if the proof coalesces.
- (e): None. — This distractor lacks a falsifiable legal claim, as it merely states a factual condition ("acted entirely independently... as mere buyers") that fails to meet the test, rather than asserting an explicit false legal proposition.

Recommended fix: Edit (e) to include an explicit false legal claim locked with an absolute word. For example: "Evidence of independent street-level dealers purchasing from Marcus, because any ongoing buyer-seller relationship automatically constitutes an association-in-fact enterprise regardless of a shared structural purpose." Edit (c) to similarly lock a legal rule: "The finding of baking soda, which categorically establishes an association-in-fact enterprise solely because it proves specific intent to engage in fraudulent narcotics transactions."
-->

## Issue 3 — argpass-opus

**Q12.** Prosecutors want to charge Marcus under the federal RICO statute, alleging the Court Kings constitute an association-in-fact enterprise. Under the Supreme Court's Boyle standard, which of the following best supports the existence of such an enterprise?

(a) Evidence that Marcus, Darius, and Silas all committed unrelated predicate acts of violence within the same calendar year, demonstrating a temporal pattern of racketeering activity without needing a shared overarching structure.
(b) Evidence that the group shared a common purpose of drug distribution, had an ongoing relationship shown by meetings, and possessed a structure distinct from the individual predicate acts themselves. <!-- correct -->
(c) The finding of baking soda in the safe, which demonstrates the group's specific intent to engage in interstate commerce through fraudulent narcotics transactions targeting rival crews and street-level buyers.
(d) Evidence that the enterprise operated exclusively to commit predicate offenses, meaning the enterprise structure and the pattern of racketeering activity were legally and functionally identical in the eyes of the law.
(e) The fact that the group's street-level dealers acted entirely independently but occasionally purchased their supply from Marcus as mere buyers operating in an open, unstructured illicit narcotics market.

**Answer:** (b)

**Explanation:** The correct answer is (b). Under the Supreme Court's *Boyle* standard, an association-in-fact enterprise requires three structural features: a purpose, relationships among those associated with the enterprise, and longevity sufficient to permit the associates to pursue the enterprise's purpose. (a) is wrong because a pattern of racketeering alone does not automatically prove an enterprise structure. (c) is wrong because possessing baking soda relates to a specific fraud or attempt, not the structural requirements of the enterprise itself. (d) is wrong because *Turkette* and *Boyle* require the enterprise to be an entity separate and apart from the pattern of activity in which it engages. (e) is wrong because mere buyer-seller relationships do not establish the shared purpose and structure of a RICO enterprise.

**Tags:** chapters: [20], topics: [RICO, enterprise, Boyle standard], difficulty: medium, cognitive: application

**Grounding:** Chapter 20: boyle-three-part, predicate-acts-relatedness

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *Boyle*, an association-in-fact enterprise requires only a minimal ascertainable structure and does not need a formal hierarchy or chain of command. A student might argue that the lack of a "shared overarching structure" correctly applies this minimal standard. Furthermore, a student could wrongly conclude that demonstrating a temporal pattern of violent acts among associates over a calendar year is practically sufficient to infer the existence of an enterprise.
(b) Argument-for: This option perfectly aligns with the *Boyle v. United States* test for an association-in-fact enterprise. *Boyle* explicitly requires three structural features: a shared purpose, relationships among the associates, and sufficient longevity to pursue that purpose. Option (b) captures these elements while also affirming the *United States v. Turkette* requirement that the enterprise possess a structure distinct from the pattern of racketeering activity itself.
(c) Argument-for: A student could argue that finding baking soda demonstrates the enterprise's underlying shared purpose (fraudulent narcotics transactions) and establishes an interstate commerce nexus. Because *Boyle* emphasizes that the group must have a shared purpose, a student could wrongly deduce that demonstrating specific intent through physical evidence is the single best way to prove the enterprise's unifying economic goal.
(d) Argument-for: In *Turkette* and *Boyle*, the Supreme Court acknowledged that the evidence proving the enterprise and the evidence proving the pattern of racketeering activity "may in particular cases coalesce." A student might misinterpret this evidentiary overlap to mean that if an enterprise operates exclusively to commit crimes, the enterprise and the pattern functionally merge and become legally identical elements.
(e) Argument-for: *Boyle* establishes a very low structural bar for what constitutes an enterprise, explicitly rejecting the need for formal rules, meetings, or defined roles. A student could argue that a sprawling network of independent street-level buyers and sellers constitutes an association-in-fact enterprise because they are loosely linked by their participation in the same illicit market and occasional transactions with a central figure.

Head-to-head: Option (b) is the clear and unassailable keyed answer because it directly invokes the three *Boyle* factors and the *Turkette* distinction requirement. Distractor (a) uses the fatal phrasing "unrelated predicate acts," which legally prevents the formation of a RICO pattern, let alone an enterprise. Distractor (d) explicitly claims the pattern and enterprise are "legally... identical," which directly contradicts *Turkette*. Distractor (e) uses the absolute "entirely independently," which explicitly negates *Boyle*'s requirement for relationships among associates. Distractor (c), however, is weak because it relies entirely on an implicit omission (failing to mention structure or relationships) rather than stating an explicitly false legal rule locked by absolute words. Because (c) merely states a factual inference, it fails the strict close-call standard. 

Falsifiable claim per distractor:
- (a): "unrelated predicate acts" — wrong because RICO strictly requires related predicate acts to establish a pattern; legally, unrelated acts cannot serve as the foundation for an enterprise's pattern of activity.
- (c): LACKS A FALSIFIABLE LEGAL CLAIM — wrong only by implicit omission of *Boyle*'s structural requirements. The phrase "demonstrates the group's specific intent" is a factual conclusion, not an explicit, mathematically false legal claim about the RICO statute.
- (d): "legally and functionally identical in the eyes of the law" — wrong because *Turkette* explicitly holds that the enterprise and the pattern of racketeering activity are entirely separate elements that must be proven independently, even if the evidence coalesces.
- (e): "acted entirely independently" — wrong because the absolute word "entirely" completely negates the core *Boyle* requirement that there must be "relationships among those associated with the enterprise."

Recommended fix: Edit (c) to include a locked, falsifiable legal claim. Change (c) to: "(c) The finding of baking soda in the safe, which automatically satisfies the Boyle standard solely because it demonstrates the group's specific intent to engage in interstate commerce, regardless of whether the associates had an ongoing relationship."
-->
