import argparse
from utils import parse_input, parse_input_file, serialize_treasure_clues
from treasure_hunt_functional import find_treasure
from treasure_hunt_oop import TreasureMap



def start(fp=None, recursive=False):

    if fp:
        with open(fp) as f:
            data = parse_input_file(f)
    else:
        print('Put treasure map by row:')
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        data = parse_input('\n'.join(lines))

    method = find_treasure if recursive else TreasureMap(data).find_treasure

    print(serialize_treasure_clues(method(data)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Treasure hunter app')
    parser.add_argument('-f', '--file', help='read input from file', default=None)
    parser.add_argument('-r', '--recursive', help='Weather to apply recursive implementation or not', action='store_true')
    args = parser.parse_args()
    start(args.file, args.recursive)
