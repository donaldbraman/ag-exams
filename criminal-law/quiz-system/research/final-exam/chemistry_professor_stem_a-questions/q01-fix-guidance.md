# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q1.** The prosecution charges Arthur with manufacturing a Schedule I controlled substance under a statute that is silent as to mens rea. Arthur argues that his genuine, mistaken belief that he was synthesizing a legal "nootropic" defeats the charge. How should the court rule?

(a) Guilty, because the dangerous items heuristic places the burden on those dealing in narcotics to ascertain the statutory classification at their peril. <!-- correct -->
(b) Guilty, because his mistake of law was unreasonable given his extensive expertise as a tenured chemistry professor.
(c) Not guilty, because the Morissette presumption requires reading at least a recklessness standard into statutes silent on mens rea.
(d) Not guilty, because his mistake of law regarding the regulatory database constitutes a valid official reliance defense.
(e) Not guilty, because a genuine mistake of fact as to the identity of the synthesized substance negates the requisite mental state.

**Answer:** (a)

**Explanation:** (a) is correct. Under *United States v. Balint*, dealers in narcotics and other obviously dangerous items are on notice of regulation and must ascertain the statutory prohibition at their peril; strict liability applies, and a mistake regarding the substance's legal scheduling is no defense. (b) fails because even a reasonable mistake of law provides no defense to this public welfare offense. (c) fails because the *Morissette* presumption against strict liability is overridden by the dangerous items heuristic for narcotics. (d) fails because a personal misreading of a database is not an official statement of the law justifying reliance. (e) fails because Arthur knew the exact molecular structure he was making, constituting a mistake of law (its scheduling status), not a mistake of fact.

**Tags:** chapters: [11], topics: [public welfare offenses, mistake of law, dangerous items], difficulty: medium, cognitive: application

**Grounding:** Chapter 11, United States v. Balint.

<!-- audit: MUST FIX
check 1: finding: (a) assumes Arthur knew he was dealing with a narcotic/dangerous item, but the stem leaves open the possibility that he was physically mistaken about what substance he was creating. If he didn't know the physical identity of the substance, Balint's strict liability wouldn't apply.
check 2: finding: Option (e) is a highly defensible distractor. A prepared student could argue that Arthur's belief that he was making a nootropic was a mistake of fact as to the physical identity of the synthesized substance, completely negating mens rea even under a strict liability framework.
check 3: finding: Fails. The explanation for (e) relies on a phantom fact: "Arthur knew the exact molecular structure he was making." This fact is entirely absent from the stem.
check 4: finding: Fails. The stem lacks sufficient facts. It must explicitly resolve whether Arthur knew the chemical structure he was synthesizing (mistake of law regarding scheduling) or was mistaken about the physical compound he was creating (mistake of fact).
check 5: pass
check 6: pass
check 7: finding: The explanation ignores the `staples-outlier-serious-penalties` refinement (which distinguishes serious felonies from minor regulatory offenses), treating Balint as an absolute rule despite Schedule I manufacturing carrying severe felony penalties.
Recommended fix: Add to the stem that Arthur "knew the exact chemical formula and molecular structure of what he was synthesizing, but genuinely believed that specific structure was not a scheduled controlled substance." Additionally, adjust the explanation to address why Staples' limit on severe penalties doesn't override the Balint heuristic here.
-->

## Issue 2 — argpass-opus

**Q1.** The prosecution charges Arthur with manufacturing a Schedule I controlled substance under a statute that is silent as to mens rea. Arthur argues that his genuine, mistaken belief that he was synthesizing a legal "nootropic" defeats the charge. How should the court rule?

(a) Guilty, because the dangerous items heuristic places the burden on those dealing in narcotics to ascertain the statutory classification at their peril. <!-- correct -->
(b) Guilty, because his mistake of law was unreasonable given his extensive expertise as a tenured chemistry professor.
(c) Not guilty, because the Morissette presumption requires reading at least a recklessness standard into statutes silent on mens rea.
(d) Not guilty, because his mistake of law regarding the regulatory database constitutes a valid official reliance defense.
(e) Not guilty, because a genuine mistake of fact as to the identity of the synthesized substance negates the requisite mental state.

**Answer:** (a)

**Explanation:** (a) is correct. Under *United States v. Balint*, dealers in narcotics and other obviously dangerous items are on notice of regulation and must ascertain the statutory prohibition at their peril; strict liability applies, and a mistake regarding the substance's legal scheduling is no defense. (b) fails because even a reasonable mistake of law provides no defense to this public welfare offense. (c) fails because the *Morissette* presumption against strict liability is overridden by the dangerous items heuristic for narcotics. (d) fails because a personal misreading of a database is not an official statement of the law justifying reliance. (e) fails because Arthur knew the exact molecular structure he was making, constituting a mistake of law (its scheduling status), not a mistake of fact.

**Tags:** chapters: [11], topics: [public welfare offenses, mistake of law, dangerous items], difficulty: medium, cognitive: application

**Grounding:** Chapter 11, United States v. Balint.

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the dangerous items heuristic derived from *United States v. Balint*, statutes regulating narcotics and other inherently dangerous items are construed as public welfare offenses. Thus, even if a statute is silent on mens rea, courts will apply strict liability, requiring those dealing in such items to ascertain the law and facts at their peril. Arthur's mistaken belief provides no defense, rendering him guilty.
(b) Argument-for: Ignorance of the law is generally no excuse, but some jurisdictions might consider reasonable mistakes under limited circumstances. Because Arthur is a chemistry professor, any mistake regarding the legality of a synthesized chemical is objectively unreasonable. Therefore, his unreasonableness precludes any possible mistake of law defense, leading to his guilt.
(c) Argument-for: The *Morissette v. United States* presumption against strict liability applies to crimes with severe punishments that are not true public welfare offenses. Since manufacturing Schedule I substances is typically a severe felony, a court must read a mens rea of at least recklessness into the silent statute, per default gap-filling principles. Because Arthur had a genuine belief, he may not have been reckless.
(d) Argument-for: The official reliance doctrine excuses a mistake of law when a defendant reasonably relies on an official statement of the law. If Arthur's mistake stemmed from consulting a regulatory database to ascertain the "nootropic" status, this constitutes reliance on an official government publication, providing a valid defense.
(e) Argument-for: The distinction between mistake of fact and mistake of law is critical; a genuine mistake of fact can negate the requisite mens rea. If Arthur intended to synthesize a different, legal substance but accidentally synthesized a Schedule I substance, this constitutes a mistake of fact regarding the physical identity of the chemical. Such a mistake negates the knowledge requirement inherently read into non-public welfare statutes.

Head-to-head: Option (a) accurately states the rule from *United States v. Balint*, establishing strict liability for narcotics offenses when the statute is silent based on the dangerous items heuristic. Option (b) fails because it predicates guilt on the *unreasonableness* of the mistake of law, whereas mistake of penal law is categorically no defense regardless of reasonableness. Option (c) falsely asserts that *Morissette* mandates reading "at least a recklessness standard" into silent statutes; *Morissette* typically reads in common law knowledge or intent, while the recklessness default belongs to the distinct Model Penal Code (§ 2.02(3)). Option (d) fails because relying on a personal reading of a regulatory database does not qualify as an individualized "official statement" under the official reliance doctrine. Option (e) claims a mistake of fact negates the mental state. While legally sound as a general principle, the explanation relies on the unstated premise that Arthur "knew the exact molecular structure he was making." Because this crucial fact is absent from the prompt, a student could justifiably interpret Arthur's "mistaken belief" as a mistake of fact, leaving (e) without an explicit, falsifiable error within the four corners of the question.

Falsifiable claim per distractor:
- (b): "because his mistake of law was unreasonable" — wrong because mistake of penal law is generally no defense regardless of reasonableness; the unreasonableness is not the legal basis for his guilt.
- (c): "the Morissette presumption requires reading at least a recklessness standard" — wrong because *Morissette* reads in common law knowledge or general intent; the categorical "recklessness" default is an MPC statutory provision, not the *Morissette* presumption.
- (d): "his mistake of law regarding the regulatory database constitutes a valid official reliance defense" — wrong because personal misinterpretations of a database do not constitute the affirmative official statement required for a valid reliance defense.
- (e): "genuine mistake of fact as to the identity of the synthesized substance negates the requisite mental state" — arguably lacks a falsifiable error because the prompt fails to specify whether Arthur's mistake was regarding the physical substance's identity (fact) or its legal scheduling (law).

Recommended fix: Edit the prompt to explicitly establish that Arthur knew the physical characteristics of the substance. Change: "Arthur argues that his genuine, mistaken belief that he was synthesizing a legal 'nootropic' defeats the charge." to "Arthur knows the exact molecular structure of the substance he is making, but argues that his genuine, mistaken belief that the substance is an unscheduled, legal 'nootropic' defeats the charge."
-->
