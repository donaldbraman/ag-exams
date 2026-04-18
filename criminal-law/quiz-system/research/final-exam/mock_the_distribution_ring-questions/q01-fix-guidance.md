# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

*Our narcotics unit has been tracking a new distribution ring. We ran a sting operation yesterday that yielded mixed results. Read the initial surveillance reports. I need a memo assessing whether we have actionable conspiracy charges based on their meeting, and whether the attempted distribution charge against the buyer holds water given his actions en route.*

---

**Q1.** Is there sufficient evidence to support a finding that Ben, Cole, and Damon formed a conspiratorial agreement with Artie at the apartment?

(a) Yes, because their coordinated conduct of nodding and accepting the cash advance with no plausible innocent explanation allows an inference of mutual agreement to the criminal enterprise. <!-- correct -->
(b) No, because the defendants never explicitly discussed the specific details of the stash house plan among themselves, which defeats the requirement for an express meeting of the minds.
(c) No, because their silent presence at Artie's apartment and receipt of funds fails to establish the specific intent to promote the underlying offense required by the substantial step test.
(d) Yes, because under the unilateral conspiracy approach, Artie's individual belief that they had joined his operation is legally sufficient to impose liability on the entire group simultaneously.
(e) No, because their acceptance of the $500 cash advance merely establishes an unconsummated buyer-seller relationship, which categorically cannot form the basis of a distribution conspiracy charge.

**Answer:** (a)

**Explanation:** (a) is correct because courts can infer conspiratorial agreement from coordinated conduct (such as nodding and taking money to execute a task) that lacks a plausible innocent explanation; direct proof of explicit agreement is not required. (b) is wrong because conspirators do not need to explicitly discuss details to form an agreement. (c) is wrong because the "substantial step" test applies to the actus reus of attempt, not the formation of a conspiracy agreement. (d) is wrong because unilateral conspiracy allows conviction of the *one* person who believes an agreement exists (e.g., when dealing with an undercover agent), but it does not magically bind others who lack intent. (e) is wrong because the buyer-seller exception applies to purchasing drugs for personal use, not receiving an advance to distribute drugs for an organization.

**Tags:** chapters: [19], topics: [conspiracy, agreement-inference], difficulty: medium, cognitive: application

**Grounding:** Chapter 19, agreement-inference

<!-- audit: MUST FIX
<check 1>: pass (doctrinally accurate on `agreement-inference`, though un-evaluable against the text since facts are missing)
<check 2>: pass (no distractors become correct, but lack of facts makes evaluating distractor viability impossible)
<check 3>: pass (explanation accurately reflects the `agreement-inference` doctrine)
<check 4>: MUST FIX. The stem completely omits the actual facts of the case. It directs the student to "Read the initial surveillance reports" but never provides them. The crucial facts required to answer the question—that Ben, Cole, and Damon were "nodding and accepting the [$500] cash advance" without a "plausible innocent explanation"—only appear backward-engineered in the answer choices.
<check 5>: pass (no unresolved jurisdictional splits implicated by the tested doctrine)
<check 6>: pass (no excluded topics)
<check 7>: pass (doctrine is properly grounded in Ch 19 map under `agreement-inference`)
<check 8>: pass (all options are roughly symmetrical in length and structure)
Recommended fix: Add the missing factual scenario to the stem (or before Q1) explicitly describing the surveillance report of the sting, the meeting at Artie's apartment, the defendants' nodding, and their acceptance of the $500 cash advance to run the distribution.
-->
