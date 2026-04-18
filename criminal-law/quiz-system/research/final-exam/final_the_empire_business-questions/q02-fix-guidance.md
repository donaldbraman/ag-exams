# Fix Guidance for q02

The QA pipeline flagged this question. Rewrite `q02.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q2.** Assume the U.S. Attorney wants to charge Carmine with RICO conspiracy for the narcotics agreement. Is Carmine guilty of RICO conspiracy?

(a) Guilty of RICO conspiracy, because an agreement to form a future enterprise constitutes a completed RICO conspiracy offense even if the enterprise does not yet exist. <!-- correct -->
(b) Not guilty of RICO conspiracy, because the substantive RICO offense requires the existence of a fully formed enterprise at the time the agreement is reached.
(c) Guilty of RICO conspiracy, because Carmine had already established Pinnacle Waste and the new syndicate would merely operate as a subsidiary of that existing enterprise.
(d) Not guilty of RICO conspiracy, because neither Carmine nor Dominic had committed any predicate acts in furtherance of the planned future narcotics syndicate at that time.
(e) Guilty of RICO conspiracy, because the agreement involved the distribution of narcotics which automatically satisfies the pattern of racketeering requirement under the federal RICO statute.

**Answer:** (a)

**Explanation:** Under United States v. Rich, an agreement to associate with and participate in a yet-to-be-formed racketeering enterprise constitutes a completed RICO conspiracy offense. The enterprise does not need to exist at the time of the agreement. (b) is incorrect because the Sixth Circuit explicitly held that a future enterprise satisfies the conspiracy element. (c) is incorrect because the facts state they agreed to form a "new, separate" syndicate, making its status as a subsidiary factually incorrect and legally unnecessary. (d) is incorrect because under Salinas v. United States, a RICO conspirator does not need to personally commit predicate acts; the agreement itself is the crime. (e) is incorrect because while narcotics distribution is a predicate act, RICO requires an agreement to conduct the affairs of an enterprise through a pattern of racketeering, not merely a standard drug conspiracy.

**Tags:** chapters: [20], topics: [RICO, conspiracy, future enterprise, Salinas], difficulty: hard, cognitive: application

**Grounding:** United States v. Rich; Salinas v. United States

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fail. The question stem is missing the required factual context (it references "Carmine", "Dominic", "the narcotics agreement", and "Pinnacle Waste" but provides no facts about them). It appears to be a dependent question separated from a master fact pattern.
check 5: fail. The explanation justifies ruling out option (b) by stating "the Sixth Circuit explicitly held...". Because RICO is a federal statute subject to circuit splits, treating a specific circuit's ruling as universal black-letter law without stipulating the jurisdiction or asking about the rule in *Rich* violates the jurisdictional clarity requirement.
check 6: pass
check 7: pass
Recommended fix: (1) Integrate the necessary facts into the stem (or ensure it is explicitly paired with its master fact pattern). (2) Add a jurisdictional stipulation to the stem, such as: "Assume the applicable jurisdiction follows the rule from United States v. Rich."
-->
