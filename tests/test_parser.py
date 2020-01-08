import os
import unittest

from utils import parse_input, parse_input_file


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
            parsed_data = parse_input_file(f)
            self.assertEqual(expected_result, parsed_data)
