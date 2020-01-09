from treasure_hunt_functional import get_item, find_treasure, parse_input, serialize_treasure_clues
from exceptions import ValidationError, ItemNotFound
import os
import unittest


class TestParser(unittest.TestCase):

    def setUp(self) -> None:
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

    def test_parse_input_string(self):
        input_data = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 15
'''
        expected_result = [
            [(5, 5), (1, 4), (2, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 3), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        parsed_data = parse_input(input_data)
        self.assertEqual(expected_result, parsed_data)

    def test_parse_input_file(self):
        input_file = os.path.join(self.current_dir, "inputdata.txt")
        expected_result = [
            [(5, 5), (1, 4), (2, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 3), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        with open(input_file) as f:
            parsed_data = parse_input(f.read())
            self.assertEqual(expected_result, parsed_data)

    def test_serialize_treasure_clues(self):
        clues = [(1, 1), (5, 5), (1, 5), (2, 1), (4, 4), (3, 2), (1, 3), (2, 5), (4, 3)]
        expected_result = "11 55 15 21 44 32 13 25 43"
        self.assertEqual(expected_result, serialize_treasure_clues(clues))


class TestFunctionalTreasureHunt(unittest.TestCase):

    def test_get_item(self):
        test_arr = [
            [(1, 2), (2, 1), (3, 1)],
            [(3, 1), (3, 2), (2, 3)],
            [(3, 1), (2, 3), (1, 3)]
        ]
        test_clue = (1, 2)
        expected_result = (2, 1)
        self.assertEqual(expected_result, get_item(test_clue, test_arr))

    def test_find_treasure_success(self):
        test_arr = [
            [(5, 5), (1, 4), (2, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 3), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        expected_result = [(1, 1), (5, 5), (1, 5), (2, 1), (4, 4), (3, 2), (1, 3), (2, 5), (4, 3)]
        self.assertEqual(expected_result, find_treasure(test_arr))

    def test_find_treasure_fails(self):
        test_arr = [
            [(5, 5), (1, 4), (2, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 4), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        self.assertRaises(RecursionError, find_treasure, test_arr)

    def test_find_treasure_item_not_found_error(self):
        test_arr = [
            [(5, 5), (1, 4), (6, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (5, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 4), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        self.assertRaises(ItemNotFound, find_treasure, test_arr)

    def test_find_treasure_validation_error(self):
        test_arr = [
            [(5, 5), (1, 4), (2, 5), (5, 2)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 4), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        self.assertRaises(ValidationError, find_treasure, test_arr)
