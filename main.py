import argparse

from tabulate import tabulate

from src.parser.parser_file_csv import ParserCSV
from src.reports.report import Report

if __name__ == "__main__":

    def main():
        parser = argparse.ArgumentParser(
            description="Формирование отчёта анализа успеваемости студентов."
        )
        parser.add_argument(
            "--files", nargs="+", help="Список названий файлов", required=True
        )
        parser.add_argument("--report", help="Название отчёта", required=True)

        args = parser.parse_args()
        try:
            parser_file_csv = ParserCSV(path_to_files=args.files)
            report = Report(parser_file_csv.students)
            report.__getattribute__(
                args.report
            )()  # Находим и вызываем метод по флагу --report для выполнения отчёта
        except AttributeError as e:
            raise AttributeError(
                f"отчёт с названием {e.name} не найден. "
                f"Попробуйте использовать '_' между словами"
            )

        table_data = report.table_data
        headers = report.headers

        # Вывод таблицы в терминал
        print(
            tabulate(
                table_data,
                headers=headers,
                tablefmt="outline",
            )
        )

    main()
