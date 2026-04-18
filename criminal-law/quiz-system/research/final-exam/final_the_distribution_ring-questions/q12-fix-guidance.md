# Fix Guidance for q12

The QA pipeline flagged this question. Rewrite `q12.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — argpass-sonnet

**Q12.** For the purposes of a joint trial and hearsay admissibility, prosecutors argue that the Tuesday turf defense and the Thursday robbery were part of a single overarching conspiracy. Applying the *Kotteakos* "wheel" analogy, is this likely correct?

(a) Yes, because Marcus directed both actions, forming a single wheel conspiracy even if Silas and Darius did not know each other.
(b) No, because Silas and Darius had no shared purpose, mutual awareness, or interdependence, creating separate conspiracies. <!-- correct -->
(c) Yes, because both events targeted Vance, which automatically fuses the separate agreements into a single chain conspiracy.
(d) No, because the turf defense was a violent crime and the robbery was a property crime, meaning they cannot legally belong to the same conspiracy.
(e) Yes, because Marcus's leadership role satisfies the *Pinkerton* requirement that all coconspirators are liable for the acts of the enterprise.

**Answer:** (b)

**Explanation:** (b) is correct. Under *Kotteakos*, an overarching single conspiracy requires the "spokes" to share a "rim"—meaning mutual awareness, interdependence, or a shared common purpose. Silas (hired Thursday for a robbery) and Darius (assigned Tuesday for turf defense) share no rim, making them separate conspiracies. (a) is incorrect because Marcus alone acts as the "hub," but without a rim connecting the spokes, it remains multiple separate conspiracies. (c) is incorrect because targeting the same rival does not create a chain conspiracy without mutual dependence. (d) is incorrect because a single conspiracy can encompass diverse types of criminal acts if the parties share an overarching agreement. (e) is incorrect because *Pinkerton* governs liability for substantive offenses, not the structural scope of the conspiracy itself.

**Tags:** chapters: [19], topics: [conspiracy, kotteakos-wheel, scope], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19: Conspiracy > Liability Limits > Scope: Single vs. Multiple Conspiracies (Kotteakos Wheel)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student could argue that hub-and-spoke conspiracies inherently rely on the central hub to coordinate disparate actors. By orchestrating both the Tuesday and Thursday events, Marcus acts as the unifying center of the enterprise. Therefore, a student might conclude that his overarching direction is sufficient to establish a single conspiracy, even if the "spokes" lack direct contact or knowledge of one another.
(b) Argument-for: Under the precise holding of *Kotteakos*, a central hub interacting with multiple independent spokes creates multiple separate conspiracies, not one single overarching wheel. A single conspiracy requires a "rim" of mutual awareness, interdependence, or shared common purpose to connect the spokes. Because Silas and Darius operated completely independently without a shared rim, this correctly applies the doctrine to find separate conspiracies.
(c) Argument-for: A student could argue that chain conspiracies depend on linked steps toward a shared ultimate goal. Because both events targeted the same individual (Vance), a student might perceive this shared victim as a unifying objective that necessarily binds the separate actions into a single operational chain.
(d) Argument-for: A student might mistakenly believe that specific intent for conspiracy is strictly bound to the nature of the target offense. Because violence and property crimes have fundamentally different elements and objectives, a student could argue they are legally incompatible within a single specific-intent agreement and must be severed.
(e) Argument-for: *Pinkerton* liability allows coconspirators to be held responsible for the reasonably foreseeable acts of others. A student might confuse this substantive liability doctrine with the structural definition of a conspiracy's scope, arguing that Marcus's leadership logically pulls all enterprise acts into one unified vehicle for liability.

Head-to-head: Option (b) is the clear, correct application of *Kotteakos*, accurately identifying that the absence of a "rim" (interdependence/mutual awareness) defeats a single conspiracy claim. Options (c), (d), and (e) are excellent distractors containing hard, falsifiable errors locked with definitive language ("automatically fuses," "cannot legally belong," and explicitly misstating the *Pinkerton* requirement). Option (a) correctly identifies the "hub" dynamic but asserts a false legal conclusion (that a single wheel exists without a rim). However, (a) lacks a locking absolute word (e.g., "solely" or "categorically"), making its falsifiable error slightly softer than the requested close-call standard demands.

Falsifiable claim per distractor:
- (a): "forming a single wheel conspiracy even if Silas and Darius did not know each other" — wrong because under *Kotteakos*, a hub without a shared purpose or mutual awareness (a rim) creates multiple conspiracies, not a single wheel. (Note: missing an absolute lock).
- (c): "which automatically fuses the separate agreements into a single chain conspiracy" — wrong because a shared victim does not automatically create a chain conspiracy without mutual dependence or a continuous overarching agreement.
- (d): "meaning they cannot legally belong to the same conspiracy" — wrong because a single overarching conspiracy can categorically encompass multiple distinct types of crimes (e.g., both violence and property crimes) if there is a unified agreement.
- (e): "satisfies the Pinkerton requirement that all coconspirators are liable for the acts of the enterprise" — wrong because *Pinkerton* dictates liability for substantive crimes committed in furtherance of a conspiracy, but it does not define the structural scope of the conspiracy itself.

Recommended fix: Edit (a) to lock the false proposition with an absolute word. Change to: "(a) Yes, solely because Marcus directed both actions, which automatically forms a single wheel conspiracy even if Silas and Darius did not know each other."
-->

## Issue 3 — argpass-opus

**Q12.** For the purposes of a joint trial and hearsay admissibility, prosecutors argue that the Tuesday turf defense and the Thursday robbery were part of a single overarching conspiracy. Applying the *Kotteakos* "wheel" analogy, is this likely correct?

(a) Yes, because Marcus directed both actions, forming a single wheel conspiracy even if Silas and Darius did not know each other.
(b) No, because Silas and Darius had no shared purpose, mutual awareness, or interdependence, creating separate conspiracies. <!-- correct -->
(c) Yes, because both events targeted Vance, which automatically fuses the separate agreements into a single chain conspiracy.
(d) No, because the turf defense was a violent crime and the robbery was a property crime, meaning they cannot legally belong to the same conspiracy.
(e) Yes, because Marcus's leadership role satisfies the *Pinkerton* requirement that all coconspirators are liable for the acts of the enterprise.

**Answer:** (b)

**Explanation:** (b) is correct. Under *Kotteakos*, an overarching single conspiracy requires the "spokes" to share a "rim"—meaning mutual awareness, interdependence, or a shared common purpose. Silas (hired Thursday for a robbery) and Darius (assigned Tuesday for turf defense) share no rim, making them separate conspiracies. (a) is incorrect because Marcus alone acts as the "hub," but without a rim connecting the spokes, it remains multiple separate conspiracies. (c) is incorrect because targeting the same rival does not create a chain conspiracy without mutual dependence. (d) is incorrect because a single conspiracy can encompass diverse types of criminal acts if the parties share an overarching agreement. (e) is incorrect because *Pinkerton* governs liability for substantive offenses, not the structural scope of the conspiracy itself.

**Tags:** chapters: [19], topics: [conspiracy, kotteakos-wheel, scope], difficulty: hard, cognitive: analysis

**Grounding:** Chapter 19: Conspiracy > Liability Limits > Scope: Single vs. Multiple Conspiracies (Kotteakos Wheel)

<!-- argument-pass: SHOULD FIX
(a) Argument-for: A student might select this by focusing on the "hub" element of the *Kotteakos* analogy. Since Marcus is the central figure organizing and directing the criminal activities, his overarching leadership arguably creates a unified enterprise. In complex conspiracies, subordinates (spokes) do not always need to interact directly to be part of the same wheel, so long as the hub connects them. Thus, Marcus's central role arguably justifies treating the acts as a single wheel conspiracy.
(b) Argument-for: This is the legally correct application of the rule from *Kotteakos v. United States*. A single wheel conspiracy requires not just a central "hub" (Marcus) but also an outer "rim" to enclose the spokes (Silas and Darius). The rim requires mutual awareness, a shared common purpose, or economic interdependence among the spokes. Because the Tuesday and Thursday actors lacked these connections, the law treats them as two separate conspiracies, not a single overarching one.
(c) Argument-for: A student could argue that the identity of the victim (Vance) supplies the necessary unifying thread for a conspiracy. In conspiracy law, shared objectives are critical. If both the turf defense and the robbery were directed at destroying Vance, they arguably serve the exact same overarching goal. This shared target might lead a student to conclude that the discrete events are transformed into interconnected links of a single chain conspiracy.
(d) Argument-for: A student might choose this based on the principle that the precise scope of an agreement defines a conspiracy. A turf defense involves violent confrontation, while a robbery is primarily an acquisitive property offense. Because the acts require fundamentally different types of *mens rea* and criminal mechanics, a student could logically deduce that they cannot stem from the same singular conspiratorial agreement without a broader explicit RICO-like enterprise charge.
(e) Argument-for: This option appeals to students who remember that *Pinkerton* expands the scope of criminal liability within a conspiracy. If Marcus is the leader of both operations, *Pinkerton* makes coconspirators liable for foreseeable acts in furtherance of the broader conspiracy. A student might mistakenly reason that because Marcus faces overarching liability for both actions under his leadership umbrella, the legal framework explicitly fuses the enterprise into one single overarching conspiracy.

Head-to-head: Option (b) correctly applies the specific structural requirement of *Kotteakos*, noting the lack of a "rim" (interdependence/awareness). Distractor (a) is highly tempting but legally insufficient under *Kotteakos*, though its lack of absolute phrasing makes it borderline on strict falsifiability. Distractor (c) provides an excellent falsifier ("automatically fuses") and mistakenly swaps the wheel analogy for a "chain" conspiracy (which requires sequential dependence, not parallel independent strikes). Distractor (d) invents a categorical bar ("cannot legally belong") against combining violent and property crimes. Distractor (e) misapplies *Pinkerton*, incorrectly treating a rule of substantive vicarious liability as the threshold test for whether an overarching conspiracy exists in the first place. 

Falsifiable claim per distractor:
- (a): "forming a single wheel conspiracy even if Silas and Darius did not know each other." — wrong because while spokes do not strictly need to know each other *if* they have interdependence, Marcus's direction alone is insufficient to form the single wheel; however, the lack of an absolute word ("solely") relies slightly on implicit omission of the rim requirement. 
- (c): "automatically fuses the separate agreements into a single chain conspiracy." — wrong because a common target does not automatically create a single conspiracy, nor does parallel targeting fit the legal definition of a sequential "chain" conspiracy.
- (d): "meaning they cannot legally belong to the same conspiracy." — wrong because a single conspiratorial agreement can categorically encompass multiple disparate crimes, including both violent and property offenses.
- (e): "satisfies the Pinkerton requirement that all coconspirators are liable for the acts of the enterprise." — wrong because *Pinkerton* dictates substantive liability for completed offenses, not the structural scope (single vs. multiple) of the conspiracy itself.

Recommended fix: To strictly adhere to the close-call standard and lock (a) as definitively falsifiable without relying on omission, edit (a) to use an absolute phrasing: "(a) Yes, solely because Marcus directed both actions, which automatically forms a single wheel conspiracy regardless of whether Silas and Darius shared any interdependence."
-->
