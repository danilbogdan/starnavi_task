from typing import Tuple, List
from exceptions import ItemNotFound, ValidationError


def get_item(clue: Tuple[int, int], map_arr: List[List[Tuple[int, int]]]) -> Tuple[int, int]:
    row, col = clue
    try:
        return map_arr[row - 1][col - 1]
    except IndexError:
        raise ItemNotFound(f'({row}, {col})')


def get_map_size(map_arr: List[List[Tuple[int, int]]]) -> int:
    return len(map_arr) * len(map_arr[0])

def validate_map(map_arr: List[List[Tuple[int, int]]]) -> None:
    rows_count = len(map_arr)
    for row in map_arr:
        if len(row) != rows_count:
            raise ValidationError('Treasure map must be square')

def find_treasure(map_arr: List[List[Tuple[int, int]]]) -> List[Tuple[int, int],]:
    validate_map(map_arr)
    clues = [(1,1)]

    def get_last_clue(): return clues[-1]

    def find(map_arr):
        if len(clues) > get_map_size(map_arr):
            raise RecursionError('Map size exceeded. No treasure found.')
        clue = get_last_clue()
        item = get_item(clue, map_arr)
        if item == clue:
            return clues
        clues.append(item)
        return find(map_arr)
    return find(map_arr)

