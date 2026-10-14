# Student Performance Analytics System

## 1. Project Title and Student Details

**Project title:** Student Performance Analytics System  
**Student name:** Shruti Gupta  
**Course:** Python with AI  
**Submission deadline:** 15 October 2026, on or before

## 2. Objective

The system reads student records from a CSV file, validates the input, and analyzes marks and attendance. It provides consistent student totals, averages, grades and results, alongside useful class and subject summaries. It is a basic data-analysis project and does not use machine learning or prediction.

## 3. Technologies Used

- Python 3 for program logic and terminal output.
- NumPy for sums, means, minimums, maximums, and numerical pass checks.
- Pandas for CSV loading, DataFrame validation, filtering, sorting, and descriptive statistics.
- Python `unittest` for automated tests (standard library).
- VS Code may be used as the editor; no claim is made that any GitHub account or repository has been created.

## 4. Dataset Description

`students.csv` contains 24 synthetic student records. The columns are `student_id`, `name`, `department`, `english`, `mathematics`, `science`, `computer_science`, and `attendance`. The four subject fields contain marks on a 0-100 scale. Attendance is recorded as a percentage and analyzed separately. The supplied file includes passing and failing examples, varied marks, unique IDs, and no intentionally missing values.

## 5. Implementation

1. `main.py` builds the CSV path relative to the script and calls `load_student_data()` to read it with Pandas.
2. `validate_student_data()` checks for an empty dataset, required columns, missing values, blank text fields, duplicate IDs, non-numeric values, and out-of-range marks or attendance. Invalid input produces an actionable error rather than being replaced.
3. `calculate_student_metrics()` uses a loop over student rows and NumPy to calculate each total and average, then applies the reusable pass/fail and grading functions.
4. `calculate_subject_summary()` loops through the shared `SUBJECT_COLUMNS` list to calculate each subject's mean, maximum, and minimum.
5. `calculate_overall_summary()` calculates class averages, pass/fail counts and percentages, attendance, and all tied highest/lowest students. Pandas selects and sorts student rows for the output and top-three ranking.
6. `main.py` presents the preview, DataFrame information, descriptive statistics, student table, and analysis in readable terminal sections.

Pass/fail rule: all four subject marks must be at least 40 to pass. Failing any subject gives result `Fail` and grade `F`. For passing students, average thresholds are A+ (90+), A (80-<90), B (70-<80), C (60-<70), D (50-<60), and E (40-<50). Attendance does not determine pass/fail.

## 6. Key Features

- Input validation with clear error messages.
- Per-student totals (maximum 400), averages, grades, and pass/fail results.
- Overall class average, tied highest and lowest student averages, pass/fail counts and percentages, and average attendance.
- Subject averages, maximums, minimums, and identification of the highest- and lowest-average subjects.
- Top three students sorted by average descending, then student ID ascending for ties.
- Automated tests for rules, calculations, summaries, and invalid data.

## 7. Output / Screenshots (Optional)

No screenshot is included. To capture a genuine screenshot, run `python main.py` in the VS Code terminal, arrange the relevant output visibly, and use macOS Screenshot (`Shift-Command-4`) or the system screenshot utility. Save the image in a `screenshots/` folder and update this section to identify it. Do not include a simulated or recreated output image.

## 8. Final Outcome

The program was executed with `python3 main.py` against the supplied CSV and analyzed all 24 records successfully.

- Student records: 24.
- Class average: 72.22/100; average attendance: 85.83%.
- Pass/fail: 21 passed (87.50%) and 3 failed (12.50%).
- Highest student average: Priya Shah (STU022), 97.25; lowest: Daniel Park (STU021), 40.00.
- Highest/lowest subject averages: computer science, 74.83; English, 70.67.
- Top three students: Priya Shah (STU022), 97.25; Leo Martinez (STU005), 93.50; Aarav Mehta (STU001), 93.00.

The automated test suite also completed successfully: 8 tests passed.

## 9. Challenges and Learning

- **Challenge encountered:** One important challenge was making sure that the analysis used consistent rules and did not produce misleading results when the input data was invalid. For example, a student must fail if even one subject mark is below 40, regardless of the overall average. Missing values, duplicate student IDs, non-numeric entries, and marks or attendance outside the 0-100 range also needed to be handled before calculations could be trusted.

- **How it was addressed:** I organised the project into reusable functions so that validation, calculations, and summaries could be handled separately. The `validate_student_data()` function checks the required columns, missing and blank values, duplicate IDs, numeric fields, and allowed ranges. The `determine_pass_fail()` and `assign_grade()` functions apply the pass/fail and grading rules consistently. I also used Python's `unittest` framework to check pass/fail conditions, grade boundaries, student calculations, class and subject summaries, duplicate IDs, and out-of-range marks. Finally, I ran the main program and test suite against the supplied dataset to verify that the analysis completed successfully.

- **What I learned:** I learned how to load CSV data into a Pandas DataFrame, inspect and validate records, and use functions, loops, and conditions to organise a Python data-analysis workflow. I developed a clearer understanding of using NumPy for totals, averages, and numerical checks, and Pandas for descriptive statistics, filtering, sorting, and summarising student and subject performance. I also learned why input validation, clearly defined business rules, and testing edge cases are important for reliable results. The project helped me practise turning raw tabular data into understandable summaries using the Python concepts required for the assignment, without needing machine learning or prediction.

## 10. GitHub Repository

Repository name: `student-performance-analytics`  
Repository URL: **[REPLACE WITH THE ACTUAL GITHUB REPOSITORY URL AFTER CREATING IT]**

Manual submission checklist:

1. Sign in to GitHub or create an account.
2. Create a repository named `student-performance-analytics`.
3. Choose visibility and accessibility according to the EWB Courses trainer's instructions.
4. Upload or commit all project files from this folder.
5. Open the repository in a browser and verify the required files are visible.
6. Copy the actual repository URL and replace the placeholder in this file and `README.md`.
7. Push/commit the documentation update to GitHub.
8. Verify the final repository and updated URL again.
9. Submit the correct repository link through the Google Form provided by EWB Courses. The form URL was not supplied, and submission has not been claimed.