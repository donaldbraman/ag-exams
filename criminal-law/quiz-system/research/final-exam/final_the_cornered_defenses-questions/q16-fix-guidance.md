# Fix Guidance for q16

The QA pipeline flagged this question. Rewrite `q16.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q16.** Based on the fentanyl found in Trey's vehicle, can Trey be charged with Possession With Intent to Distribute (PWID)?

(a) Yes, because the mere physical presence of fifty grams of fentanyl automatically triggers a strict and mandatory federal presumption of criminal intent to distribute.
(b) No, because he was parked twenty feet away from the vehicle, legally defeating the strictly required element of immediate physical control over the illegal drugs.
(c) Yes, because the car keys in his pocket establish constructive possession, and the distinct baggies and drug ledger support a strong inference of intent to distribute. <!-- correct -->
(d) No, because constructive possession cannot be established for specific items locked inside a hidden compartment unless the targeted defendant is actively driving the car.
(e) Yes, because his widely known status as the syndicate's hitman legally excuses the prosecution from affirmatively proving his personal knowledge of the vehicle's hidden compartment.

**Answer:** (c)

**Explanation:** Possession can be actual or constructive. Trey had constructive possession of the fentanyl because the car keys in his pocket provided him with the power and intent to control the vehicle and its contents, even from twenty feet away. Furthermore, intent to distribute is routinely inferred from circumstantial evidence such as large quantities, individual packaging (25 tiny baggies), and the presence of a drug ledger. (a) is incorrect because while quantity creates an inference for the jury, it does not trigger an automatic mandatory legal presumption. (b) is incorrect because constructive possession specifically exists to criminalize control over contraband even when the defendant lacks immediate, actual physical custody. (d) is incorrect because constructive possession relies on the right and ability to access the space (via the keys), not active operation of the vehicle. (e) is incorrect because status or reputation never excuses the prosecution from proving the elements of the offense, including *mens rea* regarding knowledge of the drugs.

**Tags:** chapters: [15], topics: [constructive possession, PWID inferences], difficulty: medium, cognitive: application

**Grounding:** Chapter 15 - cp-awareness-control, qty-pwid

<!-- audit: MUST FIX
check 1: Correct-answer accuracy fails. Option C states that "car keys in his pocket establish constructive possession." Under `cp-awareness-control`, constructive possession requires both the power to control AND awareness/knowledge of the contraband. Keys alone establish power, but do not automatically establish awareness of drugs inside a *hidden compartment*. A well-prepared student would challenge C as doctrinally incomplete.
check 2: pass
check 3: Explanation consistency fails. The explanation claims the keys "provided him with the power and intent to control." Keys provide physical access (power), but do not inherently establish intent or knowledge of hidden contents.
check 4: The stem lacks the standalone facts required to answer the question, heavily relying on a master scenario that is assumed but omitted here (e.g., the hidden compartment, ledger, and 20-foot distance only emerge in the options).
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Revise Option C to include the knowledge element (e.g., "Yes, because his exclusive control of the vehicle and the keys establish constructive possession..."). Update the explanation to clarify that constructive possession requires both power to control (via keys) AND knowledge of the hidden drugs (which would be inferred from exclusive control or other scenario facts).
-->
