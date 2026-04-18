# Fix Guidance for q04

The QA pipeline flagged this question. Rewrite `q04.md` addressing each numbered issue below. Do NOT delete this guidance file — the pipeline handles it.

## Issue 1 — audit

<!-- audit: MUST FIX -->

**Safety Block Triggered.** The previous version of this question was blocked by Gemini's safety filters as unsafe. Please rewrite the fact pattern to reduce the risk of unsafe content blocking.

Error: Model returned empty or blocked response.

## Issue 2 — edge-case

**Q4.** Assume it is established that Marcus and Darius are members of the same Court Kings drug distribution conspiracy. Can Marcus be held vicariously liable for Darius's attempted murder of Vance?

(a) Yes, under the Pinkerton doctrine, Marcus is liable if the attempted murder of Vance was a reasonably foreseeable consequence and committed in furtherance of their ongoing drug distribution conspiracy. <!-- correct -->
(b) Yes, under the MPC, because conspiracy membership automatically establishes accomplice liability for any foreseeable violent acts committed by coconspirators in the same territory against rival gang members.
(c) No, under the Pinkerton doctrine, because Marcus was not physically present in the vehicle and did not personally authorize or direct Darius to execute the specific hit on Vance.
(d) No, under both approaches, because vicarious liability only attaches to completed substantive offenses, not to inchoate crimes like attempted murder where the target victim is unharmed.
(e) Yes, under the traditional rule, but only if the prosecution proves that Marcus personally supplied the 9mm handgun that Darius used to hunt for Vance on Wednesday night.

**Answer:** (a)

**Explanation:** The correct answer is (a). Under Pinkerton, each conspirator is vicariously liable for the foreseeable substantive offenses of coconspirators committed in furtherance of the ongoing conspiracy, even if they did not personally participate. (b) is wrong because the MPC explicitly rejects Pinkerton liability. (c) is wrong because physical presence and personal authorization are precisely the requirements that Pinkerton dispenses with. (d) is wrong because attempt is a substantive offense that can trigger Pinkerton liability. (e) is wrong because supplying the weapon would be a basis for accomplice liability; Pinkerton does not require such direct facilitation.

**Tags:** chapters: [19], topics: [conspiracy, Pinkerton, vicarious liability], difficulty: medium, cognitive: application

**Grounding:** Chapter 19: pinkerton-doctrine, pinkerton-mpc-rejection

<!-- edge-case-audit: SHOULD FIX
1. Fact Pattern Booby Traps: pass
2. Cross-Doctrine Clashes: pass
3. Cross-Question Spoilers: Calling the event "Darius's attempted murder" in the prompt casually spoils Q2, which tests whether Darius's conduct actually met the actus reus for attempt under different jurisdictional tests. 
Recommended fix: Change the prompt's phrasing from "Darius's attempted murder of Vance" to "Darius's actions against Vance" or "any attempt crime established by Darius's conduct" to preserve the mystery of Q2.
-->
