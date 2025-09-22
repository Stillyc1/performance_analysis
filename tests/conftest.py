import pytest


@pytest.fixture
def read_data_for_parser_csv():
    return (
        "student_name,subject,teacher_name,date,grade"
        "\nСеменова Елена,Английский язык,Ковалева Анна,2023-10-10,5"
        "\nТитов Владислав,География,Орлов Сергей,2023-10-12,4"
    )
