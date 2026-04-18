# Fix Guidance for q13

The QA pipeline flagged this question. Rewrite `q13.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q13.** Assume prosecutors charge Deacon and his network under the federal Racketeer Influenced and Corrupt Organizations (RICO) Act. Under the *Boyle* test, does the operation qualify as an associated-in-fact "enterprise"?

(a) Yes, because the fentanyl network possessed a shared illicit purpose, ongoing relationships among its associates, and sufficient longevity to permit them to pursue the enterprise's overarching criminal goals. <!-- correct -->
(b) No, because the network entirely lacked an underlying legitimate business front, which is structurally required to establish a continuous pattern of racketeering activity under the federal statute.
(c) Yes, because the organized group successfully committed at least two predicate felony offenses within a ten-year period, which automatically and independently satisfies the statutory enterprise requirement.
(d) No, because a purely criminal organization cannot legally constitute an enterprise unless it exerts verifiable monopolistic control over a specific, defined geographic territory or illicit market sector.
(e) Yes, because the network was operated exclusively by associated individuals rather than a legally recognized corporate entity, which shields it from standard state-level corporate criminal liability doctrines.

**Answer:** (a)

**Explanation:** (a) is correct. Under *Boyle v. United States*, an associated-in-fact enterprise requires only three structural features: a shared purpose, relationships among those associated with the enterprise, and sufficient longevity to pursue that purpose. Deacon's network, with its hierarchy, meetings, distinct roles, and two-year operational history, easily meets this standard. (b) is wrong because *United States v. Turkette* explicitly established that wholly illegitimate (purely criminal) organizations can qualify as RICO enterprises. (c) is wrong because committing two predicate offenses establishes the "pattern of racketeering activity" element, which must be proven separately from the existence of the "enterprise" itself. (d) is wrong because monopolistic territorial control is not a requirement under *Boyle* or the RICO statute. (e) is wrong because RICO applies to both corporate entities and associated-in-fact individuals; lack of corporate form is not the reason it qualifies.

**Tags:** chapters: [20], topics: [RICO, enterprise, Boyle], difficulty: medium, cognitive: application

**Grounding:** Chapter 20, boyle-three-part

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX - The stem completely lacks a fact pattern. It refers to "Deacon and his network" but provides no facts about their relationships, shared purpose, or longevity. The explanation relies on "hierarchy, meetings, distinct roles, and two-year operational history," which are completely absent from the prompt. A student cannot evaluate the application of the Boyle test without these facts.
check 5: pass
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Incorporate the missing factual context directly into the stem. For example: "Assume prosecutors charge Deacon and his fentanyl distribution network under the federal Racketeer Influenced and Corrupt Organizations (RICO) Act. The network features regular meetings, distinct distribution roles among its members, and a two-year operational history. Under the Boyle test, does the operation qualify as an associated-in-fact 'enterprise'?"
-->
