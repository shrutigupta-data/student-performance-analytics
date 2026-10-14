# Student Performance Analytics System

A beginner-friendly command-line project that loads synthetic student records from CSV, validates them with Pandas, calculates performance metrics with NumPy, and presents class and subject summaries.

## Objective

Analyze student marks and attendance consistently, including each student's total and average marks, grade, pass/fail result, subject statistics, class statistics, and top performers.

## Technologies

- Python 3
- NumPy
- Pandas
- `unittest` from Python's standard library

## Features

- Validates required columns, empty data, missing values, text fields, numeric values, unique IDs, and 0-100 ranges.
- Calculates four-subject totals and averages, grades, and pass/fail results.
- Reports class statistics, attendance, subject comparisons, tied highest/lowest student averages, and the top three students.
- Resolves `students.csv` relative to `main.py`, so launch location does not matter.

## Dataset

`students.csv` contains 24 synthetic student records. Its columns are `student_id`, `name`, `department`, `english`, `mathematics`, `science`, `computer_science`, and `attendance`. Student identifiers are unique; the four subject marks and attendance are percentages from 0 to 100. The data includes both passing and failing students.

## Grading and Pass/Fail Rules

A student passes only if every subject mark is at least 40. A mark below 40 in any subject means the result is `Fail` and the grade is `F`, regardless of average. Otherwise, grades are assigned by average: 90+ is A+, 80-<90 A, 70-<80 B, 60-<70 C, 50-<60 D, and 40-<50 E. Attendance is reported separately and does not affect grades or results.

## Project Files

```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── requirements.txt
├── README.md
├── Project_Documentation.md
├── test_project.py
└── .gitignore
```

## Installation

Create and activate a virtual environment from this directory.

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

The program prints a dataset preview and information, student-level results, overall class statistics, subject statistics, highest/lowest averages, and the top three performers.

## Run the Tests

```bash
python -m unittest -v
```

## Actual Analysis Results

Verified by running `python3 main.py` on the supplied dataset:

- Students analyzed: 24.
- Overall class average: 72.22/100; average attendance: 85.83%.
- Pass/fail: 21 passed (87.50%) and 3 failed (12.50%).
- Highest student average: Priya Shah (STU022), 97.25; lowest: Daniel Park (STU021), 40.00.
- Highest subject average: computer science, 74.83; lowest: English, 70.67.
- Top three: Priya Shah (97.25), Leo Martinez (93.50), and Aarav Mehta (93.00).

## GitHub and Submission

Planned repository name: `student-performance-analytics`.

Repository URL: **[REPLACE WITH THE ACTUAL GITHUB REPOSITORY URL]**. Do not use this placeholder as a submission link. Create the repository using the visibility and accessibility required by the EWB Courses trainer, upload or push all project files, then update this README and `Project_Documentation.md` with the actual URL and upload the documentation update. Verify the final repository in a browser. Submit that repository URL through the Google Form supplied by EWB Courses; its URL was not provided here, so it is not included or claimed as submitted.

1. Sign in to GitHub and create a repository named `student-performance-analytics`.
2. Set its visibility and accessibility as instructed by the EWB Courses trainer.
3. Upload or commit every file in this project folder.
4. Open the repository in a browser and confirm the required files are visible.
5. Replace the URL placeholder in this README and `Project_Documentation.md` with the real repository URL, then push that update.
6. Verify the final repository again and submit its URL using the EWB Courses Google Form. The form link must come from the course; it was not provided here.

See [Project_Documentation.md](Project_Documentation.md) for the ten-section assignment documentation and detailed upload checklist.