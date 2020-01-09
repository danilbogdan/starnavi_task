from treasure_hunt_oop import Map, Row, Clue, Array, TreasureMapResolver
import unittest
from exceptions import ValidationError, ItemNotFound


class TestArray(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = '5514255221'

    def test_getitem(self):
        self.assertEqual(5, Array(self.test_data)[0])
        self.assertEqual(1, Array(self.test_data)[-1])

    def test_to_string(self):
        input_data = Array(self.test_data)
        self.assertEqual(self.test_data, str(input_data))

    def test_length(self):
        input_data = Array(self.test_data)
        self.assertEqual(10, len(input_data))

    def test_equity(self):
        input_data_1 = Array(self.test_data)
        input_data_2 = Array(self.test_data)
        self.assertEqual(input_data_1, input_data_2)

    def test_invalid_input(self):
        input_data = '1234ad1234'
        self.assertRaises(ValidationError, Array, input_data)


class TestClue(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = '53'

    def test_getitem(self):
        self.assertEqual(5, Clue(self.test_data)[0])
        self.assertEqual(3, Clue(self.test_data)[1])
        self.assertEqual(3, Clue(self.test_data)[-1])

    def test_to_string(self):
        input_data = Clue(self.test_data)
        self.assertEqual(self.test_data, str(input_data))

    def test_length(self):
        input_data = Clue(self.test_data)
        self.assertEqual(2, len(input_data))

    def test_equity(self):
        input_data_1 = Clue(self.test_data)
        input_data_2 = Clue(self.test_data)
        self.assertEqual(input_data_1, input_data_2)

    def test_invalid_input(self):
        input_data = ['55a', '55 ', '555']
        for data in input_data:
            with self.subTest(data=data):
                self.assertRaises(ValidationError, Clue, data)


class TestRow(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = '55 14 25 52 21'

    def test_getitem(self):
        self.assertEqual(Clue('55'), Row(self.test_data)[0])
        self.assertEqual(Clue('25'), Row(self.test_data)[2])
        self.assertEqual(Clue('21'), Row(self.test_data)[-1])

    def test_to_string(self):
        input_data = Row(self.test_data)
        self.assertEqual(self.test_data, str(input_data))

    def test_length(self):
        input_data = Row(self.test_data)
        self.assertEqual(5, len(input_data))

    def test_equity(self):
        input_data_1 = Row(self.test_data)
        input_data_2 = Row(self.test_data)
        self.assertEqual(input_data_1, input_data_2)

    def test_invalid_input(self):
        input_data = ['55 14 25 52  21', '55 14 25 52', '55 14 25 52 aa']
        for data in input_data:
            with self.subTest(data=data):
                self.assertRaises(ValidationError, Row, data)


class TestMap(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 15
'''

    def test_getitem(self):
        self.assertEqual(Clue('55'), Map(self.test_data)[Clue('11')])
        self.assertEqual(Clue('15'), Map(self.test_data)[Clue('55')])
        self.assertEqual(Clue('31'), Map(self.test_data)[Clue('22')])

    def test_to_string(self):
        input_data = Map(self.test_data)
        self.assertEqual(self.test_data, str(input_data))

    def test_length(self):
        input_data = Map(self.test_data)
        self.assertEqual(25, len(input_data))

    def test_equity(self):
        input_data_1 = Map(self.test_data)
        input_data_2 = Map(self.test_data)
        self.assertEqual(input_data_1, input_data_2)

    def test_invalid_input(self):
        input_data = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 15

51 23 33 54 15
'''
        self.assertRaises(ValidationError, Map, input_data)


class TestTreasureMapResolver(unittest.TestCase):

    def test_find_treasure_1(self):
        input_data = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 15
'''
        treasure_clues = TreasureMapResolver(input_data).find_treasure()
        self.assertEqual("11 55 15 21 44 32 13 25 43", treasure_clues)

    def test_find_treasure_2(self):
        input_data = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 55
'''
        treasure_clues = TreasureMapResolver(input_data).find_treasure()
        self.assertEqual("11 55", treasure_clues)

    def test_find_treasure_3(self):
        input_data = '''
55 14 25 52 21

44 22 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 22
'''
        treasure_clues = TreasureMapResolver(input_data).find_treasure()
        self.assertEqual("11 55 22", treasure_clues)

    def test_find_treasure_validation_error(self):
        input_data = '''
55 14 25 52 21

44 22 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 22

51 23 33 54 22
'''
        self.assertRaises(ValidationError, TreasureMapResolver, input_data)
