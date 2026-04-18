# Fix Guidance for q03

The QA pipeline flagged this question. Rewrite `q03.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

**Q3.** Marlowe is charged under the federal statute for storing hazardous chemicals without a permit. The statute is silent on mental state and carries up to 10 years in prison. Must the prosecution prove Marlowe knew the chemicals were hazardous?

(a) Yes, because the severe ten-year penalty rebuts the public welfare exception and triggers a presumption of a mens rea requirement. <!-- correct -->
(b) Yes, because the statute expressly states that the storage must be done "knowingly" or "purposely" to constitute a felony.
(c) No, because the statute is entirely silent on mental state, which automatically designates it as a strict liability offense.
(d) No, because dealing with hazardous chemicals puts Marlowe on notice that his conduct is highly regulated by the government.
(e) No, because federal courts refuse to read mens rea requirements into statutes that protect community health and public safety.

**Answer:** (a)

**Explanation:** (a) is correct because under *Staples v. United States*, severe felony penalties (like 10 years) strongly signal that Congress did not intend to create a strict-liability public welfare offense, triggering the *Morissette* presumption of mens rea. (b) fails factually because the statute is "entirely silent" on mental state. (c) fails because statutory silence does not automatically mean strict liability; courts presume mens rea. (d) fails because while the dangerous-items heuristic applies to chemicals, the severe penalty limits its application under *Staples*. (e) fails because federal courts routinely read mens rea into public safety statutes (*Morissette*).

**Tags:** chapters: [10, 11], topics: [morissette presumption, staples outlier, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 11 - Public Welfare Offenses (Staples as Outlier — Serious Penalties Presumed to Require Mens Rea)

<!-- audit: MUST FIX
<check 1>: fails. The categorical assertion in (a) that a "severe ten-year penalty rebuts the public welfare exception" is doctrinally incomplete. A prepared student will know that in *United States v. Freed*, the Supreme Court upheld the PWO exception for unregistered hand grenades despite a 10-year penalty. *Staples* distinguished *Freed* not just on the penalty, but on the "normative categories" of the items (guns are traditionally lawful; hand grenades are not). Because "hazardous chemicals" are inherently dangerous, they arguably fit the *Freed* / *International Minerals* PWO exception despite the 10-year penalty.
<check 2>: fails. A smart student could easily mount a credible argument for (d). "Hazardous chemicals" are the classic dangerous/highly-regulated item (*United States v. International Minerals & Chemical Corp.*), meaning Marlowe is on notice. If the item is inherently dangerous, the 10-year penalty does not automatically bar the PWO exception (as proven by *Freed*), making (d) arguably the better legal answer than (a). 
<check 3>: fails. The explanation overstates the holding of *Staples* by ignoring the `staples-normative-categories` tag from the chapter map, which limits the "severe penalty" heuristic when dealing with inherently dangerous items. 
<check 4>: pass. The stem contains the necessary facts, though the facts conflict with the intended doctrine.
<check 5>: pass. The stem specifies a federal statute, clearly invoking federal *Morissette*/*Staples* doctrine.
<check 6>: pass. No excluded-topic bleed.
<check 7>: pass. The doctrines are clearly grounded in Chapter 11 (Public Welfare Offenses).
Recommended fix: Change the regulated item in the stem from "hazardous chemicals" to something traditionally lawful and innocent (e.g., "ordinary household fertilizer" or "a standard semi-automatic hunting rifle"). This completely disables the dangerous-items heuristic in (d), cleanly aligning the "innocent item" logic with the "severe penalty" logic under *Staples* to make (a) indisputably correct.
-->

## Issue 2 — argpass-sonnet

**Q3.** Marlowe is charged under the federal statute for storing hazardous chemicals without a permit. The statute is silent on mental state and carries up to 10 years in prison. Must the prosecution prove Marlowe knew the chemicals were hazardous?

(a) Yes, because the severe ten-year penalty rebuts the public welfare exception and triggers a presumption of a mens rea requirement. <!-- correct -->
(b) Yes, because the statute expressly states that the storage must be done "knowingly" or "purposely" to constitute a felony.
(c) No, because the statute is entirely silent on mental state, which automatically designates it as a strict liability offense.
(d) No, because dealing with hazardous chemicals puts Marlowe on notice that his conduct is highly regulated by the government.
(e) No, because federal courts refuse to read mens rea requirements into statutes that protect community health and public safety.

**Answer:** (a)

**Explanation:** (a) is correct because under *Staples v. United States*, severe felony penalties (like 10 years) strongly signal that Congress did not intend to create a strict-liability public welfare offense, triggering the *Morissette* presumption of mens rea. (b) fails factually because the statute is "entirely silent" on mental state. (c) fails because statutory silence does not automatically mean strict liability; courts presume mens rea. (d) fails because while the dangerous-items heuristic applies to chemicals, the severe penalty limits its application under *Staples*. (e) fails because federal courts routinely read mens rea into public safety statutes (*Morissette*).

**Tags:** chapters: [10, 11], topics: [morissette presumption, staples outlier, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 11 - Public Welfare Offenses (Staples as Outlier — Serious Penalties Presumed to Require Mens Rea)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could rely on *Staples v. United States* and *Morissette v. United States*, arguing that the presumption of mens rea applies when a statute is silent. The presence of a severe 10-year felony penalty strongly signals that Congress did not intend to create a strict-liability public welfare offense, even for traditionally dangerous items. Thus, the prosecution must prove knowledge of the factual elements that make the conduct illegal.
(b) Argument-for: A student might argue that for a 10-year felony, constitutional due process requires the statute to effectively include "knowingly" or "purposely." By reading the necessary constitutional floor into the statute, they could conclude the statute "expressly" operates this way in practice under federal common law.
(c) Argument-for: A student leaning heavily on plain-meaning textualism might argue that courts should not rewrite statutes. If Congress leaves a statute entirely silent on mental state, the default textual interpretation is strict liability, as the text contains no subjective requirements. The "automatically" wording appeals to this rigid, bright-line textualist rule.
(d) Argument-for: A student could cite *United States v. International Minerals* or *United States v. Dotterweich*, arguing that hazardous chemicals are quintessential public welfare items. Because these materials are inherently dangerous, individuals dealing with them are on notice of strict regulation, excusing the need for mens rea. The reasoning aligns perfectly with the historical justification for public welfare offenses.
(e) Argument-for: A student could argue that the paramount purpose of public welfare offenses is to protect community health. Because of the vital importance of these interests, federal courts strictly refuse to read mens rea requirements into such regulatory statutes, preferring to place the burden on the actor rather than the vulnerable public.

Head-to-head: Option (a) correctly applies the *Staples* limitation on the public welfare doctrine, noting that a severe penalty triggers the *Morissette* presumption of mens rea. Option (b) fails because it directly contradicts the prompt's premise that the statute is silent. Option (c) relies on a false legal rule, as statutory silence does not automatically create strict liability. Option (e) uses the absolute word "refuse," making it demonstrably false since courts routinely read mens rea into public safety statutes (*Staples*). Option (d), however, relies on an entirely true premise—that dealing with hazardous chemicals puts an actor on notice of regulation—but reaches the wrong conclusion due to an unstated omission (ignoring the 10-year penalty). Because (d) lacks an explicit, absolute false claim and relies purely on an implicit omission, it violates the close-call standard.

Falsifiable claim per distractor:
- (b): "expressly states that the storage must be done 'knowingly' or 'purposely'" — wrong because it explicitly contradicts the stipulated fact in the prompt that the statute is silent on mental state.
- (c): "entirely silent on mental state, which automatically designates it as a strict liability offense" — wrong because statutory silence triggers a common law presumption of mens rea under *Morissette*, not automatic strict liability.
- (d): None. The claim "dealing with hazardous chemicals puts Marlowe on notice that his conduct is highly regulated" is legally true (*Int'l Minerals*). The distractor fails only because it omits the *Staples* severe-penalty exception. 
- (e): "federal courts refuse to read mens rea requirements into statutes" — wrong because federal courts frequently do read mens rea into such statutes when penalties are severe.

Recommended fix: Edit (d) to include a locked falsifiable claim. For example: "(d) No, because dealing with hazardous chemicals categorically exempts the statute from any mens rea requirement, regardless of the penalty's severity."
-->

## Issue 3 — argpass-opus

**Q3.** Marlowe is charged under the federal statute for storing hazardous chemicals without a permit. The statute is silent on mental state and carries up to 10 years in prison. Must the prosecution prove Marlowe knew the chemicals were hazardous?

(a) Yes, because the severe ten-year penalty rebuts the public welfare exception and triggers a presumption of a mens rea requirement. <!-- correct -->
(b) Yes, because the statute expressly states that the storage must be done "knowingly" or "purposely" to constitute a felony.
(c) No, because the statute is entirely silent on mental state, which automatically designates it as a strict liability offense.
(d) No, because dealing with hazardous chemicals puts Marlowe on notice that his conduct is highly regulated by the government.
(e) No, because federal courts refuse to read mens rea requirements into statutes that protect community health and public safety.

**Answer:** (a)

**Explanation:** (a) is correct because under *Staples v. United States*, severe felony penalties (like 10 years) strongly signal that Congress did not intend to create a strict-liability public welfare offense, triggering the *Morissette* presumption of mens rea. (b) fails factually because the statute is "entirely silent" on mental state. (c) fails because statutory silence does not automatically mean strict liability; courts presume mens rea. (d) fails because while the dangerous-items heuristic applies to chemicals, the severe penalty limits its application under *Staples*. (e) fails because federal courts routinely read mens rea into public safety statutes (*Morissette*).

**Tags:** chapters: [10, 11], topics: [morissette presumption, staples outlier, mens rea], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 11 - Public Welfare Offenses (Staples as Outlier — Serious Penalties Presumed to Require Mens Rea)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: Under the *Morissette* line of cases, federal criminal statutes are generally presumed to require a mens rea even if they are silent on the matter. While the public welfare exception (*Balint*, *Dotterweich*) removes this requirement for certain dangerous items, *Staples v. United States* establishes that a severe felony penalty (such as 10 years in prison) rebuts this exception. Therefore, the general presumption of mens rea survives, and the prosecution must prove Marlowe knew the factual nature of the items he possessed.
(b) Argument-for: A student might argue that general federal code construction principles or background Model Penal Code rules automatically read "knowingly" or "purposely" into felony statutes to avoid strict liability. If a student mistakenly believes this background interpretive presumption operates as an "express" statutory provision in the federal system, they might select this option despite the prompt's language.
(c) Argument-for: A strict textualist reading suggests that when a legislature omits a mens rea term, it intends strict liability. Some strict liability offenses (like statutory rape in certain jurisdictions) operate precisely by statutory silence. A student might argue that for a regulatory offense like chemical storage, statutory silence automatically means the legislature intended a strict liability regime.
(d) Argument-for: The doctrine of public welfare offenses, articulated in cases like *United States v. International Minerals & Chem. Corp.*, holds that individuals handling inherently dangerous or highly regulated materials are put on notice of the likelihood of regulation. Because Marlowe is dealing with hazardous chemicals, a student could argue he assumes the risk of strict liability. This perfectly aligns with the historical justification for dispensing with mens rea in environmental and public health contexts, making it a highly attractive answer.
(e) Argument-for: The public welfare exception was specifically created because requiring mens rea would obstruct the enforcement of laws designed to protect community health and public safety. Cases like *Balint* explicitly dispensed with mens rea to protect the public from dangerous goods. Thus, a student could argue that federal courts categorically refuse to read mens rea into such protective statutes in order to maintain their vital deterrent effect.

Head-to-head: Option (a) is the clear correct answer because it accurately synthesizes the *Morissette* presumption with the *Staples* limitation on public welfare offenses. Option (b) fails on a blatant factual contradiction with the prompt. Option (c) fails because of its absolute claim that silence "automatically designates" strict liability, contradicting *Morissette*. Option (e) fails because of its absolute claim that federal courts "refuse to read" mens rea into public safety statutes, which is demonstrably false. Option (d) is the strongest distractor because its legal principle (notice of regulation for dangerous chemicals) is historically accurate under *International Minerals*; its only flaw is an implicit omission of the *Staples* penalty limitation. Because (d) lacks an explicit, absolute falsifiable claim, it violates the close-call standard and must be fixed.

Falsifiable claim per distractor:
- (b): "the statute expressly states" — wrong because the prompt explicitly stipulates "The statute is silent on mental state".
- (c): "automatically designates it as a strict liability offense" — wrong because federal law (*Morissette*) applies a strong presumption of mens rea to silent statutes.
- (d): NO EXPLICIT FALSIFIABLE CLAIM. It relies on an implicit omission (it ignores the 10-year penalty exception) rather than an explicitly false proposition.
- (e): "federal courts refuse to read mens rea requirements" — wrong because federal courts routinely read mens rea into public safety statutes, especially when penalties are severe (*Staples*).

Recommended fix: Add an absolute locking phrase to (d) to make it explicitly false. Change (d) to: "No, because dealing with hazardous chemicals puts Marlowe on notice that his conduct is highly regulated, which categorically overrides the need for a mens rea requirement regardless of the penalty."
-->
