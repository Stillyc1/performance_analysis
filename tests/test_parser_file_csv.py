from unittest.mock import mock_open, patch

from src.parser.parser_file_csv import ParserCSV


def test_reader(read_data_for_parser_csv):
    with patch(
        "builtins.open", new_callable=mock_open, read_data=read_data_for_parser_csv
    ):
        parser = ParserCSV(path_to_files=["students1.csv"])

        assert len(parser.students) == 2
        assert parser.students[0]["student_name"] == "Семенова Елена"
        assert parser.students[1]["student_name"] == "Титов Владислав"
