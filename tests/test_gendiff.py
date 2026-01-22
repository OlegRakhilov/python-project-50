import json

from gendiff.scripts.gendiff import generate_diff


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

