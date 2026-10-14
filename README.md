# 🎓 Student Performance Analytics System

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243?logo=numpy&logoColor=white)
![Project](https://img.shields.io/badge/Project-Completed-success)

A Python-based data analysis project that evaluates student academic performance using **Python, NumPy, and Pandas**. The system processes student records, calculates marks and averages, assigns grades, determines pass/fail results, and generates meaningful class-wide and subject-wise performance summaries.

## 📌 Project Overview

The **Student Performance Analytics System** was developed as part of the Python with AI course assignment by EWB Courses.

The project demonstrates how Python programming and data analysis libraries can be used to transform structured student data into useful performance insights.

### 🎯 Objectives

- Load and analyse student records stored in a CSV file.
- Calculate total marks and average marks for each student.
- Assign grades and determine pass/fail results using defined rules.
- Analyse overall class performance and attendance.
- Compare subject-wise averages, highest marks, and lowest marks.
- Identify the highest-performing students and the top three performers.
- Validate input data and test calculations for reliable results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming logic, functions, loops, and conditions |
| Pandas | CSV loading, DataFrame operations, validation, filtering, sorting, and analysis |
| NumPy | Numerical calculations, including sums, means, minimums, and maximums |
| Python `unittest` | Automated testing of calculations, grading rules, and input validation |
| CSV | Storage of student records |

## ✨ Key Features

- **Data validation:** Checks required columns, missing values, blank text fields, duplicate student IDs, non-numeric values, and invalid ranges.
- **Student performance analysis:** Calculates totals, averages, grades, and pass/fail results.
- **Class performance summary:** Reports student count, class average, average attendance, and pass/fail percentages.
- **Subject-wise analysis:** Calculates average, highest, and lowest marks for each subject.
- **Performance ranking:** Identifies students with the highest and lowest averages and lists the top three performers.
- **Error handling:** Displays meaningful error messages when the input dataset cannot be processed.
- **Automated testing:** Tests the main calculation rules and validation conditions.

## 📂 Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
├── test_project.py
├── requirements.txt
├── README.md
└── Project_Documentation_completed.md
```

**File descriptions:**

- `main.py` — Runs the program and displays the analysis.
- `functions.py` — Contains reusable functions for data validation, calculations, grading, and summaries.
- `students.csv` — Contains the student dataset.
- `test_project.py` — Contains automated unit tests.
- `requirements.txt` — Lists the required Python libraries.
- `README.md` — Provides an overview and instructions for using the project.
- `Project_Documentation_completed.md` — Documents the objective, technologies, dataset, implementation, key features, final outcome, challenges, and learning.

## 📊 Dataset Description

The project uses a CSV dataset containing **24 synthetic student records**.

| Column | Description |
|---|---|
| `student_id` | Unique student identifier |
| `name` | Student name |
| `department` | Student's department |
| `english` | English marks |
| `mathematics` | Mathematics marks |
| `science` | Science marks |
| `computer_science` | Computer Science marks |
| `attendance` | Attendance percentage |

All subject marks and attendance values are recorded on a scale of 0–100. The dataset includes both passing and failing examples.

## 📐 Grading and Pass/Fail Rules

A student passes only when **all four subject marks are at least 40**. If any subject mark is below 40, the student's result is `Fail` and the grade is `F`, regardless of the overall average.

For students who pass, grades are assigned according to their average marks:

| Average Marks | Grade |
|---|---|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| 40 to below 50 | E |

Attendance is analysed separately and does not affect grades or pass/fail results.

## 🚀 Getting Started

### 1. Install Python

Install Python 3 on your computer if it is not already available.

### 2. Download or Clone the Repository

After creating the GitHub repository, clone it using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd student-performance-analytics
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 3. Create a Virtual Environment (Recommended)

For macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Project

For macOS or Linux:

```bash
python3 main.py
```

Alternatively, use:

```bash
python main.py
```

The program displays the dataset preview, descriptive statistics, individual student results, overall class performance, subject-wise analysis, and top three performers.

## 🧪 Run Automated Tests

Execute the test suite using:

```bash
python -m unittest -v
```

The tests cover pass/fail conditions, grade boundaries, student calculations, subject and overall summaries, duplicate student IDs, and invalid marks.

**Verified result:** All 8 automated tests passed.

## 📈 Project Results

The program was executed successfully against the supplied dataset of 24 student records.

### Overall Class Performance

| Metric | Result |
|---|---:|
| Total students analysed | 24 |
| Overall class average | 72.22/100 |
| Average attendance | 85.83% |
| Students passed | 21 |
| Pass percentage | 87.50% |
| Students failed | 3 |
| Fail percentage | 12.50% |

### Subject-Wise Performance

| Subject | Average Marks |
|---|---:|
| English | 70.67 |
| Computer Science | 74.83 |

Computer Science recorded the highest subject average, while English recorded the lowest subject average.

### Highest and Lowest Student Averages

| Category | Student | Student ID | Average |
|---|---|---|---:|
| Highest average | Priya Shah | STU022 | 97.25 |
| Lowest average | Daniel Park | STU021 | 40.00 |

### 🏆 Top Three Performers

| Rank | Student | Student ID | Average Marks |
|---:|---|---|---:|
| 1 | Priya Shah | STU022 | 97.25 |
| 2 | Leo Martinez | STU005 | 93.50 |
| 3 | Aarav Mehta | STU001 | 93.00 |

*Note: These results are based on the supplied synthetic dataset.*

## 📚 Concepts Demonstrated

This project applies core Python programming and introductory data analysis concepts, including:

- Variables, data types, loops, and conditional statements.
- Reusable functions and modular programming.
- NumPy numerical calculations.
- Pandas DataFrames and CSV processing.
- Data validation and error handling.
- Descriptive statistics and data summarisation.
- Filtering, sorting, and ranking.
- Automated testing with Python's `unittest` framework.

## 💡 Challenges and Learning

During this project, I focused on applying consistent rules to student marks and ensuring that invalid input data would not produce misleading results. I organised the program into reusable functions to separate validation, calculations, grading, and analysis.

I learned how to work with CSV data using Pandas, perform numerical operations with NumPy, apply functions and loops to process records, and use automated tests to check calculations and important edge cases. This project strengthened my understanding of how raw tabular data can be transformed into meaningful analytical insights using Python.

## 🔮 Future Improvements

Possible extensions to the current project include:

- Creating interactive dashboards for student performance.
- Adding charts to visualise marks and subject comparisons.
- Exporting the analysis results to CSV or Excel.
- Developing a graphical user interface for easier use.

These are potential improvements and are not part of the current implementation.

## 📖 Project Documentation

For a more detailed explanation of the project's objective, dataset, implementation, features, outcome, challenges, and learning, refer to the project documentation included in the repository.

## 👩‍💻 Author

**Shruti Gupta**

Course: Python with AI  
Project: Student Performance Analytics System  
Institution: EWB Courses

## 📅 Submission Information

Course assignment deadline: **15 October 2026**

This project was developed to demonstrate Python fundamentals, NumPy, Pandas, and data analysis as specified in the course assignment.

---

⭐ *A practical introduction to Python-based data analysis, student performance metrics, and data validation.*
