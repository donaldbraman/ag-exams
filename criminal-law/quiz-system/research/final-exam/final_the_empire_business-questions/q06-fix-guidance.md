# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q6.** Assume Kevin's possession of the handgun is established. Is he guilty of being a felon in possession of a firearm under 18 U.S.C. § 922(g)?

(a) Guilty, because the statute applies strict liability to the defendant's legal status, meaning his mistaken belief about the conviction is irrelevant.
(b) Guilty, because the Morissette presumption does not extend the mental state requirement to attendant circumstances like a prior conviction.
(c) Not guilty, because he did not possess the specific intent to violate federal firearms laws when he acquired the 9mm handgun.
(d) Not guilty, because under Rehaif, the government must prove he knew he belonged to the prohibited class, which his genuine belief negates. <!-- correct -->
(e) Not guilty, because the Second Amendment's historical tradition test categorically prohibits the government from disarming individuals based solely on nonviolent commercial fraud convictions.

**Answer:** (d)

**Explanation:** Under *Rehaif v. United States*, the government must prove both that the defendant knew he possessed a firearm and that he knew he belonged to the relevant prohibited category (here, having a felony conviction). Because Kevin genuinely believed his conviction was a misdemeanor based on his attorney's email, he lacked the requisite knowledge of his status. (a) is wrong because *Rehaif* explicitly rejected strict liability for the status element. (b) is wrong because the *Morissette* presumption does apply to status elements, which is the core holding of *Rehaif*. (c) is wrong because the government does not need to prove specific intent to break the law, only knowledge of the facts that make the conduct illegal. (e) is wrong because the constitutionality of disarming nonviolent felons is an open and actively litigated post-*Bruen* question, not a categorical prohibition.

**Tags:** chapters: [10], topics: [mistake of fact, status elements, Rehaif], difficulty: hard, cognitive: application

**Grounding:** Chapter 10 (Rehaif v. United States / rehaif-status-element)

<!-- audit: SHOULD FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail. The stem lacks the facts necessary to answer the question (e.g., Kevin's belief that his conviction was a misdemeanor based on his attorney's email), which are only revealed in the explanation. Unless this question is attached to a master fact pattern, it is unsolvable.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: If this is a standalone question, incorporate the necessary facts into the stem: "Assume Kevin's possession of the handgun is established, but he genuinely believed his prior conviction was a misdemeanor based on his attorney's email. Is he guilty..."
-->
