# Week 2 · AcademicMate design choices

![AcademicMate design showing file review, answers with sources, and reminders](week2_architecture_v1.png)

## What the design needs

The simplest version takes a question and returns an answer. That leaves no way to check a date, save a task or send a reminder later.

| Rules | What is needed | Part of the design |
|---|---|---|
| FR1–FR3, RAI1 | Read either file and check dates before saving. | File reader and student review. |
| FR4, FR5, FR8, RAI2, RAI3 | Use only the student's files. Show a source or flag a missing answer. | Private file text and answer with source. |
| FR6 | Show which confirmed task comes first. | Task calendar. |
| FR7, NFR4, RAI4 | Schedule one send and record what WhatsApp reports. | Reminder schedule and WhatsApp status. |

## Decisions and trade-offs

| Choice | Rules | Other option | Decision and cost |
|---|---|---|---|
| Get the notice | FR1, RAI3 | Connect to the student's eLearning account. | Use uploads. Setup is simpler, but the student must upload a revised notice. |
| Save a date | FR2, FR3, RAI1 | Add every date as soon as the file is read. | Ask the student to confirm the date first. It takes one extra step and catches mix-ups between a quiz opening and closing time. |
| Answer a question | FR4, FR5, FR8, RAI2 | Let the model answer from memory. | Find a passage in the student's file first, then use it to answer. This takes time and can miss a useful passage. |
| Send a reminder | FR7, NFR4, RAI4 | Send each time the task is checked. | Keep one send record per task and chosen time. This adds a record to maintain and prevents a retry from sending the same reminder twice. |

## How we will check the design

| Goal | Rules | Test and target | Part of the design | Evidence to keep |
|---|---|---|---|---|
| O1 | FR2, NFR1 | At least 85 of 100 title and date fields match. | File reader | Expected and extracted values side by side. |
| O1 | FR3, RAI1 | Zero dates confirmed early in 20 checks. | Student review | Task status before and after approval. |
| O2 | FR4, FR5, FR8, NFR2, RAI2 | At least 24/30 answers correct. All 30 cite a source, at least 27 support the reply, and at least 18/20 missing answers are flagged. | Private file text and answer with source | Answer key, replies and cited lines. |
| O2 | FR6, NFR3 | At least 16/20 task lists in order. The 27th of 30 sorted reply times is under 5 seconds. | Calendar and answer with source | Expected order, actual order and reply times. |
| O3 | FR7, NFR4, RAI4 | At least 19/20 valid sends accepted on time. Zero duplicate or unapproved sends in 20 further cases. | Reminder schedule and WhatsApp status | Task, chosen minute, send record and service reply for each test. |

**Biggest trade-off.** Student review adds a click. FR3 calls for that check. If the app reads “opens Friday” as “due Friday,” the student can catch it before a reminder goes out.
