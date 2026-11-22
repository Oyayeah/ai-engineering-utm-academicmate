# Week 2 · AcademicMate test plan

These are planned tests. Use the same files and answer key for each run. Use made-up contact details and a test recipient for WhatsApp.

| Goal / rule | What to test | Lab category | Method | Measure and pass mark | Why it matters |
|---|---|---|---|---|---|
| O1 / FR2 / NFR1 | Task title and date | Domain-specific capability | Compare 50 tasks from PDFs and screenshots with 100 hand-checked fields. | At least 85 of 100 fields match. | Less retyping and fewer wrong dates. |
| O1 / FR3 / RAI1 | Automatic date or review | Instruction-following capability | Try 20 clear, unclear, conflicting, missing or past dates. Check each result against the expected action. | 20/20 routed correctly and zero held cases scheduled. | Clear deadlines need no extra click. Uncertain dates cannot start a reminder. |
| O2 / FR4 / NFR2 | Answer accuracy | Generation capability | Compare 30 answers with the answer key. All required facts must match. | At least 24 of 30 correct. | Students know what to hand in. |
| O2 / FR5, FR8 / RAI2 | Sources and missing details | Instruction-following capability | Read the sources for those 30 answers. Ask 20 more questions the files cannot answer. | 30/30 cite a source, at least 27/30 cite supporting text, and at least 18/20 missing answers are flagged. | Students can check the lecturer's words. |
| O2 / FR6 | Task order | Domain-specific capability | Make 20 lists with known deadlines, including ties. Check the whole order in each list. | At least 16 of 20 lists in earliest-deadline order. | The next task is easy to find. |
| O2 / NFR3 | Wait for a reply | Cost and latency | Time the 30 answerable questions after the files are ready. Sort the times. | The 27th time is under 5 seconds. | A student can check a detail while planning. |
| O3 / FR7 / NFR4, RAI4 | Correct, single reminder | Instruction-following capability | Schedule 20 valid sends. Separately try 20 cases with retries, changed dates, opt-outs or tasks in review. Check recipient, task, time and service status. | At least 19/20 valid sends accepted in the chosen minute. Zero duplicate, stale or unapproved sends. | Students can see whether the service accepted their reminder. |
| O2 / FR4, FR8 / RAI3 | Private files and public lookup | Tool use and privacy | Use two accounts for 20 checks. Reopen the app and start a new chat with a valid session, then test after sign-out and expiry. Try another student’s file, a public lookup and an outgoing alert. Inspect what each tool receives. | No new sign-in prompt during an active session. Zero unauthorised reads or disclosures. A public answer links to its source, and a web result cannot set a course deadline. | Signing in alone does not keep files private. |

A service status of **accepted** means WhatsApp took the request. Mark a message **delivered** only if the service confirms delivery. A simulated send can test the schedule but cannot count towards the 19 accepted sends.

**Most important test.** Getting the date right. A reminder that arrives on time for the wrong day can still make a student miss the deadline.
