# AcademicMate · Data quality and bias report

## 1. Project and data overview

In the proposed service, a UTM student signs in once on their device. They can return to the same university session to upload an assignment or ask another question. They can ask what to submit and turn on automatic reminders. This audit covers **FR2** (read tasks and dates correctly) and **FR5** (show the PDF page or screenshot text behind an answer). [Week 2 requirements](week2_requirements.md)

**Scope.** Week 3 Part B, paths A (PDF text) and C (images). Five PDFs produced 117 text pieces. Two past screenshots produced two PNGs. The follow-up split 29 pieces at page breaks and saved 146 passages with page numbers. All seven source and output file hashes matched [data/week3_manifest.json](../data/week3_manifest.json). The [inventory](week3_data_inventory.md) lists the sources. The [Week 4 manifest](../data/week4_pdf_pages/manifest.json) names the new passage file under `data/week4_pdf_pages/`.

| Local output | Where it was checked |
|---|---|
| PDF text | S02 uses `data/processed/prepared_text.jsonl`. S01, S03, S04 and S05 each use `data/processed/<source ID>/prepared_text.jsonl`. |
| Screenshots | The [image list](../data/processed/image_manifest.csv) gives the exact PNG path under `data/processed/images/` for S06 and S07. Both match the same Part B manifest. |

**Sample.** Two pieces from each PDF and both screenshots, 12 items in total. The PDF row numbers, counted from 1, were S01 (1, 2), S02 (1, 10), S03 (2, 5), S04 (2, 3) and S05 (3, 36). These cover task instructions, exact dates, teaching weeks and a missing deadline. This small, deliberately chosen sample cannot represent all UTM courses.

## 2. Five-dimension quality scorecard

| Dimension | Observed evidence | Effect and decision |
|---|---|---|
| Completeness | The Lab 3 export had 117 empty page fields. After the fix, all 146 passages name the file and the correct PDF viewer page. | **Pass** for FR5 page references. A student can open the cited page. |
| Consistency | In both screenshot pairs, “Opened” and “Due” still label different values after resizing. | The two roles can be told apart when reading the image. **Pass** for these two copies. |
| Accuracy | All ten sampled passages matched the source text when spacing was ignored. Both saved images preserved the displayed dates and times. | **Pass** for the 12 comparisons. The app’s own answers and date reading still need testing. |
| Timeliness | S06 and S07 were chosen as past examples. In both screenshots the opening and due dates match the originals. | **Pass** for testing how the app reads dates. An old date is useful for checking that a past task gets no reminder. |
| Uniqueness | All seven source hashes and all 146 new passage IDs were distinct. No two passages matched after ignoring case and repeated spaces. | **Pass** for exact duplicates. Two files can still describe one task. |

## 3. Validation findings

| Rule | Tested and observed | Action |
|---|---|---|
| V1 · FR2. A saved passage must match the original text in order, ignoring spacing. A saved notice must keep each opening and due label with the same date and time. | All 12 passed, 0 failed, 0 unverified. Compared ten passages with the original PDF text and read the two pairs of images side by side. | Keep these copies for the audit. If a label or value changes, check the original before scheduling anything. |
| V2 · FR5. Each passage must name its file and match text on the stated PDF page. Page 1 is the first page in the viewer. | Before the fix, 0/117 had a page. After the fix, 146/146 passed across 37 pages in five PDFs. S02 row 10 now gives separate passages for pages 2 and 3. | Use the new passages for citations. Rerun the check whenever a PDF or the way it is split changes. |

## 4. Duplicate, anomaly and coverage findings

| Case | What the sample shows | Effect |
|---|---|---|
| Assignments with an exact, relative or missing deadline | S02 states a calendar date. S03 gives a teaching week. The S01 activity gives no deadline in its PDF. | Keep a missing date blank. A week alone cannot schedule a reminder for a particular day. |
| Notices with opening and closing times | Both screenshots show each label. Only S06 is a quiz and it also gives an attempt length. | A time limit is a duration. The closing time sets the end of the quiz window. More quiz layouts need testing. |

S07 lists an attachment with the same filename as S01. Two different files may describe one task. Check the course and task before sending a second reminder.

## 5. Bias assessment

**Inferred risk.** The five PDFs became searchable text. The two screenshots became images only. Both images still show dates, but a tool that searches only the saved text would miss both notices. Students who receive screenshot notices could get less complete answers. Read the image text and test it against the visible labels before enabling screenshot reminders. [Week 3 preparation choices](week3_pipeline_decisions.md)

## 6. Privacy, rights and governance

**Observed.** The student supplied seven course files for a local class example. S07 includes a submission status that the reminder does not need. The audit uses IDs and counts. The originals and prepared course content stay local.

**Not Verified.** The exact versions, owner approval for use in a live service, permission to share, and consent from anyone mentioned in the files are undocumented. The proposed app reuses the student’s signed-in session across visits and checks file ownership on each request. Before a pilot, the project owner should confirm approved storage, model access and deletion with the university. Restrict each file to its student, keep files and credentials out of web lookups, and send only a generic reminder through an optional messaging service.

## 7. Mitigation and impact on requirements

| Priority | Who and when | Check before use |
|---|---|---|
| 1. Keep the PDF page (FR5). | Completed locally. The developer repeats the check after a file or reader change. | All 146 passages matched their pages. Joining each original piece’s parts recovered its text, ignoring spacing. Table layout can still be lost. |
| 2. Test reminder behaviour (FR2). | Developer, before enabling sends and after a scheduling change. | Use the past screenshots for a simulated run and a made-up future notice for a scheduled alert. Also test a missing date and a teaching week. |

## 8. Quality-gate decision

**GO WITH CONDITIONS for local testing on these samples.** The 12 source comparisons passed, and all 146 passages matched their PDF pages. Keep course content local and use simulated reminders. Screen capture age is expected here. Rerun the checks after any source or preparation change. Before a live pilot, confirm permitted use and test screenshot reading, saved sessions and delivery with suitable test accounts.
