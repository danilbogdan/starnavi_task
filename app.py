import argparse
from treasure_hunt_functional import find_treasure, serialize_treasure_clues, parse_input
from treasure_hunt_oop import TreasureMapResolver



def start(fp=None, recursive=False):

    if fp:
        with open(fp) as f:
            data = f.read()
    else:
        print('Put treasure map by row:')
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        data = '\n'.join(lines)

    if recursive:
        result = serialize_treasure_clues(find_treasure(parse_input(data)))
    else:
        result = TreasureMapResolver(data).find_treasure()

    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Treasure hunter app')
    parser.add_argument('-f', '--file', help='read input from file', default=None)
    parser.add_argument('-r', '--recursive', help='Weather to apply recursive implementation or not', action='store_true')
    args = parser.parse_args()
    start(args.file, args.recursive)
