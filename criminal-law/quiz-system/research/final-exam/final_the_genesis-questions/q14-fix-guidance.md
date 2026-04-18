# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** Under the Model Penal Code, is the Courier guilty of attempted possession of narcotics with intent to distribute?

(a) Guilty, because driving to the stash house with a duffel bag strongly corroborates his criminal purpose to possess the drugs. <!-- correct -->
(b) Guilty, because receiving the text message from Avon immediately established his specific intent to commit the crime.
(c) Not guilty, because the MPC requires the actor to come within physical touching distance of the contraband to qualify.
(d) Not guilty, because he was arrested on an unrelated warrant, which legally nullifies his intent to commit the drug offense.
(e) Not guilty, because walking down a public street is protected conduct that cannot be criminalized as an attempt.

**Answer:** (a)

**Explanation:** (a) is correct because under the Model Penal Code's substantial step test, an act is an attempt if it strongly corroborates the actor's criminal purpose. Arriving at the location with an empty duffel bag to execute a drug pickup satisfies this standard. (b) fails because intent alone is insufficient; an actus reus (substantial step) is required. (c) fails because the MPC rejects the proximity test and does not require getting that physically close to completion. (d) fails because the reason for the police intervention does not erase the attempt actus reus already committed. (e) fails because otherwise innocent conduct (walking) becomes criminal when it constitutes a substantial step.

**Tags:** chapters: [17], topics: [attempt, substantial step, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 - Attempts (Actus Reus - Substantial Step)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: FAIL. The stem is entirely missing the fact pattern. The question jumps straight to the prompt and references "the Courier", "Avon", "the stash house", and an "unrelated warrant", but none of these facts are provided to the student.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Add the missing fact pattern describing Avon's text, the Courier's actions with the duffel bag, and the subsequent arrest.
-->

## Issue 2 — argpass-sonnet

**Q14.** Under the Model Penal Code, is the Courier guilty of attempted possession of narcotics with intent to distribute?

(a) Guilty, because driving to the stash house with a duffel bag strongly corroborates his criminal purpose to possess the drugs. <!-- correct -->
(b) Guilty, because receiving the text message from Avon immediately established his specific intent to commit the crime.
(c) Not guilty, because the MPC requires the actor to come within physical touching distance of the contraband to qualify.
(d) Not guilty, because he was arrested on an unrelated warrant, which legally nullifies his intent to commit the drug offense.
(e) Not guilty, because walking down a public street is protected conduct that cannot be criminalized as an attempt.

**Answer:** (a)

**Explanation:** (a) is correct because under the Model Penal Code's substantial step test, an act is an attempt if it strongly corroborates the actor's criminal purpose. Arriving at the location with an empty duffel bag to execute a drug pickup satisfies this standard. (b) fails because intent alone is insufficient; an actus reus (substantial step) is required. (c) fails because the MPC rejects the proximity test and does not require getting that physically close to completion. (d) fails because the reason for the police intervention does not erase the attempt actus reus already committed. (e) fails because otherwise innocent conduct (walking) becomes criminal when it constitutes a substantial step.

**Tags:** chapters: [17], topics: [attempt, substantial step, mpc], difficulty: medium, cognitive: application

**Grounding:** Chapter 17 - Attempts (Actus Reus - Substantial Step)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under MPC § 5.01(1)(c), an attempt requires the actor to take a "substantial step" toward the commission of the target crime. The MPC further specifies that a substantial step must be "strongly corroborative of the actor's criminal purpose." Driving to a known stash house equipped with a duffel bag to collect drugs perfectly meets this standard. The facts show the Courier has gone beyond mere preparation, fulfilling both the mens rea and the actus reus requirements for attempt liability.
(b) Argument-for: The primary focus of attempt law under subjective theories, which the MPC largely adopts, is the actor's mens rea. Attempt specifically requires the purpose to commit the target offense. Receiving the text from Avon and acting upon it proves beyond a reasonable doubt that the Courier possessed this exact specific intent. Therefore, a student could argue that because his intent to distribute narcotics was immediately crystallized by the message, the foundation for guilt is firmly established. 
(c) Argument-for: A foundational concern of attempt law is punishing mere thought or preliminary, non-dangerous preparation. To differentiate a punishable attempt from preparation, some historical common-law tests require the actor to be on the immediate precipice of the crime. A student could argue that under a strict proximity analysis, a person must be in the immediate physical vicinity of the drugs—such as physical touching distance—to constitute an attempt. Without this proximity, the actus reus is insufficiently dangerous.
(d) Argument-for: Attempt liability requires an unbroken causal chain of intent and action up to the point of external frustration by law enforcement trying to stop *that specific crime*. When the Courier is arrested on an unrelated warrant, the specific causal chain of the drug attempt is interrupted by a mere coincidence. A student could argue that this unrelated arrest legally supersedes the in-progress attempt, effectively nullifying the intent and halting the crime before the requisite actus reus for the drug offense is truly completed.
(e) Argument-for: Criminalizing ordinary, everyday behavior risks violating constitutional protections against vagueness and overbreadth in criminal law. Walking down a public street is inherently ambiguous and innocent conduct protected under the Constitution. A student could argue that because the conduct is so fundamentally innocuous, it categorically cannot cross the threshold into a criminal actus reus for attempt, as doing so would criminalize the daily routines of citizens.

Head-to-head: Option (a) is definitively correct because it uses the exact legal standard for the MPC actus reus of attempt (a substantial step strongly corroborative of criminal purpose). Option (c) relies on a falsifiable claim about the MPC requiring "physical touching distance," which explicitly contradicts the MPC's rejection of proximity tests. Option (d) relies on a fabricated legal doctrine that an unrelated arrest "legally nullifies" prior intent. Option (e) features a falsifiable claim by stating walking "cannot be criminalized," ignoring that the MPC allows otherwise innocent conduct to constitute a substantial step. Option (b), however, reaches the wrong conclusion ("Guilty") but relies on a factually plausible premise ("receiving the text... established his specific intent") while *implicitly omitting* the substantial step actus reus requirement. Because implicit omissions do not suffice for a bulletproof distractor under the close-call standard, (b) lacks an explicitly locked false claim.

Falsifiable claim per distractor:
- (b): "receiving the text message from Avon immediately established his specific intent" — implicitly wrong because it lacks the required actus reus for guilt, but the statement itself lacks an absolute word locking the false legal standard (e.g., that intent *alone* is sufficient).
- (c): "requires the actor to come within physical touching distance" — wrong because the MPC uses the substantial step test and expressly rejects such strict physical proximity requirements.
- (d): "legally nullifies his intent to commit the drug offense" — wrong because an intervening arrest on a different matter does not retroactively erase established mens rea or a completed substantial step.
- (e): "is protected conduct that cannot be criminalized as an attempt" — wrong because ordinary, legal behavior like walking can become criminal under the MPC if it is strongly corroborative of a criminal purpose.

Recommended fix: Edit (b) to lock the false proposition with an absolute word. Change (b) to: "Guilty, solely because receiving the text message from Avon established his specific intent, which is the only requirement for attempt."
-->
