from collections import defaultdict

from src.reports.base_report import BaseReport


class Report(BaseReport):
    """
    Анализируем и сортируем данные для возможности формирования отчёта.
    """

    REPORT_NAMES: tuple[str] = (
        "students_performance",
    )

    def __init__(self, students):
        self.students: list[dict[str, str]] = students
        self.table_data: list[tuple] = list()
        self.headers: list[str] = list()

    def students_performance(self) -> None:
        """
        Собирает успеваемость студентов и сортирует их по средним оценкам.
        """
        students_grades = defaultdict(list)
        for student in self.students:
            student_name = student.get("student_name")
            try:
                grade = int(student.get("grade"))
                students_grades[student_name].append(grade)
            except (ValueError, TypeError):
                print(
                    f"Некорректная оценка для студента '{student_name}': {student.get('grade')}"
                )
        average_grades = self.calculate_average_grades(students_grades)
        sorted_students = sorted(
            average_grades.items(), key=lambda item: item[1], reverse=True
        )
        self.table_data = [
            (index + 1, student, grade)
            for index, (student, grade) in enumerate(sorted_students)
        ]
        self.headers = ["#", "student_name", "grade"]

    @staticmethod
    def calculate_average_grades(
        students_grades: defaultdict[str, list[int]],
    ) -> dict[str, float]:
        average_grades = {}
        for student, grades in students_grades.items():
            average_grades[student] = round(sum(grades) / len(grades), 1)
        return average_grades
