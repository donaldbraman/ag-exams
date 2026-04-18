# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q1.** Silas's defense attorney files a motion to suppress all evidence obtained after the traffic stop, arguing that the officers' subjective pretextual motive violated Silas's Fourth Amendment rights. How should the court rule on the motion to suppress?

(a) Deny the motion, because the officers possessed objective probable cause of a traffic violation, rendering their subjective investigative motives irrelevant under the Fourth Amendment. <!-- correct -->
(b) Grant the motion, because a traffic stop executed solely to investigate an unrelated hunch without independent reasonable suspicion constitutes an unreasonable seizure.
(c) Deny the motion, because the subsequent felony evasion and destruction of evidence retroactively cured any constitutional defect in the officers' initial pretextual traffic stop.
(d) Grant the motion, because using a minor traffic infraction as a pretext for drug enforcement violates the Equal Protection Clause whenever racial disparities are documented.
(e) Deny the motion, because the officers' subjective intent must only be balanced against the severity of the ultimate crime discovered during the resulting execution of the stop.

**Answer:** (a)

**Explanation:** Under *Whren v. United States*, a traffic stop is constitutional under the Fourth Amendment as long as officers have objective probable cause to believe a traffic violation occurred. The officers' actual subjective motivations are irrelevant to the Fourth Amendment analysis. (b) is wrong because *Whren* explicitly forecloses challenges based on subjective pretext. (c) is wrong because post-stop conduct does not retroactively cure an initially unconstitutional stop. (d) is wrong because while Equal Protection prohibits racial discrimination, it does not mandate suppression under the Fourth Amendment framework. (e) is wrong because *Whren* rejected a balancing test based on subjective intent.

**Tags:** chapters: [6], topics: [whren-pretext-constitutional, pretextual-stops, fourth-amendment], difficulty: foundational, cognitive: application

**Grounding:** Chapter 6, Section: Pretextual Stops and the Volume Engine (*Whren v. United States*)

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail. The stem completely lacks a factual scenario. It refers to "the traffic stop" and option (a) assumes "the officers possessed objective probable cause," but the stem provides no facts establishing what Silas did, the traffic violation, or the officers' motives. 
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Add the missing factual scenario to the stem detailing Silas's traffic violation (establishing objective probable cause), the officers' pretextual motive, and the subsequent events.
-->

## Issue 2 — argpass-sonnet

**Q1.** Silas's defense attorney files a motion to suppress all evidence obtained after the traffic stop, arguing that the officers' subjective pretextual motive violated Silas's Fourth Amendment rights. How should the court rule on the motion to suppress?

(a) Deny the motion, because the officers possessed objective probable cause of a traffic violation, rendering their subjective investigative motives irrelevant under the Fourth Amendment. <!-- correct -->
(b) Grant the motion, because a traffic stop executed solely to investigate an unrelated hunch without independent reasonable suspicion constitutes an unreasonable seizure.
(c) Deny the motion, because the subsequent felony evasion and destruction of evidence retroactively cured any constitutional defect in the officers' initial pretextual traffic stop.
(d) Grant the motion, because using a minor traffic infraction as a pretext for drug enforcement violates the Equal Protection Clause whenever racial disparities are documented.
(e) Deny the motion, because the officers' subjective intent must only be balanced against the severity of the ultimate crime discovered during the resulting execution of the stop.

**Answer:** (a)

**Explanation:** Under *Whren v. United States*, a traffic stop is constitutional under the Fourth Amendment as long as officers have objective probable cause to believe a traffic violation occurred. The officers' actual subjective motivations are irrelevant to the Fourth Amendment analysis. (b) is wrong because *Whren* explicitly forecloses challenges based on subjective pretext. (c) is wrong because post-stop conduct does not retroactively cure an initially unconstitutional stop. (d) is wrong because while Equal Protection prohibits racial discrimination, it does not mandate suppression under the Fourth Amendment framework. (e) is wrong because *Whren* rejected a balancing test based on subjective intent.

**Tags:** chapters: [6], topics: [whren-pretext-constitutional, pretextual-stops, fourth-amendment], difficulty: foundational, cognitive: application

**Grounding:** Chapter 6, Section: Pretextual Stops and the Volume Engine (*Whren v. United States*)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under *Whren v. United States*, a traffic stop is reasonable under the Fourth Amendment if police have objective probable cause of a traffic violation. The Supreme Court explicitly held that an officer's subjective motives for making the stop (such as an unrelated investigative hunch) are completely irrelevant to the Fourth Amendment analysis. Therefore, the pretextual nature of the stop does not render it unconstitutional, making this the correct application of black-letter doctrine.
(b) Argument-for: A student could argue that the Fourth Amendment's fundamental touchstone is reasonableness, and seizing a motorist to pursue an unfounded hunch is inherently unreasonable. If the traffic violation is merely a manufactured pretext lacking independent reasonable suspicion for the targeted crime, the true nature of the stop is an unconstitutional fishing expedition. This appeals to the policy idea that police cannot use minor traffic rules to bypass the requirement for individualized suspicion.
(c) Argument-for: A student might argue that even if a stop is initially unconstitutional, the defendant's subsequent intervening acts—such as fleeing and destroying evidence—break the causal chain under the attenuation doctrine. By committing new, independent crimes, the defendant purges the taint of the original illegality. Therefore, a student could incorrectly conclude this legally "cures" the constitutional defect of the stop itself.
(d) Argument-for: A student could argue that pretextual stops often disproportionately target minority drivers, implicating the Equal Protection Clause. Because *Whren* acknowledged that intentional discrimination violates Equal Protection, a student might reason that documented racial disparities (disparate impact) are sufficient to prove this violation. Consequently, granting the motion to suppress would serve as the appropriate remedy to deter racially discriminatory police practices.
(e) Argument-for: A student could argue that Fourth Amendment reasonableness is generally determined by a balancing test that weighs the intrusion on the individual against legitimate governmental interests. Under this view, an officer's subjective intent could be factored into a broader balancing approach where the severity of the discovered crime overrides the pretextual nature of the initial stop. This reflects a pragmatic, totality-of-the-circumstances approach to suppression.

Head-to-head: 
Option (a) correctly states the holding of *Whren v. United States*: objective probable cause makes the traffic stop constitutional regardless of subjective intent. Option (b) attempts to contradict *Whren* by asserting that an uncorroborated hunch makes a stop an unreasonable seizure, but it fails to include an absolute lock; if the officers genuinely lacked objective probable cause for the traffic violation, (b) would technically be true. Option (c) relies on a legally false concept; while new crimes might attenuate the taint for the exclusionary rule, they do not "retroactively cure" the Fourth Amendment defect of an initially unconstitutional stop. Option (d) incorrectly states that documented racial disparities automatically violate Equal Protection, ignoring the discriminatory intent requirement, and falsely assumes suppression is the remedy. Option (e) relies on a fabricated balancing test explicitly rejected in *Whren*. Option (b) requires a fix to make it explicitly false even when objective probable cause is present.

Falsifiable claim per distractor:
- (b): "constitutes an unreasonable seizure" — wrong under *Whren* assuming objective probable cause existed, but lacks an absolute word guaranteeing falsity if the student assumes no probable cause was present.
- (c): "retroactively cured any constitutional defect" — wrong because intervening events may attenuate evidentiary taint but cannot legally retroactively "cure" an initially unconstitutional seizure.
- (d): "violates the Equal Protection Clause whenever racial disparities are documented" — wrong because Equal Protection requires a showing of discriminatory purpose/intent, not merely documented disparate impact, and Fourth Amendment suppression is not the remedy.
- (e): "must only be balanced against the severity of the ultimate crime discovered" — wrong because *Whren* explicitly rejected any Fourth Amendment balancing test involving subjective intent and crime severity for traffic stops.

Recommended fix: In (b), add an absolute phrase to lock the falsifiability so it reads: "Grant the motion, because a traffic stop executed solely to investigate an unrelated hunch categorically constitutes an unreasonable seizure, regardless of objective probable cause for a traffic infraction."
-->
