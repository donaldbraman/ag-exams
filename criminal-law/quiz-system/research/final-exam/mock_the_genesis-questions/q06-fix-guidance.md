# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume that, instead of traditional common law, the jurisdiction has fully adopted the Model Penal Code (MPC). Because the Chemical Act carries a penalty of up to 30 days in jail, the MPC would not permit it to be treated as a strict liability violation. How does the MPC resolve the statute's silence on mens rea?

(a) It defaults to a requirement of purpose, meaning the prosecution must prove Albert's conscious object was to violate the permit requirement of the Chemical Act.
(b) It defaults to a requirement of recklessness, meaning the prosecution must prove Albert consciously disregarded a substantial and unjustifiable risk that his storage lacked a permit. <!-- correct -->
(c) It defaults to a requirement of negligence, meaning Albert can be convicted if he should have been aware of the permit requirement but failed to notice.
(d) It invalidates the statute entirely under the void-for-vagueness doctrine due to the legislature's failure to specify a mental state in the text of the law.
(e) It reads in a requirement of knowledge regarding the actus reus, but retains strict liability for the attendant circumstance of lacking the required safety permit.

**Answer:** (b)

**Explanation:** Under MPC § 2.02(3), when a statute defining an offense is silent on the required mental state, the default culpability level is recklessness. The prosecution must prove the defendant consciously disregarded a substantial and unjustifiable risk regarding the material elements. (a) is incorrect because the MPC defaults to recklessness, not purpose, when the statute is silent. (c) is incorrect because the default is recklessness, not negligence. (d) is incorrect because statutory silence triggers the MPC's default interpretation rules rather than invalidating the statute for vagueness. (e) is incorrect because under MPC § 2.02(4), the "one for all" presumption applies the default mens rea to all material elements, including attendant circumstances like the permit requirement.

**Tags:** chapters: [10], topics: [MPC defaults, mpc-silence-recklessness], difficulty: medium, cognitive: application

**Grounding:** Chapter 10, Mistake of Fact and Law — mpc-silence-recklessness

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: explanation drift. The explanation for (e) cites MPC § 2.02(4) to apply the default mens rea to the attendant circumstance. However, § 2.02(4) (the "one-for-all" rule) only applies when a statute *explicitly provides* a mens rea but doesn't distinguish among elements. When a statute is entirely silent, § 2.02(3) alone applies the recklessness default to each material element. 
Check 4: missing facts. The stem completely lacks a fact pattern. The answer choices reference "Albert" and the fact that "his storage lacked a permit," but Albert and his conduct are never introduced in the stem.
Check 5: pass
Check 6: pass
Check 7: pass
Recommended fix: Add a sentence to the stem establishing the missing facts (e.g., "Albert is charged under the Chemical Act, which provides that 'whoever stores hazardous chemicals without a permit shall be guilty of an offense.'"). Additionally, update the explanation for (e) to reflect that § 2.02(3) itself applies the recklessness default to each material element when the statute is silent.
-->
