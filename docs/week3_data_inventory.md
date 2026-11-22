# Week 3 · Data inventory

The supplied folder contains **five PDFs and two screenshots**. All 37 PDF pages had readable text. Both screenshots opened and contained dates. They are past course notices selected as examples.

| ID | File in the raw folder | Use and inspection evidence | Date or version clue |
|---|---|---|---|
| S01 | Activity for Module 2.pdf | One page about the Grab case activity. It gives a task but no stated deadline. | Copy supplied for this lab. |
| S02 | Assignment 1[Individual].pdf | Three pages. Page 1 labels 30 April 2026 as the deadline and gives a submission method. | Deadline appears in the brief. |
| S03 | NLP Final Project Question.pdf | Twelve pages. The brief asks for a proposal by the end of Week 11. Keep this as a week, since the brief does not give that date here. | Week 11 is a course week. |
| S04 | Post Module Assessment_SAIA3453_final.pdf | Six pages. Page 1 shows 11 June 2026 as the date and 2 July 2026 as the upload deadline. | Semester II, 2025/2026. |
| S05 | SAIA 2163 — Assignment 2_ Text Vectorization & Embedding Methods.pdf | Fifteen pages. The brief says Week 12 and refers to a deadline. Its print footer also contains a date. The footer is a poor source for a due date. | Assignment Two, Week 12. |
| S06 | Screenshot 2026-11-02 093501.png | Quiz notice, 1413 × 767, RGBA. The opening and due times differ. The instructions also mention a 30-minute limit. | Filename gives 2 Nov 2026. The quiz is dated 23 Apr 2026. |
| S07 | Screenshot 2026-11-02 094157.png | Assignment page, 1361 × 837, RGBA. It shows separate opening and due dates and a submission status. | Filename gives 2 Nov 2026. The displayed due date is 28 Oct 2026. |

**Source and access.** These are student-supplied course files from `D:/raw`. The exact versions and permission to publish them are unknown. The local repo keeps copies under `data/raw/`. The raw files, prepared text and screenshots stay out of Git.

**Why these files matter.** These uploads represent what a student might bring from eLearning after university sign-in. FR2 needs the task and its stated dates. FR5 needs a source for each answer. RAI3 covers private uploads and submission details. These files are inputs for the [Week 2 file reader](week2_architecture_v1.png).

**What Week 3 keeps.** Each PDF text record names its source. The handout joins the pages before splitting the text, so the page number is empty in the Lab 3 export. The [Week 4 follow-up](../data/week4_pdf_pages/manifest.json) adds a PDF viewer page to each passage. Each screenshot links to an RGB copy. Reading dates from those images is a later step. [Notebook](../notebooks/week3_pipeline.ipynb) · [Source and output records](../data/week3_manifest.json)
