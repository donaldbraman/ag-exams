# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q12.** Dominic is charged with constructive possession of the 9mm handgun found in his wife's dresser. He argues that he cannot be convicted because the gun was in his wife's exclusive control. How should the court analyze his possession of the weapon?

(a) Dominic constructively possessed the gun because his admission that he knew it was in her drawer proves awareness, which alone establishes possession in a shared home.
(b) Dominic did not constructively possess the gun because mere awareness of contraband is insufficient to establish possession without evidence of his intent to exercise dominion over it. <!-- correct -->
(c) Dominic constructively possessed the gun because spouses are legally presumed to have joint dominion and complete control over all property located within the marital residence.
(d) Dominic did not constructively possess the gun because the Second Amendment prohibits holding a felon strictly liable for firearms legally owned by other completely innocent household members.
(e) Dominic did not constructively possess the gun because the weapon was registered exclusively to his wife, which conclusively negates any possible legal inference of control by him.

**Answer:** (b)

**Explanation:** Constructive possession requires the government to prove that the defendant both knew of the contraband's presence and intended to exercise dominion and control over it. As established in *State v. White*, mere awareness that a gun is in a shared household—especially in a space exclusively controlled by a co-occupant, like a personal dresser drawer—does not establish the requisite dominion and control. (a) is wrong because awareness of contraband is a necessary but not sufficient condition for constructive possession. (c) is wrong because there is no legal presumption of joint possession of all items in a shared home, requiring space-specific analysis. (d) is wrong because while the Second Amendment protects the wife's right to own the gun, it does not categorically immunize the felon if actual dominion and control are proven. (e) is wrong because registration is relevant evidence but does not conclusively legally negate constructive possession if control is otherwise proven.

**Tags:** chapters: [15], topics: [firearms, constructive-possession, shared-household], difficulty: intermediate, cognitive: application

**Grounding:** Chapter 15, State of Louisiana v. Gerald Manchip White

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The stem is missing necessary facts that have leaked into the options. Option (a) references "his admission that he knew it was in her drawer" and Option (b) assumes the prosecution's case is based on "mere awareness." Because the stem never stipulates that his admission/awareness is the *only* evidence the state has, a prepared student could rightfully object to the definitive conclusion in (b) ("Dominic did not constructively possess...") by pointing out that the state might possess additional evidence of intent/control not mentioned in the sparse prompt.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Constrain the evidentiary universe in the stem. Add a sentence like: "The prosecution's only evidence linking Dominic to the weapon is his admission to police that he knew it was in the drawer."
-->
