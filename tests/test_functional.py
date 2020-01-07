from treasure_hunt_functional import get_item, find_treasure
import unittest

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

    def test_find_treasure(self):
        test_arr = [
            [(5, 5), (1, 4), (2, 5), (5, 2), (2, 1)],
            [(4, 4), (3, 1), (1, 1), (5, 3), (4, 3)],
            [(2, 4), (1, 3), (4, 5), (1, 2), (3, 4)],
            [(4, 2), (2, 2), (4, 3), (3, 2), (4, 1)],
            [(5, 1), (2, 3), (3, 3), (5, 4), (1, 5)],
        ]
        expected_result = [(1,1), (5,5), (1,5), (2,1), (4,4), (3,2), (1,3), (2,5), (4,3)]
        self.assertEqual(expected_result, find_treasure(test_arr))
