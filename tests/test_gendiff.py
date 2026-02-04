import json
import pytest

from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import parse_data
from gendiff.format.stylish import stringify
from gendiff.format.plain import get_nested


def read_file(path):
    with open(path) as f:
        return f.read().strip()


def test_generate_diff_json():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    expected = read_file("tests/test_data/expected_stylish.txt")
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_yml():
    file1 = "tests/test_data/file1_test.yml"
    file2 = "tests/test_data/file2_test.yml"
    expected = read_file("tests/test_data/expected_stylish.txt")
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_plain_json():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    expected = read_file("tests/test_data/expected_plain.txt")
    result = generate_diff(file1, file2, 'plain')
    assert result == expected


def test_generate_diff_plain_yml():
    file1 = "tests/test_data/file1_test.yml"
    file2 = "tests/test_data/file2_test.yml"
    expected = read_file("tests/test_data/expected_plain.txt")
    result = generate_diff(file1, file2, 'plain')
    assert result == expected


def test_generate_diff_json_format():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    result = generate_diff(file1, file2, 'json')
    parsed_result = json.loads(result)

    # 1. Проверяем, что это словарь (как и выдает ваша программа)
    assert isinstance(parsed_result, dict)

    # 2. Проверяем наличие ключевых данных
    assert 'common' in parsed_result
    assert 'group1' in parsed_result

    # 3. Проверяем, что значения внутри тоже являются структурами (словарями)
    assert isinstance(parsed_result.get('common'), dict)


def test_parse_data_invalid_type():
    # Проверяем строку 32 (ValueError при неверном расширении)
    with pytest.raises(ValueError, match="Invalid file type"):
        parse_data("tests/test_data/expected_stylish.txt")


def test_parse_data_file_not_found():
    # Проверяем строки 37-39 (FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        parse_data("non_existent_file.json")


def test_stringify_primitive():
    # Проверяем работу с простым числом (не словарем)
    assert stringify(42) == '42'
    # Проверяем работу со строкой
    assert stringify('value') == 'value'


def test_generate_diff_invalid_formatter():
    file1 = "tests/test_data/file1_test.json"
    file2 = "tests/test_data/file2_test.json"
    # Проверяем, что выбрасывается ValueError при передаче 'unknown'
    with pytest.raises(ValueError, match="Invalid formatter: unknown"):
        generate_diff(file1, file2, 'unknown')


def test_get_nested_none():
    # Пытаемся получить ключ из чего-то, что не является словарем
    data = {"key": "value"}
    # Путь ['key', 'sub-key'] заставит функцию зайти в else (стр. 16),
    # так как по ключу 'key' лежит строка, а не словарь.
    assert get_nested(data, ["key", "sub-key"]) is None