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
