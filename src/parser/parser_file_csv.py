import csv
import os

from src.parser.base_parser import BaseParser


class ParserCSV(BaseParser):
    """
    Формируем список о каждой оценке студента.
    Парсим каждый файл и записываем в атрибут students.
    """

    def __init__(self, path_to_files: list[str]):
        self.students: list[dict[str, str]] = list()
        self.__reader(path_to_files)

    def __reader(self, path_to_files: list[str]) -> None:
        """Читает данные из переданных файлов и заполняет список студентов."""
        for file in path_to_files:
            path = os.path.join("students", file)
            try:
                with open(path, encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for student in reader:
                        self.students.append(student)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Файл {e.filename} не найден!")
            except Exception as e:
                raise Exception(f"Ошибка при чтении файла '{path}': {e}")
