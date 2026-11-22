# Week 2 · AcademicMate requirements

Version 1.0

## 0. Project and scope

**Problem.** A student can copy the wrong date into a planner. For example, one UTM assignment starts in week 5 but is due in week 6. A review also found a link between time management and learning outcomes. We do not yet know how often UTM students miss deadlines. [UTM schedule](https://people.utm.my/mnazri/semm-1921-intro-to-mechanical-engineering/) · [College study](https://doi.org/10.3389/fpsyg.2026.1700298)

**Existing tools.** MyStudyLife plans classes and homework. Google Calendar puts tasks on dates. Todoist tracks deadlines. A student looking at a saved date may still ask, “Which line in the notice gives that date?” AcademicMate will show that line beside the date it saves. [MyStudyLife](https://mystudylife.com/) · [Google Calendar](https://support.google.com/calendar/answer/9901136?hl=en) · [Todoist](https://www.todoist.com/help/todoist/features/introduction-to-deadlines-in-todoist-uMqbSLM6U)

### Goals

- **O1** Read the task and dates from an upload. Save clear dates automatically and ask about missing or conflicting ones.
- **O2** Answer questions about the student’s assignment with a source. Show upcoming tasks in date order.
- **O3** When a student turns on WhatsApp reminders, send one alert per task at the student’s chosen time.

| Scope | Decision |
|---|---|
| Users and setting | A UTM student signs in once on their device. The app remembers the session across visits and new chats. Their uploads, answers and tasks are private to that account. |
| Inputs | One assignment PDF or one quiz screenshot. The app reads titles, dates, times and instructions that are visible. [Public examples](week1_project_scope.md#data-sources-and-scope) |
| Tasks | Ask about an assignment, check its source, look up a separate public question or receive an automatic deadline reminder. |
| Limits | Files and model processing need university-approved storage and access. A date that is missing, unclear or disputed needs review. WhatsApp reminders require opt-in. |
| Outside the project | The student downloads and submits work in eLearning. The assistant will not sign in to eLearning on their behalf, complete assessed work or make decisions about grades. |
| Main test | Can a student get an answer from their own file and one timely reminder, while another account cannot see that file? |

## 1. Functional requirements

| ID | Required behaviour |
|---|---|
| FR1 | Reuse the active university session for chats and uploads. Ask for sign-in again after sign-out or when the session expires. Accept an assignment PDF or quiz screenshot. Explain unsupported file types. |
| FR2 | The system shall read the task title, instructions and stated dates. It shall keep opening time, closing time and attempt length separate. |
| FR3 | Show the source beside each date. Save an explicit, unambiguous future deadline automatically. Hold incomplete or conflicting dates for review. Let the student correct a saved date. |
| FR4 | Answer assignment-specific questions from the signed-in student’s uploads. For a separate background question, the assistant may read an approved public page and cite it. |
| FR5 | For a course answer, show its file and the PDF page or screenshot text. For public background, link to the page used. |
| FR6 | Put the next ready task first. Use the due date for an assignment, the start for a scheduled quiz or the close for a quiz window. Ties can appear in either order. |
| FR7 | When the student opts in, schedule and send one WhatsApp reminder per ready task at their chosen time. Show its status. A student can change or cancel it. |
| FR8 | Say when a course file lacks the answer. Web results cannot supply a missing course deadline or change the lecturer’s instructions. Decline requests to solve or submit assessed work. |

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
| RAI1 | A wrong date triggers an alert. Use only a clear future date supported by the file. Hold ambiguous, missing, conflicting or past dates. | Try 20 dates covering clear and held cases. Compare the calendar with the expected decision for each. | All 20 routed correctly. Zero held cases scheduled. |
| RAI2 | An answer invents instructions. Cite the upload for course rules and label public background with its link. | Check sources for 30 course questions. Ask 20 more with no answer in the file. | Sources on 30/30 answers, at least 27/30 support the answer, and at least 18/20 missing answers flagged. |
| RAI3 | Check the saved session and the file owner in the background before every read. Use approved storage and model processing. Keep files, private prompts and credentials out of public lookup, logs and third-party alerts. | Try two test accounts and a signed-out session. Inspect 20 access and disclosure checks, including web requests and alerts. | Zero unauthorised reads or disclosures. |
| RAI4 | Send one generic alert per opted-in task and reminder time. Check the latest task state before sending. | Try 20 cases including retries, opt-outs, corrected dates and tasks in review. | Zero duplicate, stale or unapproved sends. |

**Hardest rule to check.** RAI2. A reply can name the correct page and still mix up “opens” and “closes.” Someone must read the cited line and compare it with the answer.
