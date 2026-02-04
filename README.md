### Hexlet tests and linter status:
[![Actions Status](https://github.com/OlegRakhilov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OlegRakhilov/python-project-50/actions)


[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=OlegRakhilov_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=OlegRakhilov_python-project-50)

[![asciicast](https://asciinema.org/a/Z9bqrEhi5FVOjtMa4WVp6e8Mx.svg)](https://asciinema.org/a/Z9bqrEhi5FVOjtMa4WVp6e8Mx)

## Возможности (Features)

- **Поддержка форматов:** Работает с файлами конфигураций в форматах **JSON**, **YAML** и **YML**.
- **Различные форматы вывода:**
  - `stylish` — наглядное дерево изменений (по умолчанию).
  - `plain` — плоский текстовый отчет о значимых изменениях.
  - `json` — машиночитаемый формат для интеграции с другими инструментами.
- **Рекурсивное сравнение:** Корректно обрабатывает вложенные структуры любой глубины.
- **Надежность:** Код покрыт тестами на **92%** (основная логика — **100%**).
- **Чистота кода:** Соответствует стандартам **PEP 8**, проходит проверку линтером **Ruff**.
- **Современный стек:** Используется менеджер пакетов **UV** для быстрой установки и управления зависимостями.

### Тестирование и покрытие
Для запуска тестов и генерации отчета о покрытии выполните:
```bash
make test