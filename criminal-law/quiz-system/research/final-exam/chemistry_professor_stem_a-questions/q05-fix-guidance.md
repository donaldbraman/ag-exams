# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q5.** Assume that, whether or not Arthur is the factual cause of death, he is charged with depraved heart murder. Arthur argues that because he genuinely believed Julian was just having a "bad reaction" and would "sleep it off," he lacked the conscious awareness of risk required for murder. How should the court rule?

(a) Guilty of depraved heart murder, because abandoning a convulsing victim behind a locked door objectively manifests extreme indifference to human life. <!-- correct -->
(b) Guilty of depraved heart murder, because any distribution of a Schedule I substance is deemed inherently dangerous in the abstract.
(c) Not guilty, because the MPC extreme indifference standard requires the defendant to subjectively desire the victim's death to support murder.
(d) Not guilty, because his genuine belief that Julian would recover negates the gross deviation from ordinary care required for constructive recklessness.
(e) Not guilty, because depraved heart murder requires an affirmative act of violence, and cannot be established through a failure to act.

**Answer:** (a)

**Explanation:** (a) is correct. Under common law cases like *Commonwealth v. Welansky*, constructive recklessness applies when a defendant knows facts that would cause a reasonable person to perceive grave danger; locking a convulsing victim in a room without a phone objectively manifests extreme indifference to human life, satisfying the depraved heart standard even if Arthur subjectively thought Julian would recover. (b) fails because depraved heart murder requires assessing the actual risk created, not abstract dangerousness (which belongs to felony murder). (c) fails because extreme indifference requires recklessness, not a purposeful desire for death. (d) fails because an unreasonable genuine belief does not negate an objective constructive recklessness standard. (e) fails because omissions breaching a legal duty can support depraved heart murder.

**Tags:** chapters: [13], topics: [unintentional homicide, constructive recklessness, depraved heart murder], difficulty: medium, cognitive: application

**Grounding:** Chapter 13, Commonwealth v. Welansky and extreme indifference standard.

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The phrase "whether or not Arthur is the factual cause" inadvertently creates a booby trap. If Arthur is *not* the factual cause of death, he cannot be legally "Guilty of depraved heart murder" (Option A), making the intended correct answer conditionally false. Additionally, the word "convulsing" in option A is not supported by the facts, which state Julian "collapsed."
2. Cross-Doctrine Clashes: Under the MPC, a genuine lack of conscious awareness of the risk negates the subjective recklessness required for extreme indifference murder. The question's intended logic relies on the common law *Welansky* standard (constructive recklessness), but fails to specify the jurisdiction, making it vulnerable to valid MPC-based challenges.
3. Cross-Question Spoilers: pass

Recommended fix: Update the first sentence of the prompt to: "Assume causation is established and Arthur is charged with common law depraved heart murder." In option (a) and the explanation, change "convulsing victim" to "collapsed victim".
-->
