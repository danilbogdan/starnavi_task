import argparse
from utils import parse_input, parse_input_file
from treasure_hunt_functional import find_treasure



def start(fp=None, input_data=None, recursive=False):
    if fp:
        with open(fp) as f:
            data = parse_input_file(f)
    elif input_data:
        data = parse_input(input_data)
    else:
        raise Exception('No input.')
    if recursive:
        method = find_treasure
    else:
        # TODO: Implement OOP
        method = None
    print(method(data))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Treasure hunter app')
    parser.add_argument('-f', '--file', help='read input from file', default=None)
    parser.add_argument('-i', '--input', help='Input data string', default=None)
    parser.add_argument('-r', '--recursive', help='Weather to apply recursive implementation or not', default=None)
    args = parser.parse_args()
    start(args.file, args.input, args.recursive)
