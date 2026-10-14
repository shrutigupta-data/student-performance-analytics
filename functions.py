"""Reusable loading, validation, calculation, and analysis functions."""

import numpy as np
import pandas as pd

SUBJECT_COLUMNS = [
    "english",
    "mathematics",
    "science",
    "computer_science",
]

REQUIRED_COLUMNS = [
    "student_id",
    "name",
    "department",
    *SUBJECT_COLUMNS,
    "attendance",
]
NUMERIC_COLUMNS = [*SUBJECT_COLUMNS, "attendance"]
TEXT_COLUMNS = ["student_id", "name", "department"]


def load_student_data(csv_path):
    """Load student records from a CSV file into a DataFrame."""
    return pd.read_csv(csv_path)


def validate_student_data(df):
    """Validate required fields and return a numeric, validated copy."""
    if df.empty:
        raise ValueError("The dataset is empty; add at least one student record.")

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    data = df.copy()
    missing_values = data[REQUIRED_COLUMNS].isna().any()
    columns_with_missing_values = missing_values[missing_values].index.tolist()
    if columns_with_missing_values:
        raise ValueError(
            "Missing values found in: " + ", ".join(columns_with_missing_values)
        )

    for column in TEXT_COLUMNS:
        blank_values = data[column].astype("string").str.strip().eq("")
        if blank_values.any():
            raise ValueError(f"Blank values are not allowed in '{column}'.")

    student_ids = data["student_id"].astype("string").str.strip()
    if student_ids.duplicated().any():
        raise ValueError("Student IDs must be unique.")

    for column in NUMERIC_COLUMNS:
        converted_values = pd.to_numeric(data[column], errors="coerce")
        if converted_values.isna().any():
            raise ValueError(f"Column '{column}' must contain only numeric values.")
        data[column] = converted_values

        out_of_range = ~data[column].between(0, 100)
        if out_of_range.any():
            raise ValueError(f"Values in '{column}' must be between 0 and 100.")

    return data


def determine_pass_fail(marks):
    """Return Pass only when every subject mark is at least 40."""
    if np.any(np.asarray(marks, dtype=float) < 40):
        return "Fail"
    return "Pass"


def assign_grade(average_marks, pass_fail):
    """Assign a grade, giving a failing student F before checking averages."""
    if pass_fail == "Fail":
        return "F"
    if average_marks >= 90:
        return "A+"
    elif average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    elif average_marks >= 40:
        return "E"
    else:
        return "F"


def calculate_student_metrics(df, subject_columns):
    """Add totals, averages, grades, and results without removing source data."""
    data = df.copy()
    totals = []
    averages = []
    results = []
    grades = []

    for marks in data[subject_columns].itertuples(index=False, name=None):
        total = float(np.sum(marks))
        average = float(np.mean(marks))
        result = determine_pass_fail(marks)
        totals.append(total)
        averages.append(average)
        results.append(result)
        grades.append(assign_grade(average, result))

    data["total_marks"] = totals
    data["average_marks"] = averages
    data["grade"] = grades
    data["result"] = results
    return data


def calculate_subject_summary(df, subject_columns):
    """Return average, highest, and lowest marks for each subject."""
    summaries = []
    for subject in subject_columns:
        marks = df[subject].to_numpy(dtype=float)
        summaries.append(
            {
                "subject": subject,
                "average_marks": float(np.mean(marks)),
                "highest_mark": float(np.max(marks)),
                "lowest_mark": float(np.min(marks)),
            }
        )
    return pd.DataFrame(summaries)


def calculate_overall_summary(df, subject_columns):
    """Return class-wide statistics from student metrics and attendance."""
    student_count = len(df)
    pass_count = int(df["result"].eq("Pass").sum())
    fail_count = int(df["result"].eq("Fail").sum())
    highest_average = float(np.max(df["average_marks"].to_numpy(dtype=float)))
    lowest_average = float(np.min(df["average_marks"].to_numpy(dtype=float)))

    return {
        "student_count": student_count,
        "class_average": float(np.mean(df["average_marks"].to_numpy(dtype=float))),
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "highest_performers": df.loc[
            df["average_marks"].eq(highest_average),
            ["student_id", "name", "department", "average_marks", "grade", "result"],
        ],
        "lowest_performers": df.loc[
            df["average_marks"].eq(lowest_average),
            ["student_id", "name", "department", "average_marks", "grade", "result"],
        ],
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_percentage": pass_count / student_count * 100,
        "fail_percentage": fail_count / student_count * 100,
        "average_attendance": float(np.mean(df["attendance"].to_numpy(dtype=float))),
    }


def get_top_performers(df, top_n=3):
    """Return top performers by average, breaking ties by student ID."""
    return df.sort_values(
        ["average_marks", "student_id"], ascending=[False, True]
    ).head(top_n)