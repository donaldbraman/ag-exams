# Fix Guidance for q06

The QA pipeline flagged this question. Rewrite `q06.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q6.** Assume that Steve's actions qualify as participation in the enterprise, but he did not agree to personally commit any predicate narcotics offenses. Under the *Salinas* doctrine, is Steve guilty of RICO conspiracy?

(a) Steve is guilty of RICO conspiracy because he knew about the broader enterprise's activities and agreed to facilitate them, even if he did not personally commit predicate acts. <!-- correct -->
(b) Steve is guilty of RICO conspiracy because his formal legal representation of the enterprise automatically makes him a co-conspirator to all of their substantive racketeering offenses.
(c) Steve is not guilty of RICO conspiracy because a defendant must explicitly agree to personally commit at least two predicate acts to satisfy the statutory agreement requirement.
(d) Steve is not guilty of RICO conspiracy because his specific role was strictly limited to logistical planning, which completely falls outside the statutory definition of racketeering activity.
(e) Steve is not guilty of RICO conspiracy because an outside independent contractor cannot legally be considered a member of a criminal enterprise under the federal racketeering laws.

**Answer:** (a)

**Explanation:** Under the *Salinas* doctrine, a defendant can be convicted of a RICO conspiracy if they agree to facilitate the broader criminal enterprise, even without agreeing to personally commit the substantive predicate acts. Steve's agreement to provide logistical support for the network satisfies this requirement, making (a) correct. (b) is incorrect because legal representation alone does not automatically create conspiratorial liability without an agreement to facilitate the enterprise. (c) is incorrect because *Salinas* specifically rejected the requirement that a conspirator must explicitly agree to personally commit predicate acts. (d) is incorrect because facilitating the enterprise's racketeering through logistics is sufficient for conspiracy, even if logistics isn't a predicate act itself. (e) is incorrect because outside contractors can legally join a RICO conspiracy.

**Tags:** chapters: [11, 14], topics: [RICO conspiracy, Salinas, enterprise liability], difficulty: hard, cognitive: analysis

**Grounding:** Under Salinas v. United States, a defendant can be guilty of RICO conspiracy if they adopt the goal of furthering the enterprise, even if they do not agree to personally commit the requisite predicate acts.

<!-- GROUNDING-FAIL: Salinas doctrine is not in any chapter map. The closest taught doctrines are: none available (meta-map missing). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q6.** Assume that Steve's actions qualify as participation in the enterprise, but he did not agree to personally commit any predicate narcotics offenses. Under the *Salinas* doctrine, is Steve guilty of RICO conspiracy?

(a) Steve is guilty of RICO conspiracy because he knew about the broader enterprise's activities and agreed to facilitate them, even if he did not personally commit predicate acts. <!-- correct -->
(b) Steve is guilty of RICO conspiracy because his formal legal representation of the enterprise automatically makes him a co-conspirator to all of their substantive racketeering offenses.
(c) Steve is not guilty of RICO conspiracy because a defendant must explicitly agree to personally commit at least two predicate acts to satisfy the statutory agreement requirement.
(d) Steve is not guilty of RICO conspiracy because his specific role was strictly limited to logistical planning, which completely falls outside the statutory definition of racketeering activity.
(e) Steve is not guilty of RICO conspiracy because an outside independent contractor cannot legally be considered a member of a criminal enterprise under the federal racketeering laws.

**Answer:** (a)

**Explanation:** Under the *Salinas* doctrine, a defendant can be convicted of a RICO conspiracy if they agree to facilitate the broader criminal enterprise, even without agreeing to personally commit the substantive predicate acts. Steve's agreement to provide logistical support for the network satisfies this requirement, making (a) correct. (b) is incorrect because legal representation alone does not automatically create conspiratorial liability without an agreement to facilitate the enterprise. (c) is incorrect because *Salinas* specifically rejected the requirement that a conspirator must explicitly agree to personally commit predicate acts. (d) is incorrect because facilitating the enterprise's racketeering through logistics is sufficient for conspiracy, even if logistics isn't a predicate act itself. (e) is incorrect because outside contractors can legally join a RICO conspiracy.

**Tags:** chapters: [11, 14], topics: [RICO conspiracy, Salinas, enterprise liability], difficulty: hard, cognitive: analysis

**Grounding:** Under Salinas v. United States, a defendant can be guilty of RICO conspiracy if they adopt the goal of furthering the enterprise, even if they do not agree to personally commit the requisite predicate acts.

<!-- audit: MUST FIX
Check 1: pass
Check 2: pass
Check 3: pass
Check 4: Fails. The stem lacks the facts necessary to make sense of the options. It references "Steve" and states "assume that Steve's actions...", while the options and explanation refer to specific but unstated facts (e.g., "logistical planning", "formal legal representation", "outside independent contractor"). This indicates the question was separated from a broader fact pattern. 
Check 5: pass
Check 6: pass
Check 7: pass
Check 8: pass
Recommended fix: Integrate the missing facts into the stem. For example: "Steve, an outside independent contractor, provided logistical planning and legal representation for a narcotics enterprise. Assume that Steve's actions qualify as participation in the enterprise, but he did not agree to personally commit any predicate narcotics offenses. Under the Salinas doctrine..."
-->
