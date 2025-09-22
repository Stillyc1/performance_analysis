import unittest
from collections import defaultdict

from src.reports.report import Report


class TestReport(unittest.TestCase):
    def setUp(self):
        students = self.students()
        self.report = Report(students)

    def test_students_performance(self):
        self.report.students_performance()
        expected_table_data = self.expected_table_data()
        print(self.report.table_data)
        print(expected_table_data)
        self.assertListEqual(self.report.table_data, expected_table_data)
        self.assertListEqual(self.report.headers, ["#", "student_name", "grade"])

    def test_calculate_average_grades(self):
        students_grades = defaultdict(list)
        students_grades["Семенова Елена"].extend([5, 4])
        students_grades["Титов Владислав"].append(4)
        students_grades["Власова Алина"].append(5)
        average_grades = Report.calculate_average_grades(students_grades)
        expected_averages = self.expected_averages()
        self.assertEqual(average_grades, expected_averages)

    @staticmethod
    def students():
        return [
            {"student_name": "Семенова Елена", "grade": 5},
            {"student_name": "Титов Владислав", "grade": 4},
            {"student_name": "Власова Алина", "grade": 5},
            {"student_name": "Семенова Елена", "grade": 4},
        ]

    @staticmethod
    def expected_table_data():
        return [
            (1, "Власова Алина", 5.0),
            (2, "Семенова Елена", 4.5),
            (3, "Титов Владислав", 4.0),
        ]

    @staticmethod
    def expected_averages():
        return {
            "Семенова Елена": 4.5,
            "Титов Владислав": 4.0,
            "Власова Алина": 5.0,
        }
