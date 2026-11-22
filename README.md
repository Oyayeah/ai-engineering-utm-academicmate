# UTM AcademicMate

![AcademicMate](src/academicmate.png)

AcademicMate is a planned app for UTM undergraduates. It helps them track deadlines from an assignment PDF or a screenshot of a quiz notice.

## The problem

A lecturer can put a due date inside a brief or post quiz times in a separate notice. A student taking several courses has to find those details and copy them into a planner. The app will read the files, show the line it used and let the student check the date.

## Evidence

- One UTM course lists when each assignment starts and when students must hand it in. For Assignment 1, those are two different weeks. [UTM course example](https://people.utm.my/mnazri/semm-1921-intro-to-mechanical-engineering/)
- A review of college studies found a link between time management and learning outcomes. How often UTM students miss deadlines is still an open question. [Liu, Ma and Jia, 2026](https://doi.org/10.3389/fpsyg.2026.1700298)

## What other tools do

| Tool | What it helps with | What the student still needs |
|---|---|---|
| [MyStudyLife](https://mystudylife.com/) | Plans classes, homework and exams. | Check which line in a brief sets the deadline. |
| [Google Calendar](https://support.google.com/calendar/answer/9901136?hl=en) | Puts a task on a chosen date. | Read the notice and enter the right date. |
| [Todoist](https://www.todoist.com/help/todoist/features/introduction-to-deadlines-in-todoist-uMqbSLM6U) | Tracks a task and its deadline. | Check which submission rules go with that task. |

## Project goals

- **O1** Read the task and dates from an upload. Let the student check and correct them.
- **O2** Answer questions using the uploaded instructions and list confirmed tasks in order of deadline.
- **O3** Send WhatsApp reminders for confirmed tasks. Check that each reminder is sent once to the right student.

## Data sources

Students upload either file on its own. An assignment PDF gives the task and any due date. A quiz screenshot gives whatever the lecturer made visible. A 30-minute time limit alone tells us nothing about when the quiz closes.

We will use these public examples for testing.

- [MIT Problem Set 1, PDF](https://ocw.mit.edu/courses/6-851-advanced-data-structures-spring-2012/7737b417ec851a04c1ca02850cf44706_MIT6_851S12_ps1.pdf) — an assignment with a due date.
- [MIT Quiz 1 announcement, PDF](https://web.mit.edu/6.033/2000/www/handouts/h8-quiz1.pdf) — screenshot the notice on page 1 to test the quiz date and times.
- [UTM Maintenance Management, Quiz 1](https://people.utm.my/shamsul/maintenance-management-frsi-2153/) — a crop showing only the quiz title and weight tests a missing date.

## Weekly progress

| Week | Focus | Files | Status |
|---|---|---|---|
| 1 | Study ChatGPT as a group. Define AcademicMate individually. | [Group notes](docs/week1_observation_sheet.md) · [Group map](docs/week1_system_map.png) · [Project scope](docs/week1_project_scope.md) | Individual scope ready. Group evidence pending. |
| 2 | Decide what the app should do and how to test it. | [Requirements](docs/week2_requirements.md) · [Test plan](docs/week2_evaluation_criteria.md) · [Design](docs/week2_architecture_v1.png) · [Design choices](docs/week2_architecture_decisions.md) | Design and test plan ready. Tests are planned. |
| 3 | Prepare five PDFs and two screenshots. | [Notebook](notebooks/week3_pipeline.ipynb) · [Inventory](docs/week3_data_inventory.md) · [Diagram](docs/week3_pipeline_diagram.png) · [Decisions](docs/week3_pipeline_decisions.md) · [Run evidence](data/week3_manifest.json) | All seven files passed the local checks. Colab run pending. |

## Run Lab 3

The [handout copy](notebooks/week3_handout_cells.ipynb) keeps the original example paths and settings. Use the project notebook below for the seven course files.

1. Open [Google Colab](https://colab.research.google.com/) and upload `notebooks/week3_pipeline.ipynb`. Connect and run **Cell 1** to create the folders.
2. Open the Files panel. Upload the five PDFs and two screenshots from `D:/raw` into `/content/week3_project/data/raw`. Keep their filenames.
3. Run the remaining cells in order. The last code cell should show six **PASS** lines, one for each PDF and one for the two screenshots together.
4. Choose **File → Download → Download .ipynb** to save the run in the repo’s `notebooks/` folder. Save the files under `week3_project/data` before Colab resets.

The saved notebook was tested locally. In VS Code, use a Python notebook kernel with pandas, Pillow and pypdf. To run a local copy, replace the Colab project path in Cells 1, 3 and 7 with your repo path. Put the seven files in `data/raw/`. Full course text and images stay local.
