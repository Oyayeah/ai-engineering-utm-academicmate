# Week 2 · AcademicMate requirements

Version 1.0

## 0. Project and scope

**Problem.** A student can copy the wrong date into a planner. For example, one UTM assignment starts in week 5 but is due in week 6. A review also found a link between time management and learning outcomes. We do not yet know how often UTM students miss deadlines. [UTM schedule](https://people.utm.my/mnazri/semm-1921-intro-to-mechanical-engineering/) · [College study](https://doi.org/10.3389/fpsyg.2026.1700298)

**Existing tools.** MyStudyLife plans classes and homework. Google Calendar puts tasks on dates. Todoist tracks deadlines. A student looking at a saved date may still ask, “Which line in the notice gives that date?” AcademicMate will show that line before the student saves the date. [MyStudyLife](https://mystudylife.com/) · [Google Calendar](https://support.google.com/calendar/answer/9901136?hl=en) · [Todoist](https://www.todoist.com/help/todoist/features/introduction-to-deadlines-in-todoist-uMqbSLM6U)

### Goals

- **O1** Read the task and dates from an upload. Let the student check and correct them.
- **O2** Answer questions using the uploaded instructions and list confirmed tasks in order of deadline.
- **O3** Send WhatsApp reminders for confirmed tasks. Check that each reminder is sent once to the right student.

| Scope | Decision |
|---|---|
| Users and setting | A UTM undergraduate uses the app in a browser to plan work across courses. |
| Inputs | One assignment PDF or one quiz screenshot. The app reads titles, dates, times and instructions that are visible. [Public examples](week1_project_scope.md#data-sources-and-scope) |
| Tasks | Check a date, ask what to submit, see what is due next and set a WhatsApp reminder. |
| Limits | Students upload their own files. A blurry notice may need a correction. WhatsApp needs a working service and the student's chosen number. |
| Outside the project | Signing in to eLearning, doing coursework, answering quiz questions or making official decisions about grades and registration. |
| Main test | Can a student check the right date, find a supported answer and get one reminder for the right task? |

## 1. Functional requirements

| ID | Required behaviour |
|---|---|
| FR1 | The system shall accept an assignment PDF or a quiz screenshot and tell the student if a file type is unsupported. |
| FR2 | The system shall read the task title, instructions and stated dates. It shall keep opening time, closing time and attempt length separate. |
| FR3 | The system shall show each proposed date beside its source. The student can correct and confirm it. Missing or conflicting dates stay open for review. |
| FR4 | The system shall answer questions about assessment instructions using only that student's uploads. |
| FR5 | The system shall show the file and PDF page or screenshot text that supports each answer. |
| FR6 | The system shall put the next confirmed task first. Use the due date for an assignment, the start for a scheduled quiz or the closing time for a quiz window. Ties can appear in either order. |
| FR7 | The system shall send one WhatsApp reminder to the student at their chosen time for a confirmed task and show its send status. |
| FR8 | The system shall say when an upload lacks the answer. It shall decline requests to solve or submit coursework. |

## 2. Non-functional requirements

These are targets for later tests. No results have been recorded.

| ID | Quality and requirement | How to measure it | Metric and target |
|---|---|---|---|
| NFR1 | Read task titles and dates correctly. | Hand-label 50 tasks across both formats. Check each title and its due or quiz date, including the time if shown. Accept equivalent date formats. | At least 85% of the 100 fields match. |
| NFR2 | Give correct answers to questions about the uploads. | Compare 30 answerable questions with a hand-checked answer key. Count an answer as correct when it gives all required facts without adding a wrong one. | At least 24 of 30 answers correct (80%). |
| NFR3 | Show answers promptly. | Time those 30 questions on the same setup, from asking to seeing the full reply. Start after the upload is ready. | The 27th fastest reply takes under 5 seconds (90th percentile). |
| NFR4 | Send reminders reliably. | Schedule 20 valid reminders. Check the student, task and scheduled minute against the WhatsApp service record. | At least 19 of 20 accepted on time (95%). |

## 3. Responsible AI requirements

| ID | Risk and rule | How to check | Target |
|---|---|---|---|
| RAI1 | A wrong date enters the calendar. Keep all dates in review until the student confirms them. | Try 20 clear, missing or conflicting dates. Inspect the saved tasks before approval. | 0 dates confirmed without approval. |
| RAI2 | An answer invents instructions. Cite the upload or say the detail is missing. | Check sources for 30 answerable questions. Ask 20 more with no answer in the file. | Sources on 30/30 answers, at least 27/30 support the answer, and at least 18/20 missing answers flagged. |
| RAI3 | One student sees another's data. Limit file and task access to the owner. Keep private text, phone numbers and keys out of logs and public files. | Use two test accounts and made-up details in 20 checks. Inspect replies, logs and repo files. | 0 leaks found. |
| RAI4 | A repeated send gives two reminders. Allow one send per confirmed task and chosen reminder time. | Try 20 cases including retries and dates still in review. Count duplicate or unapproved sends. | 0 duplicate sends and 0 unapproved sends. |

**Hardest rule to check.** RAI2. A reply can name the correct page and still mix up “opens” and “closes.” Someone must read the cited line and compare it with the answer.
