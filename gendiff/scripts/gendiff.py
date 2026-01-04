import argparse

def main():
    # Создаем парсер аргументов
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        add_help=False # Отключаем стандартный help, чтобы настроить флаг -h вручную
    )

    
    # Позиционные аргументы
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    
    # Добавляем флаг помощи именно как -h (согласно вашему требованию)
    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')
    
    # Можно добавить версию (опционально)
    # parser.add_argument('-V', '--version', action='version', version='%(prog)s 1.0.0')

    # Парсим аргументы
    args = parser.parse_args()

if __name__ == '__main__':
    main()
