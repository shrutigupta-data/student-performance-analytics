"""Unit tests for student performance calculations and validation."""

import unittest

import pandas as pd

from functions import (
    SUBJECT_COLUMNS,
    assign_grade,
    calculate_overall_summary,
    calculate_student_metrics,
    calculate_subject_summary,
    determine_pass_fail,
    validate_student_data,
)


def make_test_data():
    """Create a small dataset with hand-checkable expected results."""
    return pd.DataFrame(
        [
            ["T001", "Alex Example", "Science", 80, 90, 70, 60, 90],
            ["T002", "Blair Sample", "Arts", 40, 40, 40, 40, 80],
            ["T003", "Casey Test", "Engineering", 100, 39, 100, 100, 70],
        ],
        columns=[
            "student_id",
            "name",
            "department",
            *SUBJECT_COLUMNS,
            "attendance",
        ],
    )


class StudentPerformanceTests(unittest.TestCase):
    def test_passes_when_every_subject_is_at_least_40(self):
        self.assertEqual(determine_pass_fail([40, 60, 80, 100]), "Pass")

    def test_fails_when_one_subject_is_below_40(self):
        self.assertEqual(determine_pass_fail([90, 39, 90, 90]), "Fail")

    def test_grade_boundaries(self):
        expected_grades = {
            90: "A+",
            80: "A",
            70: "B",
            60: "C",
            50: "D",
            40: "E",
        }
        for average, grade in expected_grades.items():
            with self.subTest(average=average):
                self.assertEqual(assign_grade(average, "Pass"), grade)

    def test_failing_student_always_receives_f(self):
        self.assertEqual(assign_grade(90, "Fail"), "F")

    def test_student_totals_averages_grades_and_results(self):
        metrics = calculate_student_metrics(make_test_data(), SUBJECT_COLUMNS)
        self.assertEqual(metrics.loc[0, "total_marks"], 300)
        self.assertEqual(metrics.loc[0, "average_marks"], 75)
        self.assertEqual(metrics.loc[0, "grade"], "B")
        self.assertEqual(metrics.loc[0, "result"], "Pass")
        self.assertEqual(metrics.loc[2, "average_marks"], 84.75)
        self.assertEqual(metrics.loc[2, "grade"], "F")

    def test_subject_and_overall_summaries(self):
        metrics = calculate_student_metrics(make_test_data(), SUBJECT_COLUMNS)
        subject_summary = calculate_subject_summary(metrics, SUBJECT_COLUMNS)
        english = subject_summary.loc[subject_summary["subject"].eq("english")].iloc[0]
        self.assertAlmostEqual(english["average_marks"], 220 / 3)
        self.assertEqual(english["highest_mark"], 100)
        self.assertEqual(english["lowest_mark"], 40)

        summary = calculate_overall_summary(metrics, SUBJECT_COLUMNS)
        self.assertEqual(summary["student_count"], 3)
        self.assertAlmostEqual(summary["class_average"], (75 + 40 + 84.75) / 3)
        self.assertEqual(summary["pass_count"], 2)
        self.assertEqual(summary["fail_count"], 1)
        self.assertAlmostEqual(summary["pass_percentage"], 200 / 3)
        self.assertAlmostEqual(summary["average_attendance"], 80)

    def test_validation_rejects_duplicate_student_ids(self):
        data = make_test_data()
        data.loc[1, "student_id"] = data.loc[0, "student_id"]
        with self.assertRaisesRegex(ValueError, "unique"):
            validate_student_data(data)

    def test_validation_rejects_invalid_marks(self):
        data = make_test_data()
        data.loc[0, "mathematics"] = 101
        with self.assertRaisesRegex(ValueError, "between 0 and 100"):
            validate_student_data(data)


if __name__ == "__main__":
    unittest.main()