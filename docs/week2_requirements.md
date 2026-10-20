# Requirements Specification — UTM AcademicMate

**Project Title:** UTM AcademicMate — AI Academic Planning Assistant for UTM Students  
**Version:** 1.0

## Section 0 — Project Framing and Application Scope

### 0.1 Problem Statement

University students often need to manage multiple courses, assignments, quizzes, examinations, and submission deadlines. Academic information may be distributed across course outlines, assignment instructions, PDF documents, and screenshots from learning platforms. Manually identifying, organising, and tracking this information can require additional effort and may lead to missed deadlines or poor task prioritisation.

UTM AcademicMate aims to help UTM undergraduate students organise their academic responsibilities through an AI-powered academic planning assistant. Students can upload academic PDFs and screenshots, review extracted tasks and deadlines, ask questions about their uploaded materials, prioritise their tasks, and receive deadline reminders through WhatsApp.

### 0.2 Problem Evidence

**Evidence 1: Academic Procrastination**

Salguero-Pazos and Reyes-de-Cózar (2023) conducted a systematic review of academic procrastination research. This work provides background evidence that academic procrastination is an established issue in educational settings.

Source: https://doi.org/10.1016/j.ijer.2023.102228

**Evidence 2: Time Management and Learning Outcomes**

Liu, Ma, and Jia (2026) examined the relationship between time management and college learning outcomes through a systematic review and meta-analysis. This research provides relevant background for investigating how students manage their academic responsibilities.

Source: https://doi.org/10.3389/fpsyg.2026.1700298

These sources support the general relevance of academic procrastination and time management. However, they do not directly establish the extent of missed deadlines among UTM students. A student survey or interview could be conducted later to investigate this local problem more specifically.

### 0.3 Existing Approaches

**1. MyStudyLife**

MyStudyLife provides academic planning features that help students organise classes, examinations, assignments, and deadlines.

Source: https://mystudylife.com/

**2. Google Calendar and Google Tasks**

Google Calendar and Google Tasks allow users to organise scheduled activities and tasks, including deadlines and reminders.

Source: https://support.google.com/calendar/answer/9901136?hl=en

**3. Todoist**

Todoist provides task management features that students can use to organise coursework, track assignments, and manage deadlines.

Source: https://www.todoist.com/inspiration/todoist-guide-for-students/

These approaches already support academic scheduling and task management. Therefore, UTM AcademicMate should not claim that it is the first system to provide these capabilities.

### 0.4 Project and Engineering Gap

Existing planning and task management tools provide useful ways to organise academic responsibilities. However, UTM AcademicMate will focus on integrating information extraction from student-uploaded PDFs and screenshots with document-grounded question answering, academic task prioritisation, and WhatsApp deadline reminders in a single workflow.

The engineering challenge is to extract academic information accurately, provide answers supported by uploaded materials, and turn extracted information into useful and reliable reminders. The system must also allow students to verify extracted deadlines before they are used for planning. This is a practical engineering gap for the proposed project, rather than a claim of scientific novelty.

### 0.5 Project Objectives

**O1:** To develop a module that extracts academic tasks and deadlines from student-uploaded PDFs and screenshots, with student verification before the information is used for planning.

**O2:** To implement a retrieval-augmented generation (RAG) assistant that answers questions using uploaded academic materials and supports task prioritisation based on recorded deadlines and task information.

**O3:** To develop and evaluate a deadline reminder function that sends WhatsApp notifications and measures task extraction accuracy, answer quality, and reminder reliability.

### 0.6 Intended Users

The intended users are UTM undergraduate students who need assistance managing academic information and deadlines across multiple courses.

The initial system is designed for individual students who upload their own academic materials.

### 0.7 Supported Tasks

UTM AcademicMate will support the following tasks:

1. Accept academic PDF documents and screenshots uploaded by students.
2. Extract relevant academic information, including task descriptions, deadlines, and examination dates when available.
3. Allow students to review and correct extracted information before saving it.
4. Answer questions using information retrieved from uploaded academic materials.
5. Display recorded academic tasks and their deadlines.
6. Help students prioritise tasks using factors such as deadlines and task urgency.
7. Send WhatsApp reminders for confirmed deadlines.
8. Provide source references for document-grounded answers where supporting information is available.

### 0.8 Information and Knowledge Domain

The system will focus on student-provided academic information, including:

- Course outlines and course information documents.
- Assignment instructions and assessment briefs.
- Examination schedules and academic calendars.
- Lecture notes and other relevant academic PDFs.
- Screenshots containing academic tasks, announcements, or deadlines.

The assistant will use these materials as its main knowledge sources. It should not assume that information in an uploaded document is complete or up to date unless this has been verified.

### 0.9 Operating Context

Students will interact with the application through a user interface where they can upload academic documents, ask questions, review extracted tasks, and manage reminders.

The system will process uploaded information, store confirmed tasks and deadlines, retrieve relevant document content when answering questions, and generate reminders for scheduled tasks.

WhatsApp notifications will depend on the availability and configuration of an appropriate messaging integration. If WhatsApp integration cannot be completed within the project constraints, a simpler notification method may be used as a fallback.

### 0.10 Important Constraints

- The initial system will accept PDFs and screenshots only.
- Students must upload their own academic materials.
- The initial system will not automatically log in to UTM eLearning or monitor course dashboards.
- Extracted dates and tasks must be reviewed by students before being treated as confirmed information.
- The quality of answers depends on the relevance, accuracy, and completeness of uploaded materials.
- WhatsApp notifications require an available and properly configured messaging service.
- The project has limited development time and computational resources.
- Private student information and credentials must be protected.
- Evaluation will use a prepared test dataset containing academic documents, questions, and verified task information.

### 0.11 Explicit Out-of-Scope Tasks

UTM AcademicMate will not:

1. Automatically log in to student accounts or monitor UTM eLearning.
2. Submit assignments, complete quizzes, or perform academic work on behalf of students.
3. Guarantee that extracted information is correct without verification.
4. Make official academic decisions, such as determining graduation eligibility or approving course registration.
5. Replace lecturers, academic advisors, or official university announcements.
6. Provide answers as confirmed facts when the uploaded materials do not contain sufficient supporting information.
7. Guarantee WhatsApp message delivery when the messaging service or network is unavailable.

### 0.12 Evaluation Focus

The evaluation will determine whether UTM AcademicMate can:

- Extract academic tasks and deadlines accurately from PDFs and screenshots.
- Produce answers that are correct and supported by uploaded academic materials.
- Provide useful task prioritisation based on recorded academic information.
- Generate reminders for the correct tasks and deadlines.
- Meet acceptable response-time and notification-reliability targets.
- Protect student information and communicate uncertainty when the available evidence is insufficient.

The evaluation will use predefined test cases, verified reference answers, manually checked task information, and recorded notification results.

---

## Section 1 — Functional Requirements (FR)

| ID | Requirement — The system SHALL | Scope Boundary — SHALL NOT |
|---|---|---|
| FR1 | Allow students to upload academic PDF documents and screenshots for processing. | Accept unsupported file formats in the initial version. |
| FR2 | Extract identifiable academic tasks, relevant dates, and associated information from uploaded documents and screenshots. | Treat uncertain or missing dates as confirmed information. |
| FR3 | Display extracted tasks and deadlines for students to review and correct before saving them as confirmed tasks. | Save extracted deadlines as confirmed without student verification. |
| FR4 | Answer academic questions using relevant information retrieved from the student's uploaded materials. | Present unsupported information as if it came from the uploaded documents. |
| FR5 | Provide source references or document locations that allow students to check the supporting information for document-grounded answers. | Invent source references or claim that a document supports an answer when it does not. |
| FR6 | Organise confirmed tasks and suggest their priority using recorded deadlines and task information. | Make official academic decisions or guarantee that a suggested priority is suitable for every student. |
| FR7 | Schedule and send WhatsApp reminders for confirmed academic deadlines when the messaging integration is available. | Send reminders based on unconfirmed deadlines or claim that a message was delivered without delivery evidence. |
| FR8 | Indicate when uploaded materials do not contain sufficient information to answer a question reliably. | Fabricate course information, assessment instructions, or deadlines to fill missing information. |

---

## Section 2 — Non-Functional Requirements (NFR)

The following thresholds are initial engineering targets for the project. They will be reviewed after preliminary testing and may be adjusted if justified by the available resources and evaluation results.

| ID | Quality Attribute | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| NFR1 | Extraction Correctness | The system shall correctly extract academic task descriptions and deadlines from supported documents. | Compare extracted task and date fields against manually verified reference data from at least 50 task instances. | Exact-match accuracy for task and deadline fields. | ≥ 85% |
| NFR2 | Answer Correctness | The system shall provide answers that are factually consistent with the uploaded academic materials. | Evaluate at least 30 predefined academic questions against verified reference answers using a consistent scoring rubric. | Correct answer rate. | ≥ 80% |
| NFR3 | Performance | The system shall return answers to supported questions within an acceptable response time under the defined test conditions. | Measure end-to-end response time for at least 30 test queries, excluding initial document-upload and indexing time. | 90th-percentile response latency (p90). | < 5 seconds |
| NFR4 | Notification Reliability | The system shall correctly process scheduled reminders for confirmed academic deadlines. | Run at least 20 reminder test cases and inspect scheduling records and messaging-provider results. | Percentage of reminders successfully processed and accepted by the messaging provider. | ≥ 95% |

**Measurement notes:**

- Extraction accuracy will be calculated using the number of correctly extracted fields divided by the total number of reference fields evaluated.
- Answer correctness will be judged against a predefined answer key, not simply whether the response sounds reasonable.
- Response latency will be measured under documented test conditions using the same test environment.
- Notification acceptance by a messaging provider does not necessarily prove that the message reached the student's device. Delivery status will be recorded separately when available.

---

## Section 3 — Responsible AI Requirements (RAI)

| ID | Responsible AI Risk | Requirement | Measurement Method | Metric | Threshold |
|---|---|---|---|---|---|
| RAI1 | Accuracy and Uncertainty | The system shall require student verification before extracted tasks and deadlines are treated as confirmed planning information. | Test at least 20 extraction cases containing clear, ambiguous, and missing dates. Inspect the review process and saved task status. | Percentage of tested extracted deadlines that remain unconfirmed until student approval. | 100% |
| RAI2 | Transparency and Grounding | The system shall provide verifiable source references for document-grounded answers and indicate when sufficient supporting evidence cannot be found. | Evaluate at least 30 document-grounded questions by checking citation presence and whether the cited material supports the answer. | Citation presence rate and citation-source match rate. | 100% citation presence for document-grounded answers; ≥ 90% citation-source match rate. |
| RAI3 | Privacy and Security | The system shall prevent unauthorised disclosure of student information and shall not expose private academic materials or credentials through responses, logs, or public repositories. | Inspect application logs, repository contents, access controls, and at least 20 privacy-related test cases. | Number of detected unauthorised disclosures or exposed secrets. | 0 detected incidents in the test set. |
| RAI4 | Notification Integrity | The system shall generate reminders only for confirmed tasks and shall avoid sending duplicate reminders for the same scheduled event unless explicitly configured. | Test at least 20 reminder scenarios, including unconfirmed tasks and repeated scheduling events. | Incorrect reminders sent and unintended duplicate reminders. | 0 incorrect reminders from unconfirmed tasks and 0 unintended duplicates in the test set. |

### Part A Summary

The requirements define what UTM AcademicMate must do, the expected level of performance, and the controls needed to manage its main risks.

The functional requirements focus on document processing, task management, RAG-based question answering, and reminders. The non-functional requirements establish measurable performance targets, while the Responsible AI requirements address uncertainty, source grounding, privacy, and notification integrity.

These requirements will guide the evaluation criteria and V1 architecture in the following sections of the project.