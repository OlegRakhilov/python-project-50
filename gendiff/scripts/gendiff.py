import argparse
import json
import os

def parse_file(file_path):
    absolute_path = os.path.abspath(file_path)

    with open(absolute_path, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    
    
    parser.add_argument(
        '-f', '--format', 
        metavar='FORMAT', 
        help='set format of output'
    )

    args = parser.parse_args()

    try:
        data1 = parse_file(args.first_file)
        data2 = parse_file(args.second_file)

        print(f"Data from file 1: {data1}")
        print(f"Data from file 2: {data2}")

    except Exception as e:
        print(f"Error reading files: {e}")

if __name__ == '__main__':
    main()
