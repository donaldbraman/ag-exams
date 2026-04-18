# Fix Guidance for q08

The QA pipeline flagged this question. Rewrite `q08.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q8.** Assume Avon and Marlowe formed a criminal conspiracy to manufacture illicit drugs. Under the *Pinkerton* doctrine, is Avon criminally liable for Inspector Greggs's death, even though Avon never visited the warehouse?

(a) Yes, because the fatal fire and resulting human death were a reasonably foreseeable consequence of the drug manufacturing conspiracy, committed in furtherance of that agreement. <!-- correct -->
(b) No, because Avon specifically delegated all day-to-day warehouse management and safety monitoring to Marlowe, legally shielding him from downstream vicarious criminal liability.
(c) Yes, because corporate CEOs are automatically held to absolute strict liability for any accidental deaths that occur on company-leased property, regardless of actual foreseeability.
(d) No, because the Pinkerton doctrine only extends vicarious liability to those co-conspirators who commit an overt physical act directly contributing to the substantive offense.
(e) Yes, because the Pinkerton doctrine automatically holds all senior corporate officers liable for the unlawful acts of their subordinates, even without a prior criminal agreement.

**Answer:** (a)

**Explanation:** (a) is correct because the *Pinkerton* doctrine holds conspirators vicariously liable for the substantive offenses committed by their co-conspirators, provided those offenses are in furtherance of the conspiracy and are a reasonably foreseeable consequence of the unlawful agreement. (b) is wrong because delegating operational duties does not sever *Pinkerton* liability for foreseeable acts committed by a co-conspirator. (c) is wrong because *Pinkerton* relies on the conspiratorial agreement and foreseeability, not on a theory of absolute strict liability for CEOs. (d) is wrong because *Pinkerton* explicitly allows conviction of a conspirator who did not personally commit the substantive offense. (e) is wrong because *Pinkerton* requires proof of a conspiratorial agreement, not merely a corporate hierarchy.

**Tags:** chapters: [19], topics: [Pinkerton doctrine, conspiracy, vicarious liability], difficulty: medium, cognitive: application

**Grounding:** pinkerton-doctrine

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: The phrasing of (a) creates a slight grammatical/doctrinal trap. It states the "fatal fire and resulting human death were... committed in furtherance." In criminal law, accidental deaths and fires are not "committed in furtherance" of a conspiracy; rather, the underlying substantive offenses (drug manufacturing) are committed in furtherance, and the death is a reasonably foreseeable consequence of those acts. 
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: pass
Recommended fix: Reword (a) to clarify what was in furtherance. For example: "Yes, because the underlying acts that caused the death were committed in furtherance of the drug manufacturing conspiracy, making the resulting homicide a reasonably foreseeable consequence for which Avon is vicariously liable."
-->
