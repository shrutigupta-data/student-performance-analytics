"""Run the Student Performance Analytics System."""

from pathlib import Path

import pandas as pd

from functions import (
    SUBJECT_COLUMNS,
    calculate_overall_summary,
    calculate_student_metrics,
    calculate_subject_summary,
    get_top_performers,
    load_student_data,
    validate_student_data,
)


def main():
    """Load the supplied dataset and print its performance analysis."""
    csv_path = Path(__file__).resolve().parent / "students.csv"
    print("=" * 72)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)

    try:
        student_data = load_student_data(csv_path)
        student_data = validate_student_data(student_data)
    except (OSError, pd.errors.ParserError, UnicodeDecodeError, ValueError) as error:
        print(f"Unable to analyze the student dataset: {error}")
        return 1

    student_data = calculate_student_metrics(student_data, SUBJECT_COLUMNS)
    pd.options.display.float_format = "{:.2f}".format

    print("\nDATASET PREVIEW")
    print(student_data.head().to_string(index=False))
    print(f"\nRecords: {len(student_data)} | Columns: {len(student_data.columns)}")
    print("Column names:", ", ".join(student_data.columns))

    print("\nDATAFRAME INFORMATION")
    student_data.info()
    print("\nDESCRIPTIVE STATISTICS")
    print(student_data.describe(include="all").to_string())

    print("\nINDIVIDUAL STUDENT PERFORMANCE")
    performance_columns = [
        "student_id",
        "name",
        "department",
        "total_marks",
        "average_marks",
        "grade",
        "result",
        "attendance",
    ]
    print(student_data[performance_columns].to_string(index=False))

    summary = calculate_overall_summary(student_data, SUBJECT_COLUMNS)
    print("\nOVERALL CLASS PERFORMANCE")
    print(f"Total students: {summary['student_count']}")
    print(f"Overall class average: {summary['class_average']:.2f}")
    print(f"Average class attendance: {summary['average_attendance']:.2f}%")
    print(f"Passed: {summary['pass_count']} ({summary['pass_percentage']:.2f}%)")
    print(f"Failed: {summary['fail_count']} ({summary['fail_percentage']:.2f}%)")

    performer_columns = [
        "student_id",
        "name",
        "department",
        "average_marks",
        "grade",
        "result",
    ]
    print(f"\nHighest student average: {summary['highest_average']:.2f}")
    print(summary["highest_performers"][performer_columns].to_string(index=False))
    print(f"\nLowest student average: {summary['lowest_average']:.2f}")
    print(summary["lowest_performers"][performer_columns].to_string(index=False))

    subject_summary = calculate_subject_summary(student_data, SUBJECT_COLUMNS)
    print("\nSUBJECT-WISE PERFORMANCE")
    print(subject_summary.to_string(index=False))
    highest_subject_average = subject_summary["average_marks"].max()
    lowest_subject_average = subject_summary["average_marks"].min()
    highest_subjects = subject_summary.loc[
        subject_summary["average_marks"].eq(highest_subject_average), "subject"
    ].tolist()
    lowest_subjects = subject_summary.loc[
        subject_summary["average_marks"].eq(lowest_subject_average), "subject"
    ].tolist()
    print("Highest subject average:", ", ".join(highest_subjects))
    print("Lowest subject average:", ", ".join(lowest_subjects))

    print("\nTOP THREE PERFORMERS")
    top_columns = [*performer_columns]
    print(get_top_performers(student_data)[top_columns].to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())