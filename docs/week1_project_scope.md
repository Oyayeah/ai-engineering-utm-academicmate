# Week 1 · UTM AcademicMate

**Domain** · University course support and student planning.

**Users** · UTM undergraduates taking several courses.

## Problem and evidence

An assignment brief gives students work to hand in. A quiz notice tells them when to attend or when an online quiz closes. The details can be easy to mix up when copying them into a calendar. Students who want help understanding a brief may also have to decide whether to upload course material to an outside chat service. AcademicMate proposes a university-managed place to ask.

- In UTM's mechanical engineering course, Assignment 1 starts in week 5 and is due in week 6. To set a reminder, a student still needs the actual date. [UTM assignment schedule](https://people.utm.my/mnazri/semm-1921-intro-to-mechanical-engineering/)
- Two reviews give the wider background. Managing one's own work was a common focus in studies on putting off schoolwork. Better time management was also linked to better learning outcomes. Neither review counted missed UTM deadlines. [Salguero-Pazos and Reyes-de-Cózar, 2023](https://doi.org/10.1016/j.ijer.2023.102228) · [Liu, Ma and Jia, 2026](https://doi.org/10.3389/fpsyg.2026.1700298)

## Existing tools and the gap

| Tool | What it does | Limit for this project |
|---|---|---|
| [MyStudyLife](https://mystudylife.com/) | Keeps homework, classes and exams in one plan. | A planner entry alone does not show which line in the brief supports it. |
| [Google Calendar](https://support.google.com/calendar/answer/9901136?hl=en) | Lets a student enter a task and date. | The student still needs to pick the date from the notice. |
| [Todoist](https://www.todoist.com/help/todoist/features/introduction-to-deadlines-in-todoist-uMqbSLM6U) | Separates a work date from a final deadline. | A deadline alone does not tell the student what to submit. |

A student signs in once with their UTM account on their device. While signed in, they can come back to upload an eLearning file or ask a new question. They can ask what to submit, read the cited passage and get an automatic reminder for a clear deadline after turning reminders on.

## Project goals

- **O1** Read the task and dates from an upload. Save clear dates automatically and ask about missing or conflicting ones.
- **O2** Answer questions about the student’s assignment with a source. Show upcoming tasks in date order.
- **O3** When a student turns on WhatsApp reminders, send one alert per task at the student’s chosen time.

## Data sources and scope

One assignment PDF or quiz screenshot is enough. Students choose their own files. The app will read the text, flag missing dates and show where each answer came from. The calendar shows upcoming dates in order. Unclear dates go back to the student. A separate web tool can read approved public pages and cite them for background questions. File search, public lookup and scheduling are the assistant’s planned tools. The student handles eLearning downloads and submissions.

| Public test source | What to look for |
|---|---|
| [MIT 6.851, Problem Set 1, spring 2012 (PDF)](https://ocw.mit.edu/courses/6-851-advanced-data-structures-spring-2012/7737b417ec851a04c1ca02850cf44706_MIT6_851S12_ps1.pdf) | Page 1 gives 23 February as the due date. A student can also ask which three operations the solution must support. |
| [MIT 6.033, Quiz 1 announcement, 2000 (PDF)](https://web.mit.edu/6.033/2000/www/handouts/h8-quiz1.pdf) | Screenshot the notice on page 1. The handout is dated 22 February. The quiz is on 3 March, from 2 to 3 pm. |
| [UTM FRSI 2153, Quiz 1, 2025](https://people.utm.my/shamsul/maintenance-management-frsi-2153/) | Crop the “Quiz 1 (10%)” heading. The weight is visible. The date is missing from this crop. |

The old dates are test cases. Personal uploads and phone numbers stay out of the public repo.

## How it compares with EduAdvisor

Both apps use retrieval-augmented generation (RAG). That means finding a passage first and using it to write an answer. EduAdvisor answers questions about courses and graduation. AcademicMate uses the student's own notices to answer “What do I hand in?” Its calendar answers “What is due next?”

## Risks and checks

| What could go wrong? | What we will check |
|---|---|
| A quiz opening time is saved as its deadline. | Match the closing label to the time. Hold a reminder if the wording is unclear. |
| An answer adds a rule the lecturer never gave. | Show the source line or say the upload does not say. |
| Another student sees a file or phone number. | Use university sign-in, check who owns each file, and test with two accounts. Check that public lookup sends no private text. |
| A reminder goes twice or fails. | Track each scheduled send and show its status beside the task. |

We will compare dates and answers with a hand-checked list, then test the calendar order and WhatsApp sends. Sending a real reminder needs access to the WhatsApp service.
