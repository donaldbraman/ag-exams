# Fix Guidance for q11

The QA pipeline flagged this question. Rewrite `q11.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q11.** Assume the felony murder charge against Damon fails. If Damon is charged with intentional homicide, can he successfully reduce the charge to voluntary manslaughter?

(a) No, because being mocked as an "errand boy" does not constitute legally adequate provocation to trigger the heat of passion defense under traditional common law categories. <!-- correct -->
(b) Yes, because Damon's flushed face and immediate reaction prove he was acting under a genuine extreme emotional disturbance that automatically mitigates murder to manslaughter.
(c) No, because Damon arrived at the house with a loaded weapon, which establishes premeditation as a matter of law and absolutely precludes any mitigation argument.
(d) Yes, because words alone are always sufficient to establish adequate provocation in modern jurisdictions, provided the defendant experienced a sudden and intense loss of control.
(e) No, because the heat of passion defense is completely unavailable to defendants who are engaged in an underlying criminal enterprise at the time of the provocation.

**Answer:** (a)

**Explanation:** (a) is correct because under the traditional common law, "words alone" (such as mere insults or mocking) are categorically insufficient to constitute adequate provocation for voluntary manslaughter. (b) is wrong because while his flushed face shows subjective passion, the objective prong (adequate provocation) is not met by a simple insult. (c) is wrong because bringing a weapon may be evidence of premeditation, but it does not absolutely preclude mitigation if a legally adequate provocation (e.g., mutual combat) occurs later. (d) is wrong because the traditional rule explicitly rejects "words alone," and even modern MPC approaches require the emotional disturbance to be reasonable under the circumstances, which an insult during a home invasion is not. (e) is wrong because engaging in a crime does not categorically bar the heat of passion defense if an independent, legally adequate provocation genuinely occurs.

**Tags:** chapters: [12], topics: [homicide, provocation, words-alone], difficulty: medium, cognitive: application

**Grounding:** Chapter 12, words-alone-girouard

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The question stem is entirely missing the underlying fact pattern. It references Damon, but relies on facts found only in the options and explanation (a home invasion, arriving with a loaded weapon, being mocked as an "errand boy", having a flushed face). The student cannot answer the question without these facts.
check 5: SHOULD FIX. The question does not specify a jurisdiction (e.g., common law vs. MPC). While option (a) explicitly qualifies its reasoning with "under traditional common law categories," best practice is to specify the jurisdiction in the call of the question (e.g., "Under the traditional common law...") to prevent students from arguing for an MPC-based extreme emotional disturbance (EED) theory.
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Prepend the missing fact pattern detailing Damon's home invasion, the weapon, the "errand boy" insult, and his reaction. Modify the stub to read: "If Damon is charged with intentional homicide in a traditional common law jurisdiction, can he successfully reduce..."
-->
