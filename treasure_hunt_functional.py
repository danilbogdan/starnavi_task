from typing import Tuple, List



def get_item(clue: Tuple[int, int], map_arr: List[List[Tuple[int, int]]]) -> Tuple[int, int]:
    row, col = clue
    return map_arr[row - 1][col - 1]


def get_map_size(map_arr: List[List[Tuple[int, int]]]) -> int:
    return len(map_arr) * len(map_arr[0])


def find_treasure(map_arr: List[List[Tuple[int, int]]]) -> List[Tuple[int, int],]:
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

