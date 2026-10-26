## 1. Architecture Decision Record (ADR)

The following architecture decisions define the main components required for the initial version (V1) of UTM AcademicMate. The decisions are based on the project requirements, evaluation criteria, and development constraints.

### ADR 1: Include a Knowledge Access Component

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| Knowledge access for academic question answering | FR4, FR5, RAI2, NFR2 — Answers must be based on uploaded academic materials and provide verifiable source references. | 1. Use a language model without document retrieval. 2. Search uploaded documents using basic keyword matching. 3. Retrieve relevant document content and use it to generate grounded answers. | Include a knowledge access component that retrieves relevant content from uploaded documents before generating answers. | Retrieval improves source grounding and traceability but adds processing complexity and may retrieve irrelevant or incomplete information. |

### ADR 2: Include an Explicit Scope and Uncertainty Control

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| Control unsupported questions and uncertain information | FR8, RAI1, RAI2 — The system must identify insufficient evidence and prevent uncertain extracted deadlines from being treated as confirmed. | 1. Allow the language model to answer every question. 2. Use instructions alone to control responses. 3. Add explicit checks for evidence sufficiency and require student verification of extracted tasks and deadlines. | Include scope and uncertainty controls, together with a student review step before extracted tasks and deadlines are confirmed. | Additional checks improve reliability and user control but may increase response time or cause the system to decline some answerable questions. |

### ADR 3: Use Student-Verified Tasks for Planning and Reminders

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| Manage extracted academic tasks and deadline reminders | FR2, FR3, FR6, FR7, RAI1, RAI4 — Planning and reminders must use confirmed task information and avoid incorrect or duplicate notifications. | 1. Generate reminders directly from extracted dates. 2. Require students to manually create every task. 3. Extract tasks automatically, allow student correction, and use confirmed tasks for planning and reminders. | Use an academic task store containing student-verified tasks and deadlines, with reminder scheduling based only on confirmed records. | Student verification reduces the risk of incorrect reminders but requires additional user effort. Reminder delivery also depends on the availability of the messaging service. |

### ADR 4: Use Student-Uploaded Documents Instead of Automatic eLearning Access

| Decision | Requirement / Constraint | Alternatives Considered | Selected Option | Trade-off Accepted |
|---|---|---|---|---|
| Obtain academic information | Project scope and constraints — The initial version must remain feasible within the available development time and must not require access to private student accounts. | 1. Automatically log in to UTM eLearning and monitor course dashboards. 2. Require students to enter all academic information manually. 3. Allow students to upload PDFs and screenshots for automatic information extraction. | Use student-uploaded PDFs and screenshots as the primary input sources. | This approach reduces integration and account-access complexity but depends on students uploading the latest and relevant materials themselves. |

---

## 2. Initial Requirements Traceability Matrix

The matrix below connects each project objective to its requirements, evaluation criteria, architecture elements, and the evidence that will be collected during later testing.

| Objective ID | Requirement Type | Evaluation Criterion | Architecture Element | Later Evidence |
|---|---|---|---|---|
| O1 | FR1, FR2, NFR1 | Academic task and deadline extraction accuracy ≥ 85%. | Document Input and Extraction Component; Student Review Interface; Academic Task Store. | Compare extracted task descriptions and deadlines against manually verified reference data from at least 50 task instances. |
| O1 | FR3, RAI1 | 100% of tested extracted deadlines require student approval before confirmation. | Student Review Interface; Task Verification Control; Academic Task Store. | Test at least 20 extraction scenarios, including ambiguous and missing dates, and inspect task confirmation status. |
| O2 | FR4, NFR2 | Document-grounded answer correctness ≥ 80%. | Knowledge Access Component; Language Model Service; Response Generation Component. | Evaluate at least 30 academic questions against predefined reference answers. |
| O2 | FR5, RAI2 | 100% citation presence for document-grounded answers and ≥ 90% citation-source match rate. | Document Retrieval Component; Source Reference Tracking; Response Generation Component. | Inspect at least 30 responses to verify citation presence and whether cited content supports each answer. |
| O2 | FR6 | Task prioritisation agrees with predefined reference rules in ≥ 80% of test scenarios. | Academic Task Store; Task Prioritisation Component; Planning Interface. | Evaluate at least 20 scenarios containing tasks with different deadlines and urgency levels. |
| O3 | FR7, NFR4, RAI4 | ≥ 95% of valid reminder requests are successfully processed and accepted by the messaging provider, with no incorrect reminders from unconfirmed tasks in the test set. | Reminder Scheduler; Confirmed Academic Task Store; WhatsApp Messaging Integration. | Run at least 20 reminder test cases and inspect scheduling records, provider status, and duplicate-reminder results. |
| O3 | NFR3 | 90th-percentile response latency is below 5 seconds. | Application Interface; Knowledge Access Component; Language Model Service. | Measure end-to-end response latency across at least 30 supported queries under documented test conditions. |
| O2 | FR8, RAI2 | Appropriate uncertainty response rate ≥ 90% for questions that cannot be answered from the available documents. | Evidence Sufficiency Check; Scope and Uncertainty Control; Response Generation Component. | Test at least 20 questions with missing or insufficient supporting information and record whether the system communicates the limitation appropriately. |

