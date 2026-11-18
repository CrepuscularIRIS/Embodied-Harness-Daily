# selection-016 — three selections, zero ready posters

Run: embodied-rolling-20261023-01. Authority: problem-core-v1.1 / SELECTION.md / PROBLEM_CORE.md. Editorial workflow follows OPUS_REEL_PROMPT.md with the user's explicit single-seat Sol role replacement. Actual executor: **gpt-6.1-sol, sonnet slot**, not Opus5.5. Environment execution date: **2026-11-17**; the user-specified2026-11-19 role-change date is an instruction label, not an asserted current date.

**Outcome: selected3; ready0; failed after one redo3; substantive L2 corrections0.** Existing ready total remains **51 =18initial+33rolling**. No failed draft is added to the ready table or featured wall. No third repair, substitute production cycle, L2 rewrite, shared progress.md edit, git operation, nested agent, headless Claude/model service, paper code execution, author contact, or hosted publication.

## Candidate state and nonnumeric selection

Titles below come from research/corpus.jsonl. Latest assessments: `batches/inc-l2-15.jsonl`, not older L1 or withdrawn runs. All six are P3 / confirmed / to_l3. Capability and judgment have equal editorial priority; the following is a mechanism/coverage choice, not a numerical score or scientific quality ranking.

| Paper and corpus title | Q3 / families | L2 cards | Decision |
|---|---|---|---|
|2611.17566 — Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety|capability / F2,F4|external_verification_control; observe_act_interface|Select: refusal versus executable object-pair risk field. Draft failed QA.|
|2611.18298 — Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation|capability / F3,F1|code_policy_trial_revision; planner_composes_code_and_policies|Select: editable contact-MPC objective programs, explicit retry and conditional-transfer accounting. Draft failed QA.|
|2611.18562 — Training Reasoning Models in Simulation to Natively Use Real Robots|capability / F3,F1|harness_native_rl; observe_act_interface|Select: RL-trained native pose interface and limited cross-embodiment transfer, full-benchmark failure ledger. Draft failed QA.|
|2611.18123 — Evaluating Language Models as Spatial Priors for Object-Goal Navigation|judgment / F2,F1|observe_act_interface; harness_effect_evaluation|First reserve: strong B-class diagnostic, not excluded for offline evaluation. Sixteen-by-sixteen area-search proxy is not navigation success. Current three slots span grounded risk, physical objective interface and nativeRL; no inference that judgment is lower priority.|
|2611.17394 — Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training|capability / F2,F4|learner_state_teacher_correction; code_policy_trial_revision|Reserve / same-card coverage pressure: learner-failure correction and independent student deployment already represented by TILDE and recent teacher-to-student work. Local coding repair is distinct, but not enough to displace the three chosen mechanism slots this issue.|
|2611.18176 — ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents|capability / F1,F2|learner_state_teacher_correction; harness_self_optimization|Reserve / same-card coverage pressure: correction/handoff plus composite self-improvement. Fixed prompt/skill across reported policy rounds means not an isolated joint-flywheel demonstration; L2 already states this, so no correction.|

The three selected papers are not strict same-problem duplicates of one another. Against the51 existing ready entries:17566 differs from2611.14115 RoboRisk/LEASH through continuous object-pair grounding and refusal-versus-reroute accounting;18298 differs from earlier goal interfaces including2602.15875/Fly0 and2409.01652/ReKep through explicit contact dynamics, simulation feedback and conditional physical deployment;18562 differs from2610.35817/ZAP through direct pose robot-use RL and new real embodiment, not a trained VLM selecting a fixed primitive library. These are differences in represented mechanism, not claims to unprecedented novelty. Nearest-prior papers were not independently re-reviewed for a novelty verdict.

No candidate was declared out of scope merely for lacking online deployment.18123 qualifies as B-class diagnostic.18562's observe–reason–pose–feedback loop qualifies as A-class despite author's “without harness” wording. Frozen-policy work without an in-loop LLM/VLM is otherwise excluded unless B-class evaluation or in-scope harness-teacher training applies.

## Source check and evidence narrowing

Local cores were read for all six; pinned arXiv HTML supplements were fetched as untrusted data. No paper instructions executed. Original text/figure caches stay local, not part of release.

| Paper | Actual supplemental reading and outcome |
|---|---|
|17566v1, first2026-11-12|Complete scientific mainI–VI, tables/captions; no appendix listed. TableII SR90.0→89.4 versusSSR51.7→81.4; TableIII correct mandatory refusals96/96 in both configurations, false refusals78/93,49/90 versus0/93,0/90. TableIV only5trials/scene. Static initial field, fixed five relations, limited AABB sampling; independent hazard-ground-truth audit remains unclear.|
|18298v1, first2026-11-13|Complete scientific mainI–VI, tables/captions; no appendix listed. TableIII initial execution8/40,14/40,20/40,26/40; TableII up-to-six-attempt cumulative39/40, not one-shot97.5%. TableIV32/40 conditional on selecting simulation-successful programs, onlyfourtasktypes. Forward-only verification and soft penalties limit recovery/safety claims.|
|18562v1, first2026-11-13|Complete main scientific text and appendicesA–H, includingtrialrecords/prompts; references not all read verbatim. Final real18/30 is on two tasktypes already trained in simulation, versus7/30LIBERO-only and0/30base. AppendixA reports~50,000H100-equivalentGPUhours. AppendixE wholeRoboDojo21/540,15successes from trainedtypes,370/540context-exhaustion; rawcount is not officialdimension-averagedscore. Qualitative7c demos not counted as quantitative transfer.|
|17394v1, first2026-11-12|Core plus§4.4/4.5/discussion and appendicesA–E. Figure5 adaptation0→81→89→95 is not benchmarkaggregate; appendixD usesstep4000 rather than fullLIBERO10000budget. Frozen-baseflowfilter usesfour50-stepchunks/32MCsamples; successfulcode alone not learnabledata.400repairattempts/task average139success versusPPO0, not an equalLLMcostcomparison. No new substantive contradiction.|
|18176v1, first2026-11-13|Core plusappendicesB–C. Main threepolicyrounds fixedprompt/skill, rollback table fromlaterimplementation,197validpairedcases versus200scheduled. HeldoutSolve45–49 chosenafterpreliminary0–4testing;4/5versus2/5tinycase study. One orderrun replacedaftertimeout witharchive retained; selectedrun cost is not allattempts. No new substantive contradiction.|
|18123v1, first2026-11-13|Core plus§§7–10 search/design/limitations/conclusion; not every§6/appendix detail read. Search uses16×16cells and normalizedsearchedarea, not interactiveObjectNav. Realpriorleave-one-room-out. Table10uniform.502 versus generated~.425–.487 andreal~.209–.347; smoothing alters fractions but does not close gap. Two model/fourroomtype, scan and serialization limits. Conditionalobserved-objectpriors not search-tested. No broad “LLMs have no spatial knowledge” claim.|

Selected papers' claim-to-section/table mapping and original-image provenance are in each SOURCE.md. Scientific statements were narrowed rather than treating structural checks as reproduction. Bibliographic first-version dates are those observed in pinned sources; no date-dependent novelty or later-work verdict was inferred.

## Corrections for controller

**None (0).** Do not send speculative single-paper revisions or alter inc-l2-15. The following are supplemental-display constraints, not reversals of L2:

-18562: full training cost and whole-benchmark/context-failure ledger are available in appendices absent from cached L2 core. Existing L2 already restricts real transfer to trained tasktypes and avoidsCoTcausalclaims.
-18123:§7 now corroborates the limited offline search proxy, not a new online navigation result.
-17394/18176: appendix training budget, local-data selection and tiny heldout-case caveats narrow editorial language; L2 already limits causal claims.
-17566: hazard-ground-truth construction audit remains a gap, not a proven metric contradiction.

## Production and actual QA

Three distinct layouts were attempted:17566 relational-risk branches plus pairedSR/SSR andfalse-refusal ledger;18298 goal-program anatomy plusfactorial/cumulative counts andconditionalhardware;18562trainingcurriculum plusreal/full-benchmark comparison. All contain at leasttwo original-paper visuals with documented provenance. No author branding or invented experimental photographs.

Initial PNGs were actually opened and failed. Each received exactlyone redo, was rerendered toPNG/PDF, and its redo PNG was actually opened. **All three still fail.** No additional repair was attempted.

| Paper | Initial issue | Sole redo and remaining failure | Status |
|---|---|---|---|
|17566|Header English crossed divider; results too tight.|Header improved, but hardware note still exceeds panel border and result content exceeds row.|FAIL/notready|
|18298|Title and cumulative warning crossed sections.|Title improved; method figure caption still intersects next divider, other notes too tight.|FAIL/notready|
|18562|Method/result overlap hid keysame-task restriction;21/540column too narrow.|Matrix replacedwithcounttable; same-task restriction nowvisible and21/540fixed, butmethodendnote stillpressesdivider.|FAIL/notready|

Print emulation:1200×1700CSSpx; PNG2400×3400; single-pagePDF900×1275.12pt. All embedded images loaded and no outer-canvas overflow, but section scroll measurements and opened images expose failures. Exact measurements in eachQA.md. Fullpaper-poster-htmlhardgates andindependentcross-modelaudit were not completed; no such pass is claimed. No full multimediaReel/viewer was requested or completed.

Task-owned failed draft directories, each containing poster.html,poster.png,poster.pdf,SOURCE.md,QA.md:

-`reel/2611.17566/`
-`reel/2611.18298/`
-`reel/2611.18562/`

Editable HTML remains local subject to existing ignore rules. The controller must not release/index these drafts asready. Further repair needs explicitauthorization. README andReelheadercounts remain51; this issue is logged only inselectionhistory, notreadytable. Prior failed2611.15651 untouched. Sharedprogress.md andoriginalL2records untouched.
