# Fix Guidance for q14

The QA pipeline flagged this question. Rewrite `q14.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q14.** The prosecution seeks to charge Dom with possession with intent to distribute (PWID) rather than simple possession. What is the strongest basis for inferring an intent to distribute?

(a) The fentanyl was found hidden in a vehicle that was actively being used by the defendants to flee from pursuing police officers.
(b) The sheer quantity of one kilogram is completely inconsistent with personal use and strongly implies an intent to engage in commercial distribution. <!-- correct -->
(c) The vacuum-sealed packaging conclusively proves that the illicit drugs were recently transported across state lines by a highly organized criminal enterprise.
(d) Dom's prior involvement in an armed hijacking conspiracy establishes his general criminal intent to commit commercial offenses involving illegal narcotics distribution.
(e) The presence of another person inside the getaway vehicle satisfies the strict legal requirement of having an intended recipient for the drugs.

**Answer:** (b)

**Explanation:** In narcotics prosecutions, the sheer quantity of the drugs is a primary factor used to distinguish simple possession from possession with intent to distribute. One kilogram of fentanyl is an enormous quantity that is completely inconsistent with personal consumption, strongly implying commercial distribution. Option (a) is wrong because fleeing police indicates consciousness of guilt, but not necessarily an intent to distribute. Option (c) is wrong because vacuum-sealed packaging relates to preservation or concealment, not necessarily the crossing of state lines. Option (d) is wrong because prior involvement in unrelated crimes (hijacking) is generally inadmissible character evidence and does not prove specific intent for narcotics. Option (e) is wrong because the mere presence of a co-defendant does not legally satisfy the element of an intended buyer.

**Tags:** chapters: [15], topics: [possession with intent to distribute, quantity inferences], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: qty-pwid

<!-- audit: MUST FIX
check 1: pass
check 2: pass
check 3: pass
check 4: fails. The question is entirely missing the fact pattern it relies upon. The options refer to specific scenario details ("The fentanyl," "one kilogram," "vacuum-sealed," "prior involvement in an armed hijacking") that are nowhere in the stem. This appears to be an orphaned question from a multi-question scenario block.
check 5: pass
check 6: pass
check 7: pass
Recommended fix: Inject the necessary facts into the question stem so it functions as a standalone question (e.g., "Dom is caught fleeing police in a getaway vehicle containing one kilogram of vacuum-sealed fentanyl. Dom also has a prior conviction for armed hijacking. The prosecution seeks...").
-->

## Issue 2 — argpass-sonnet

**Q14.** The prosecution seeks to charge Dom with possession with intent to distribute (PWID) rather than simple possession. What is the strongest basis for inferring an intent to distribute?

(a) The fentanyl was found hidden in a vehicle that was actively being used by the defendants to flee from pursuing police officers.
(b) The sheer quantity of one kilogram is completely inconsistent with personal use and strongly implies an intent to engage in commercial distribution. <!-- correct -->
(c) The vacuum-sealed packaging conclusively proves that the illicit drugs were recently transported across state lines by a highly organized criminal enterprise.
(d) Dom's prior involvement in an armed hijacking conspiracy establishes his general criminal intent to commit commercial offenses involving illegal narcotics distribution.
(e) The presence of another person inside the getaway vehicle satisfies the strict legal requirement of having an intended recipient for the drugs.

**Answer:** (b)

**Explanation:** In narcotics prosecutions, the sheer quantity of the drugs is a primary factor used to distinguish simple possession from possession with intent to distribute. One kilogram of fentanyl is an enormous quantity that is completely inconsistent with personal consumption, strongly implying commercial distribution. Option (a) is wrong because fleeing police indicates consciousness of guilt, but not necessarily an intent to distribute. Option (c) is wrong because vacuum-sealed packaging relates to preservation or concealment, not necessarily the crossing of state lines. Option (d) is wrong because prior involvement in unrelated crimes (hijacking) is generally inadmissible character evidence and does not prove specific intent for narcotics. Option (e) is wrong because the mere presence of a co-defendant does not legally satisfy the element of an intended buyer.

**Tags:** chapters: [15], topics: [possession with intent to distribute, quantity inferences], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: qty-pwid

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Fleeing from the police with hidden drugs shows a high degree of consciousness of guilt and a desperation to protect a valuable illicit asset. The active use of a vehicle to evade law enforcement suggests the defendants knew the high stakes of their cargo. A student could argue that such evasive tactics are highly characteristic of drug runners protecting commercial inventory, making it a strong circumstantial basis for inferring an intent to distribute.
(b) Argument-for: In narcotics prosecutions, quantity is the most universally recognized circumstantial evidence of intent to distribute. One kilogram of fentanyl is an enormous amount that is vastly beyond any conceivable quantity for personal consumption. A student would correctly identify that established case law consistently holds such exorbitant quantities as sufficient to strongly imply commercial distribution.
(c) Argument-for: Vacuum-sealed packaging is a well-known method used by traffickers to mask odors from K-9 units and preserve large quantities of drugs for sale. A student could argue that this professional packaging elevates the possession beyond personal use and "conclusively proves" involvement in an organized enterprise. This level of organization would thereby imply an intent to distribute the illicit drugs.
(d) Argument-for: Under evidentiary rules like FRE 404(b), prior bad acts can sometimes be admitted to prove specific intent or plan. A student could argue that prior involvement in a severe commercial crime like armed hijacking shows a broader general criminal intent. Therefore, this prior conspiracy establishes the necessary mens rea to commit other commercial offenses, such as narcotics distribution.
(e) Argument-for: To "distribute" legally means to deliver or transfer a controlled substance to another person. A student might argue that the presence of another person in the getaway vehicle provides an immediate, tangible intended recipient for the drugs. Thus, their presence "satisfies the strict legal requirement" of having a buyer, proving the intent to distribute element.

Head-to-head: Option (b) is the correct answer because an inexplicably large quantity of drugs is the hallmark legal basis for inferring intent to distribute. Options (c), (d), and (e) are effectively falsified by absolute or incorrect legal claims: vacuum-sealing does not "conclusively prove" interstate transport, an unrelated hijacking does not legally establish specific intent for drug distribution, and there is no "strict legal requirement" of an intended recipient for PWID. However, option (a) merely states a factual scenario (fleeing police) without making any explicit false legal claim. While fleeing is not the *strongest* basis for PWID, the lack of a falsifiable legal proposition in (a) makes it fail the strict distractor standard.

Falsifiable claim per distractor:
- (a): None. The option merely states a factual premise without an identifiable false legal claim, relying on being a weaker inference than (b).
- (c): "conclusively proves that the illicit drugs were recently transported across state lines" — wrong because packaging methods do not conclusively prove interstate transport or highly organized enterprise involvement as a matter of law.
- (d): "establishes his general criminal intent to commit commercial offenses involving illegal narcotics distribution" — wrong because an unrelated armed hijacking does not legally establish specific intent for narcotics offenses.
- (e): "satisfies the strict legal requirement of having an intended recipient" — wrong because there is no strict legal requirement to identify an intended recipient to prove possession with intent to distribute.

Recommended fix: Edit (a) to include an explicit false legal claim. For example: "(a) Fleeing from pursuing police officers with hidden narcotics categorically establishes the specific intent required for commercial drug distribution."
-->

## Issue 3 — argpass-opus

**Q14.** The prosecution seeks to charge Dom with possession with intent to distribute (PWID) rather than simple possession. What is the strongest basis for inferring an intent to distribute?

(a) The fentanyl was found hidden in a vehicle that was actively being used by the defendants to flee from pursuing police officers.
(b) The sheer quantity of one kilogram is completely inconsistent with personal use and strongly implies an intent to engage in commercial distribution. <!-- correct -->
(c) The vacuum-sealed packaging conclusively proves that the illicit drugs were recently transported across state lines by a highly organized criminal enterprise.
(d) Dom's prior involvement in an armed hijacking conspiracy establishes his general criminal intent to commit commercial offenses involving illegal narcotics distribution.
(e) The presence of another person inside the getaway vehicle satisfies the strict legal requirement of having an intended recipient for the drugs.

**Answer:** (b)

**Explanation:** In narcotics prosecutions, the sheer quantity of the drugs is a primary factor used to distinguish simple possession from possession with intent to distribute. One kilogram of fentanyl is an enormous quantity that is completely inconsistent with personal consumption, strongly implying commercial distribution. Option (a) is wrong because fleeing police indicates consciousness of guilt, but not necessarily an intent to distribute. Option (c) is wrong because vacuum-sealed packaging relates to preservation or concealment, not necessarily the crossing of state lines. Option (d) is wrong because prior involvement in unrelated crimes (hijacking) is generally inadmissible character evidence and does not prove specific intent for narcotics. Option (e) is wrong because the mere presence of a co-defendant does not legally satisfy the element of an intended buyer.

**Tags:** chapters: [15], topics: [possession with intent to distribute, quantity inferences], difficulty: easy, cognitive: application

**Grounding:** Chapter 15: qty-pwid

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that actively fleeing from police in a vehicle containing fentanyl demonstrates involvement in a broader criminal enterprise. Flight is well-established as circumstantial evidence of consciousness of guilt. In the context of narcotics, transporting drugs while evading law enforcement might suggest the drugs are en route to a buyer or stash house rather than being held for immediate personal consumption. Therefore, the active transportation and evasion could be viewed as the primary indicator of an ongoing distribution scheme.
(b) Argument-for: In narcotics prosecutions, courts consistently hold that an unusually large quantity of drugs is sufficient circumstantial evidence to infer an intent to distribute. One kilogram of fentanyl represents a massive number of individual doses, far exceeding any plausible amount for personal use. Because such a quantity is inherently inconsistent with mere possession, it serves as the most direct and legally robust basis for a PWID charge. This aligns perfectly with standard prosecutorial practices and jury instructions.
(c) Argument-for: A student could reason that vacuum-sealed packaging is a hallmark of sophisticated drug trafficking operations aiming to evade detection by K-9 units during transit. Because such packaging is commonly associated with bulk transportation, it strongly implies a commercial purpose rather than casual personal use. The argument would conclude that this specialized packaging conclusively ties the drugs to a highly organized enterprise, establishing the necessary intent to distribute.
(d) Argument-for: A student might mistakenly apply the concept of common scheme or general criminal propensity, reasoning that Dom's prior armed hijacking shows a readiness to engage in high-level felonies. Under this flawed logic, involvement in one organized, commercial-type crime establishes a "general commercial criminal intent." The student could argue this prior bad act satisfies the mens rea for intent to distribute illegal narcotics, acting as the strongest evidence of his criminal state of mind.
(e) Argument-for: To distribute drugs, a defendant must ultimately transfer them to another individual. A student could interpret this logical necessity as a strict legal requirement that the prosecution identify an intended recipient. Finding another person inside the getaway vehicle might be seen as satisfying this supposed requirement, proving that Dom had an immediate recipient ready to take delivery of the fentanyl.

Head-to-head: Option (b) is the clear correct answer, as a massive quantity of fentanyl (one kilogram) is the strongest and most universally recognized basis for inferring an intent to distribute. Options (c), (d), and (e) are effectively negated by their inclusion of explicit, falsifiable legal or evidentiary claims: (c) uses "conclusively proves," (d) relies on inadmissible character evidence to "establish" intent, and (e) invents a "strict legal requirement." However, option (a) merely describes a factual scenario (fleeing from police) and relies on the student reasoning that quantity is a stronger factual inference than flight. Because (a) lacks an explicit, absolute false legal claim, it violates the close-call standard.

Falsifiable claim per distractor:
- (a): None. The distractor contains no explicit false legal claim, relying instead on a weak factual inference compared to the correct answer.
- (c): "conclusively proves that the illicit drugs were recently transported across state lines" — wrong because vacuum-sealing does not legally or logically establish a conclusive presumption of interstate transport or enterprise involvement.
- (d): "establishes his general criminal intent to commit commercial offenses involving illegal narcotics distribution" — wrong because prior unrelated bad acts (hijacking) do not legally establish specific intent for a narcotics distribution charge under character evidence rules.
- (e): "satisfies the strict legal requirement of having an intended recipient for the drugs" — wrong because there is no strict legal requirement to prove or identify a specific intended recipient to convict for intent to distribute.

Recommended fix: Change (a) to include an absolute, falsifiable legal claim. For example: "(a) The act of fleeing from pursuing police officers automatically triggers a legal presumption of possession with intent to distribute."
-->
