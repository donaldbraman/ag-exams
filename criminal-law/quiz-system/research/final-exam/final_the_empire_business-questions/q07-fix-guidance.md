# Fix Guidance for q07

The QA pipeline flagged this question. Rewrite `q07.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q7.** Assume Dominic's prior conviction validly prohibits him from possessing a firearm. Can he be convicted of constructively possessing the 9mm handgun found during the search?

(a) No, because the handgun was located in a space within his wife's exclusive control, defeating any inference of his dominion and control. <!-- correct -->
(b) Yes, because spouses living in a shared household are legally presumed to have joint constructive possession of all firearms located within the home.
(c) No, because the handgun was legally registered to his wife, which completely immunizes him from any constructive possession liability.
(d) Yes, because he had general access to the master bedroom, which legally satisfies the requirement of power to exercise dominion and control.
(e) No, because constructive possession requires the government to conclusively prove that the defendant's fingerprints or DNA were recovered from the firearm.

**Answer:** (a)

**Explanation:** Where contraband is found in a space within the exclusive control of a co-occupant (like a personal bedside drawer containing only her belongings), the government cannot establish that the defendant had dominion and control over it (*State v. White*). (b) is wrong because courts require space-specific analysis, not a blanket presumption for spouses. (c) is wrong because legal registration to another does not legally bar a constructive possession charge if the defendant actually exercised control. (d) is wrong because general access to the room is insufficient when the specific space (the drawer) was exclusively hers. (e) is wrong because physical evidence like fingerprints is not strictly required if other evidence of dominion and control exists.

**Tags:** chapters: [15], topics: [constructive-possession, exclusive-control], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15 - State v. White (Exclusive Control)

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Fact 11 contains Dominic's admission that he knew the gun was there and instructed his wife to get rid of it. This directly provides the "additional nexus" needed to overcome the wife's exclusive control (which Q8 is designed to test). Because students read the full fact pattern, they will know Fact 11 exists, making Q7's Answer A ("No") legally incorrect or highly confusing in context.
Recommended fix: Modify the Q7 prompt to deliberately isolate the facts: "Assume Dominic's prior conviction validly prohibits him from possessing a firearm, and assume for the purposes of this question that he made no statements to the agents. Can he be..."
-->

## Issue 3 — argpass-opus

**Q7.** Assume Dominic's prior conviction validly prohibits him from possessing a firearm. Can he be convicted of constructively possessing the 9mm handgun found during the search?

(a) No, because the handgun was located in a space within his wife's exclusive control, defeating any inference of his dominion and control. <!-- correct -->
(b) Yes, because spouses living in a shared household are legally presumed to have joint constructive possession of all firearms located within the home.
(c) No, because the handgun was legally registered to his wife, which completely immunizes him from any constructive possession liability.
(d) Yes, because he had general access to the master bedroom, which legally satisfies the requirement of power to exercise dominion and control.
(e) No, because constructive possession requires the government to conclusively prove that the defendant's fingerprints or DNA were recovered from the firearm.

**Answer:** (a)

**Explanation:** Where contraband is found in a space within the exclusive control of a co-occupant (like a personal bedside drawer containing only her belongings), the government cannot establish that the defendant had dominion and control over it (*State v. White*). (b) is wrong because courts require space-specific analysis, not a blanket presumption for spouses. (c) is wrong because legal registration to another does not legally bar a constructive possession charge if the defendant actually exercised control. (d) is wrong because general access to the room is insufficient when the specific space (the drawer) was exclusively hers. (e) is wrong because physical evidence like fingerprints is not strictly required if other evidence of dominion and control exists.

**Tags:** chapters: [15], topics: [constructive-possession, exclusive-control], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15 - State v. White (Exclusive Control)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: This option correctly identifies the core limitation on constructive possession in shared dwellings. When a specific space is under the exclusive control of a co-occupant, the defendant lacks the necessary dominion and control over the contraband within it. This aligns directly with *State v. White*, establishing that mere co-occupancy of the broader premises cannot overcome the lack of control over the specific locus, making a conviction legally impossible on these facts.
(b) Argument-for: A student could argue that in the context of marriage and shared marital property, firearms kept in the shared marital home are equally accessible. Some broader interpretations of joint possession might be mistakenly read to imply that spouses share dominion over all items in the home. Thus, a student could incorrectly infer a legal presumption of joint possession for married couples sharing a residence.
(c) Argument-for: A student could argue that a gun's legal registration establishes an exclusive legal owner who bears sole possession rights. If the firearm is legally registered to the wife, she is the lawful possessor, and Dominic cannot legally claim it. Thus, the legal registration to a third party arguably creates a barrier to attributing possession to a prohibited person, rendering him legally immune to the charge.
(d) Argument-for: General access to the room where contraband is found is often a key factor in establishing the power and intent to exercise dominion and control. Since the handgun was in the shared master bedroom, Dominic has unfettered access to the overarching space. A student could argue that this spatial proximity and access to the room itself are legally sufficient to establish his power to control the item.
(e) Argument-for: To prove constructive possession beyond a reasonable doubt for a hidden item, physical evidence linking the defendant to the weapon is heavily relied upon by defense attorneys. A student might argue that without definitive forensic evidence like fingerprints or DNA, the government lacks the necessary nexus to conclusively link Dominic to the firearm, meaning the charge must fail as a matter of law.

Head-to-head: Option (a) correctly states the legal standard from *State v. White*, acknowledging that a specific space exclusively controlled by a co-occupant defeats the constructive possession nexus. Option (b) locks a false legal claim using the absolute "all firearms." Option (c) is strongly locked by the phrase "completely immunizes." Option (e) is definitively locked by "requires the government to conclusively prove." However, option (d) claims general access "legally satisfies the requirement." While this is demonstrably a false legal claim (general access to a room does not satisfy the requirement if the specific drawer is exclusively controlled by someone else), it lacks a pure absolute word like "automatically" or "categorically" to immunize it completely against a student arguing "legally satisfies" just means "can satisfy" under the totality of the circumstances. Adding an absolute word guarantees the distractor fails the close-call standard.

Falsifiable claim per distractor:
- (b): "legally presumed to have joint constructive possession of all firearms" — wrong because there is no such blanket marital presumption for contraband in a shared home; courts require space-specific analysis.
- (c): "completely immunizes him from any constructive possession liability" — wrong because legal registration to another does not bar a charge if the defendant actually exercised dominion and control over the item.
- (d): "which legally satisfies the requirement" — wrong because general access to the broader room is legally insufficient when the specific locus is exclusively controlled by another.
- (e): "requires the government to conclusively prove that the defendant's fingerprints or DNA were recovered" — wrong because constructive possession can be proven entirely by circumstantial evidence of dominion and control, without physical forensic evidence.

Recommended fix: In (d), insert the word "categorically" or "automatically" so it reads: "which automatically legally satisfies the requirement of power to exercise dominion and control."
-->
