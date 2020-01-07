from typing import Tuple, List



def get_item(clue: Tuple[int, int], map_arr: List[List[Tuple[int, int]]]) -> Tuple[int, int]:
    row, col = clue
    return map_arr[row - 1][col - 1]


def find_treasure(map_arr: List[List[Tuple[int, int]]]) -> List[Tuple[int, int],]:
    clues = [(1,1)]
    def find(map_arr):
        clue = clues[-1]
        item = get_item(clue, map_arr)
        if item == clue:
            return clues
        clues.append(item)
        return find(map_arr)
    return find(map_arr)

