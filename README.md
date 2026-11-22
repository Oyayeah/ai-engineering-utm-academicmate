# UTM AcademicMate

![AcademicMate](src/academicmate.png)

AcademicMate is a proposed AI assistant for UTM students. A student signs in once with their university account on their device. They can reopen AcademicMate, start a new chat or upload an eLearning file while their session is active. They can ask “What do I need to submit?” and see the part of the file that answers it. If reminders are on, the assistant schedules clear deadlines automatically.

## The problem

A lecturer can put a due date inside a brief or post quiz times in a separate notice. A student taking several courses has to find those details and copy them into a planner. The assistant will show where it found each date. It will ask the student if a date is missing or unclear. Students can correct a saved date.

The proposed service keeps uploads in storage approved by the university and limits access to the student who uploaded them. For a separate public question, its web tool can read an approved public page and link to it. Private files and university credentials stay out of web requests. UTM sign-in and these controls still need to be built and tested.

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

- **O1** Read the task and dates from an upload. Save clear dates automatically and ask about missing or conflicting ones.
- **O2** Answer questions about the student’s assignment with a source. Show upcoming tasks in date order.
- **O3** When a student turns on WhatsApp reminders, send one alert per task at the student’s chosen time.

## Data sources

Students upload either file on its own. An assignment PDF gives the task and any due date. A quiz screenshot gives whatever the lecturer made visible. A 30-minute time limit alone tells us nothing about when the quiz closes.

The Week 3 and Week 4 labs use five student-supplied PDFs and two screenshots. The following public examples are also available for testing.

- [MIT Problem Set 1, PDF](https://ocw.mit.edu/courses/6-851-advanced-data-structures-spring-2012/7737b417ec851a04c1ca02850cf44706_MIT6_851S12_ps1.pdf) — an assignment with a due date.
- [MIT Quiz 1 announcement, PDF](https://web.mit.edu/6.033/2000/www/handouts/h8-quiz1.pdf) — screenshot the notice on page 1 to test the quiz date and times.
- [UTM Maintenance Management, Quiz 1](https://people.utm.my/shamsul/maintenance-management-frsi-2153/) — a crop showing only the quiz title and weight tests a missing date.

## Weekly progress

| Week | Focus | Files | Status |
|---|---|---|---|
| 1 | Study ChatGPT as a group. Define AcademicMate individually. | [Group notes](docs/week1_observation_sheet.md) · [Group map](docs/week1_system_map.png) · [Project scope](docs/week1_project_scope.md) | Individual scope ready. Group evidence pending. |
| 2 | Decide what the app should do and how to test it. | [Requirements](docs/week2_requirements.md) · [Test plan](docs/week2_evaluation_criteria.md) · [Design](docs/week2_architecture_v1.png) · [Design choices](docs/week2_architecture_decisions.md) | Design and test plan ready. Tests are planned. |
| 3 | Prepare five PDFs and two screenshots. | [Notebook](notebooks/week3_pipeline.ipynb) · [Inventory](docs/week3_data_inventory.md) · [Diagram](docs/week3_pipeline_diagram.png) · [Decisions](docs/week3_pipeline_decisions.md) · [Run evidence](data/week3_manifest.json) | All seven files passed the local checks. Colab run pending. |
| 4 | Check whether the saved files support answers and reminders. | [Data quality report](docs/week4_data_quality_report.md) · [PDF](docs/week4_data_quality_report.pdf) | **GO WITH CONDITIONS for local sample testing.** All 146 passages point to the correct PDF page. Use simulated reminders for the sample dates. |

To rebuild the Week 4 page references after Lab 3, run `python src/add_pdf_pages.py` from the repo with `pypdf` installed. The [page record](data/week4_pdf_pages/manifest.json) points to the local passages. Page 1 means the first page in the PDF viewer. The original Lab 3 exports still reproduce the handout.

## Run Lab 3

Use approved files for a hosted Colab run. The seven course files used in these labs were checked locally.

1. Open [Google Colab](https://colab.research.google.com/) and upload `notebooks/week3_pipeline.ipynb`. Connect and run **Cell 1** to create the folders.
2. Open the Files panel. Upload the five PDFs and two screenshots into `/content/week3_project/data/raw` only if cleared for hosted use. The notebook expects the original filenames.
3. Run the remaining cells in order. The last code cell should show six **PASS** lines, one for each PDF and one for the two screenshots together.
4. Choose **File → Download → Download .ipynb** to save the run in the repo’s `notebooks/` folder. Save the files under `week3_project/data` before Colab resets.

The saved notebook was tested locally. In VS Code, use a Python notebook kernel with pandas, Pillow and pypdf. To run a local copy, replace the Colab project path in Cells 1, 3 and 7 with your repo path. Put the seven files in `data/raw/`. Full course text and images stay local.
