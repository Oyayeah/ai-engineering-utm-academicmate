# Week 1 Project Scope

## Project Name
**UTM AcademicMate — AI Academic Planning Assistant for UTM Students**

## Domain
Artificial Intelligence in Education, document information extraction, Retrieval-Augmented Generation (RAG), and academic planning.

## Problem Statement
University students need to manage assignments, quizzes, examinations, and other academic activities across multiple courses. Important dates and instructions may be distributed across course outlines, PDF documents, and screenshots from learning management systems. Manually identifying and organising this information can require additional effort and may cause students to overlook important deadlines.

## Evidence of the Problem

### Evidence 1 — Academic Procrastination
A 2023 systematic review by Salguero-Pazos and Reyes-de-Cózar examined 32 interventions aimed at reducing academic procrastination. It identified self-regulation as a central aspect of educational interventions and highlighted the need to improve approaches to supporting students.

**Source:** Salguero-Pazos, R., & Reyes-de-Cózar, S. (2023). *Interventions to reduce academic procrastination: A systematic review.*  
https://doi.org/10.1016/j.ijer.2023.102228

### Evidence 2 — Time Management and Learning Outcomes
A 2026 systematic review and meta-analysis by Liu, Ma, and Jia examined 31 studies involving 13,506 participants. The findings indicated a moderate positive relationship between time management and college students' learning outcomes. This supports investigating tools that help students organise their academic workload, but does not prove that this specific system will improve academic performance.

**Source:** Liu, Ma, & Jia (2026). *Systematic review and meta-analysis of the impact of time management on college students’ learning outcomes.*  
https://doi.org/10.3389/fpsyg.2026.1700298

**Evidence limitation:** These sources support the broader importance of time management and academic planning. They do not establish how frequently UTM students miss deadlines or whether UTM students specifically need this system. Student feedback or a small survey should be collected to strengthen the local problem evidence.

## Initial Related Work / Existing Approaches

### 1. MyStudyLife — Student Planner
**Source:** https://mystudylife.com/

**Existing capabilities:** Academic schedules, assignments, exam planning, reminders, and AI-assisted study features. Its current feature descriptions also include extracting timetable information from screenshots and PDFs.

**Key limitation / comparison:** The proposed project will investigate a UTM-focused workflow combining document-grounded course question answering with WhatsApp deadline reminders. The exact feature differences should be verified against the current MyStudyLife product before making a definitive comparison.

### 2. Google Calendar — Calendar and Task Management
**Source:** https://support.google.com/calendar/answer/9901136?hl=en-7

**Existing capabilities:** Users can create tasks, set deadlines, view dated tasks on a calendar, and receive notifications.

**Key limitation / comparison:** Students generally need to enter or import task information. UTM AcademicMate aims to extract activities from uploaded academic documents and answer questions grounded in those documents.

### 3. Todoist — Task and Deadline Management
**Source:** https://www.todoist.com/inspiration/todoist-guide-for-students

**Existing capabilities:** Organising tasks by course, managing deadlines, integrating with calendars, and configuring reminders.

**Key limitation / comparison:** Task-management features alone do not establish the accuracy of extracting course-specific dates or answering questions from uploaded UTM course materials. These capabilities will be evaluated in the proposed prototype.

## Engineering Gap / Limitation
Existing student planners already provide calendars, reminders, and some AI-assisted planning features. Therefore, this project will not claim to be the first AI academic planner.

The proposed engineering gap is to design and evaluate a UTM-focused prototype that combines information extraction from student-uploaded PDFs and screenshots, RAG-based answers grounded in course materials, workload prioritisation, and WhatsApp deadline reminders in one workflow.

Key engineering challenges include:
- Extracting accurate dates from different document layouts and screenshot quality.
- Distinguishing confirmed deadlines from dates that are unclear or missing.
- Retrieving relevant course information and reducing unsupported AI answers.
- Scheduling reminders reliably without duplicates.
- Protecting private student documents and contact details.

## Initial Project Objectives

- **O1:** To develop a document-processing module that extracts academic activities and their deadlines from student-uploaded PDFs and screenshots, with student verification of extracted information.
- **O2:** To implement a RAG-based assistant that answers course-related questions and supports academic task prioritisation using information from uploaded materials and saved deadlines.
- **O3:** To implement and evaluate a deadline reminder mechanism through WhatsApp, measuring reminder delivery reliability and the accuracy of extracted academic information.

## Target Users
The primary target users are undergraduate students at Universiti Teknologi Malaysia (UTM) who manage multiple courses and need assistance organising academic tasks and deadlines.

The initial prototype will focus on individual students who upload their own course materials. It will not require direct access to their UTM accounts or automatically monitor UTM eLearning.

## Data Sources (At Least 2 Publicly Accessible Documents)

1. **UTM Academic Calendar** — https://amd.utm.my/academic-calendar/
   - Intended use: semester dates and official academic schedule context.
2. **UTM Faculty of Computing — Undergraduate Resources** — https://comp.utm.my/undergraduate/
   - Intended use: publicly available programme handbooks, academic regulations, registration information, and other undergraduate resources.
3. **UTM Faculty of Science — Academic Handbook** — https://science.utm.my/undergraduate/academic-handbook/
   - Intended use: example of publicly available faculty academic handbook information.

**Before final submission:** Select the exact PDF documents to use, record their titles and publication/session years, verify that the links work, and confirm that the materials are relevant to the prototype.

**Additional runtime inputs:** Students may upload their own course outlines, assignment instructions, lecture PDFs, and screenshots. These are user-provided inputs, not public data sources. Use synthetic or authorised sample materials for demonstrations. Do not publish private student documents or restricted materials in a public repository.

## Similar to EduAdvisor
Both UTM AcademicMate and EduAdvisor use RAG to retrieve relevant information from documents and generate answers grounded in those sources. Both aim to reduce the effort required to search academic information and should be evaluated for factual accuracy and hallucination risks.

## Different from EduAdvisor
The EduAdvisor example in the lab focuses on academic advising questions about courses, prerequisites, and graduation requirements using official university documents.

UTM AcademicMate focuses on day-to-day course management. It extracts dates from uploaded PDFs and screenshots, maintains an academic task calendar, helps prioritise work, answers questions about uploaded course materials, and sends reminders through WhatsApp.

## Responsible AI Risks

### Risk 1 — Incorrect Date Extraction
**Potential impact:** A student may receive a reminder for the wrong date or miss a real deadline.  
**Proposed control:** Show the source text or screenshot region, request confirmation of uncertain dates, and allow manual correction.

### Risk 2 — RAG Hallucination
**Potential impact:** The assistant may invent course instructions or provide an answer unsupported by uploaded materials.  
**Proposed control:** Retrieve relevant passages, show source references, and state when the available documents do not provide enough evidence to answer.

### Risk 3 — Privacy and Security
**Potential impact:** Uploaded course files or WhatsApp contact details may be exposed.  
**Proposed control:** Restrict access, minimise stored personal data, protect credentials, and avoid committing private documents to a public repository.

### Risk 4 — Notification Failure
**Potential impact:** A reminder may be delayed, duplicated, or not delivered.  
**Proposed control:** Track notification status, prevent duplicate sends, and provide an in-app deadline list as a fallback.

## Initial Scope and Assumptions
- The prototype will accept student-uploaded PDFs and screenshots.
- Students will review and confirm extracted deadlines before they are used for reminders.
- RAG responses will be grounded in the student's uploaded course materials.
- WhatsApp reminders will depend on access to an approved messaging API and its setup requirements.
- Direct automated access to UTM eLearning is outside the initial scope.
- Public repository contents will exclude API keys, credentials, private student data, and documents that cannot be redistributed.

## Initial Evaluation Plan
- **Deadline extraction:** Compare extracted activities and dates with manually verified ground truth.
- **RAG question answering:** Test questions with known answers and check answer correctness and source relevance.
- **Task prioritisation:** Check whether suggested priorities follow defined deadline and workload rules.
- **WhatsApp reminders:** Measure successful delivery, duplicate notifications, and missed scheduled reminders.

## Initial Related Public Resources
- UTM Academic Calendar: https://amd.utm.my/academic-calendar/
- UTM Faculty of Computing undergraduate resources: https://comp.utm.my/undergraduate/
- UTM Faculty of Science academic handbook: https://science.utm.my/undergraduate/academic-handbook/
- MyStudyLife: https://mystudylife.com/
- Google Calendar Tasks documentation: https://support.google.com/calendar/answer/9901136?hl=en-7
- Todoist student guide: https://www.todoist.com/inspiration/todoist-guide-for-students/

---
UTM AcademicMate proposes an AI-powered academic planning assistant that allows UTM students to upload course-related PDFs and screenshots. The system will extract important academic activities, organise them into a central schedule, send reminders through WhatsApp, and use Retrieval-Augmented Generation (RAG) to answer questions based on the uploaded course materials. It will also help students prioritise upcoming tasks and prepare study plans.