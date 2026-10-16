# UTM AcademicMate — AI Academic Planning Assistant

## Project Overview

UTM AcademicMate is an AI-powered academic planning assistant designed for students at UTM. It helps students organise their academic workload by extracting important information from uploaded PDFs and screenshots, maintaining a central deadline schedule, and providing reminders through WhatsApp.

The system also uses Retrieval-Augmented Generation (RAG) to answer questions about uploaded course materials and support students in planning and prioritising their academic tasks.

## Problem Statement

University students may need to manage assignments, quizzes, examinations and course instructions distributed across multiple documents and learning resources. Manually organising these details can require additional effort and may cause important deadlines to be overlooked.

UTM AcademicMate aims to simplify this process through document information extraction, document-grounded question answering and automated deadline reminders.

## Project Objectives

1. Develop a module to extract academic activities and deadlines from uploaded PDFs and screenshots, with student verification.
2. Implement a RAG-based assistant for course-related question answering and academic task prioritisation.
3. Implement and evaluate a WhatsApp reminder mechanism for upcoming academic deadlines.

## Target Users

Undergraduate students at Universiti Teknologi Malaysia who manage multiple courses and need support with academic planning.

## Main Features

- PDF and screenshot uploads
- Academic activity and deadline extraction
- Student verification and correction of extracted information
- Unified academic task calendar
- RAG-based question answering grounded in uploaded materials
- Academic task prioritisation and study planning
- WhatsApp deadline reminders

## Proposed Technologies

- Python
- Streamlit
- PDF and image text extraction / OCR
- Large Language Model (LLM)
- Retrieval-Augmented Generation (RAG)
- Vector database
- SQLite
- WhatsApp Business Platform API

These are proposed technologies and may be refined during development.

## Data Sources

Public academic documents:
- UTM Academic Calendar: https://amd.utm.my/academic-calendar/
- UTM Faculty of Computing undergraduate resources: https://comp.utm.my/undergraduate/
- UTM Faculty of Science academic handbooks: https://science.utm.my/undergraduate/academic-handbook/

Personalised runtime inputs:
- Student-uploaded course outlines
- Assignment instructions
- Lecture PDFs
- Screenshots of course information

Only authorised materials will be used for testing. Private student information and restricted course documents will not be published in this repository.

## Evaluation Plan

The system will be evaluated using:
- Accuracy of extracted academic dates and activity details
- Accuracy and source relevance of RAG responses
- Correctness of task prioritisation
- Reliability of scheduled WhatsApp reminders
- Handling of missing, ambiguous or conflicting information

## Responsible AI Considerations

The project will address inaccurate date extraction, unsupported AI answers, student data privacy, and notification failures. Students will be able to review extracted dates, and the assistant should indicate when the uploaded materials do not contain sufficient evidence to answer a question.

## Project Scope

The prototype will use student-uploaded PDFs and screenshots. Direct automated access to UTM eLearning is outside the initial scope.

## Project Status

Initial project scoping and repository setup.