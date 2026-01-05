import json

def generate_diff(file_path1, file_path2):
    # Чтение и парсинг данных (сравниваем данные, а не строки)
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    # Сбор всех уникальных ключей и их сортировка
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data1:
            diff.append(f"  + {key}: {val2}")
        elif key not in data2:
            diff.append(f"  - {key}: {val1}")
        elif val1 == val2:
            diff.append(f"    {key}: {val1}")
        else:
            # Если значения разные: сначала минус (старое), потом плюс (новое)
            diff.append(f"  - {key}: {val1}")
            diff.append(f"  + {key}: {val2}")

    return "{\n" + "\n".join(diff) + "\n}"
