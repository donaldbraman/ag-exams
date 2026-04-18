# Fix Guidance for q05

The QA pipeline flagged this question. Rewrite `q05.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q5.** Silas is charged with felony murder for the pedestrian's death. Under traditional felony murder rules, is Silas guilty?

(a) Yes, because evading police is an inherently dangerous felony, and the pedestrian's death occurred during his continuous flight and commission of this underlying offense. <!-- correct -->
(b) No, because the pedestrian's death was accidental rather than intentional, negating the required malice aforethought necessary for any murder conviction.
(c) Yes, because any death that occurs during any traffic violation automatically triggers the felony murder rule, regardless of the underlying violation's severity.
(d) No, because the police officers' initial pretextual stop was the actual but-for cause of the pedestrian's death, severing Silas's causal responsibility.
(e) Yes, because the merger doctrine prohibits defendants from raising any independent defenses when a homicide occurs during a high-speed vehicular pursuit.

**Answer:** (a)

**Explanation:** The felony murder rule substitutes the intent to commit a dangerous felony for malice aforethought. Evading police at high speed is an inherently dangerous felony, and the pedestrian was killed during the *res gestae* (flight) of that felony. (b) is wrong because the very purpose of the felony murder rule is to allow murder convictions for unintentional killings during qualifying felonies. (c) is wrong because minor traffic violations (misdemeanors/infractions) do not trigger felony murder. (d) is wrong because the police stop did not force Silas to flee at 90 mph; his voluntary flight is the proximate cause. (e) is wrong because the merger doctrine (*Ireland*) limits felony murder when the underlying felony is assaultive, but does not bar independent defenses altogether.

**Tags:** chapters: [14], topics: [felony-murder, inherently-dangerous-felony, res-gestae], difficulty: easy, cognitive: application

**Grounding:** Chapter 14, Section: Felony Murder Mechanics

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: MUST FIX. The stem completely lacks a fact pattern. It references Silas, a pedestrian's death, a pretextual police stop, and high-speed flight, but none of these facts are provided in the question itself.
check 5: MUST FIX. The prompt asks for an outcome under "traditional felony murder rules," but "evading police" is an unenumerated felony (outside the traditional BARRK offenses). Jurisdictions split on whether unenumerated felonies qualify for FM and whether "inherently dangerous" is assessed in the abstract (elements approach) or as committed (facts approach). The stem fails to stipulate the jurisdiction's rule.
check 6: pass
check 7: pass
check 8: pass
Recommended fix: Insert the missing fact pattern. Revise the stem to stipulate the jurisdictional rule: "Assume the jurisdiction applies the felony murder rule to unenumerated felonies that are inherently dangerous, and classifies high-speed police evasion as an inherently dangerous felony."
-->
