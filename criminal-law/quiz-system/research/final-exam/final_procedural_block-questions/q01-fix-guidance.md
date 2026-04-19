# Fix Guidance for q01

The QA pipeline flagged this question. Rewrite `q01.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — grounding

**Q1.** Based on Kevin's operation of the waste management company to run his narcotics network, does WasteCorp satisfy the "enterprise" element under federal RICO statutes?

(a) Yes, because a legitimate corporate entity systematically used to facilitate an ongoing pattern of racketeering activity legally qualifies as an enterprise under the broad federal RICO statutes. <!-- correct -->
(b) Yes, because a valid enterprise exists anytime an individual personally commits multiple federal narcotics offenses over a sustained period of commercial business within a single geographic region.
(c) No, because federal RICO statutes strictly require that the enterprise be formed exclusively for illicit purposes, whereas WasteCorp also functions as a legitimate commercial waste management company.
(d) No, because Kevin is acting as the singular executive decision-maker, and a legally valid enterprise strictly requires a decentralized management structure to qualify under the RICO statutes.
(e) No, because federal RICO laws strictly limit the definition of an enterprise to informal associations-in-fact rather than officially incorporated commercial business entities like the WasteCorp waste management organization.

**Answer:** (a)

**Explanation:** Under RICO, an "enterprise" includes legitimate corporate entities that are utilized to facilitate an ongoing pattern of racketeering activity. WasteCorp is a legal corporate entity, and Kevin's use of its payroll and fleet to run a drug network satisfies this element, making (a) correct. (b) is incorrect because an individual committing crimes does not automatically create an enterprise without an ascertainable structure. (c) is incorrect because an enterprise need not be exclusively illicit; legitimate businesses often qualify. (d) is incorrect because a single individual can operate a valid enterprise without a highly decentralized management structure. (e) is incorrect because RICO explicitly encompasses both formal legal entities and informal associations-in-fact.

**Tags:** chapters: [11], topics: [RICO, enterprise liability], difficulty: easy, cognitive: application

**Grounding:** Federal RICO statutes define "enterprise" to include legitimate legal entities (e.g., corporations and partnerships) that are used as vehicles to facilitate a pattern of racketeering activity.

<!-- GROUNDING-FAIL: RICO enterprise liability is not in any chapter map. The closest taught doctrines are: None (meta-map and focus maps are missing from the prompt, and RICO is generally outside standard 1L curriculum). Correct answer must rely on one of those instead. -->

## Issue 2 — audit

**Q1.** Based on Kevin's operation of the waste management company to run his narcotics network, does WasteCorp satisfy the "enterprise" element under federal RICO statutes?

(a) Yes, because a legitimate corporate entity systematically used to facilitate an ongoing pattern of racketeering activity legally qualifies as an enterprise under the broad federal RICO statutes. <!-- correct -->
(b) Yes, because a valid enterprise exists anytime an individual personally commits multiple federal narcotics offenses over a sustained period of commercial business within a single geographic region.
(c) No, because federal RICO statutes strictly require that the enterprise be formed exclusively for illicit purposes, whereas WasteCorp also functions as a legitimate commercial waste management company.
(d) No, because Kevin is acting as the singular executive decision-maker, and a legally valid enterprise strictly requires a decentralized management structure to qualify under the RICO statutes.
(e) No, because federal RICO laws strictly limit the definition of an enterprise to informal associations-in-fact rather than officially incorporated commercial business entities like the WasteCorp waste management organization.

**Answer:** (a)

**Explanation:** Under RICO, an "enterprise" includes legitimate corporate entities that are utilized to facilitate an ongoing pattern of racketeering activity. WasteCorp is a legal corporate entity, and Kevin's use of its payroll and fleet to run a drug network satisfies this element, making (a) correct. (b) is incorrect because an individual committing crimes does not automatically create an enterprise without an ascertainable structure. (c) is incorrect because an enterprise need not be exclusively illicit; legitimate businesses often qualify. (d) is incorrect because a single individual can operate a valid enterprise without a highly decentralized management structure. (e) is incorrect because RICO explicitly encompasses both formal legal entities and informal associations-in-fact.

**Tags:** chapters: [11], topics: [RICO, enterprise liability], difficulty: easy, cognitive: application

**Grounding:** Federal RICO statutes define "enterprise" to include legitimate legal entities (e.g., corporations and partnerships) that are used as vehicles to facilitate a pattern of racketeering activity.

<!-- audit: MUST FIX
<check 1>: pass
<check 2>: pass
<check 3>: pass
<check 4>: fail. The question is entirely missing its factual stem. The stub begins "Based on Kevin's operation..." assuming the student has read a preceding fact pattern. Furthermore, the explanation references specific facts ("use of its payroll and fleet") that do not appear anywhere in the provided text.
<check 5>: pass
<check 6>: pass
<check 7>: pass
<check 8>: pass
Recommended fix: Prepend the missing factual stem to the question so that students have the necessary context (e.g., Kevin's ownership of WasteCorp and his use of its payroll and fleet to distribute narcotics).
-->
