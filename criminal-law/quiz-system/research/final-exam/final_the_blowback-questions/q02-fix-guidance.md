# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — edge-case

**Q2.** Assume that, regardless of the premeditation analysis, Carmine claims his charge should be mitigated to voluntary manslaughter because he acted in the heat of passion. In a traditional common law jurisdiction, is Carmine's provocation defense likely to succeed?

(a) Yes, because discovering that a trusted associate is an FBI informant constitutes a legally recognized category of adequate provocation at common law.
(b) Yes, because Paulie's taunting words and sneer would cause an objectively reasonable person in Carmine's position to lose all self-control.
(c) No, because under the common law categorical approach, insulting words alone—no matter how opprobrious—do not constitute legally adequate provocation. <!-- correct -->
(d) No, because Carmine's split-second decision to shoot demonstrates that a sufficient cooling time had elapsed between the insult and the act.
(e) No, because the traditional common law rule rigidly limits adequate provocation solely to the sudden discovery of a spouse's adultery.

**Answer:** (c)

**Explanation:** At common law, voluntary manslaughter requires adequate provocation that fits within specific historical categories (e.g., mutual combat, assault, or discovering adultery). As held in *Girouard v. State*, words alone—no matter how insulting or upsetting—are never legally adequate provocation. (c) is correct because Paulie merely laughed, sneered, and spoke. (a) fails because discovering a police informant is not a recognized common law category of provocation. (b) fails because the common law does not simply ask if a reasonable person would be provoked; the trigger must be a recognized categorical physical act, not mere words. (d) fails because a split-second decision suggests almost no cooling time elapsed, which would normally favor the defendant rather than defeat the defense. (e) fails because the common law does recognize other categories, such as mutual combat and illegal arrest, not just adultery.

**Tags:** chapters: [12], topics: [voluntary manslaughter, provocation, words alone], difficulty: easy, cognitive: application

**Grounding:** Chapter 12: words-alone-girouard

<!-- edge-case-audit: MUST FIX
1. Fact Pattern Booby Traps: The explanation explicitly states that Paulie "merely laughed, sneered, and spoke," but the full scenario facts state that Paulie ALSO "quickly reached into his jacket." A sharp student will recognize that a physical act occurred and correctly reject (c) because the provocation was not "words alone."
2. Cross-Doctrine Clashes: The physical act of reaching into the jacket is meant to trigger imperfect self-defense (for Q3), but because it exists in the fact pattern, it ruins the premise of the "words alone" provocation test in Q2.
3. Cross-Question Spoilers: pass
Recommended fix: Modify the question stem to isolate the verbal aspect: "Assume Carmine claims his charge should be mitigated to voluntary manslaughter because he acted in the heat of passion in response to Paulie's admission and insult..." Then update the explanation to acknowledge the physical act, clarifying that while reaching into a jacket may trigger a self-defense analysis, a provocation claim based on the verbal insults fails under the words-alone rule, and reaching for a cigar is not a categorical provocation like mutual combat or actual battery.
-->
