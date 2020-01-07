import unittest
from utils import parse_input, parse_input_file
from tests import testdata



class TestInputStringParser(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [testdata.TEST_DATA_STRING_1, testdata.TEST_DATA_STRING_2]

    def test_parse_input(self):
        for idata in self.test_data:
            with self.subTest(idata=idata):
                parsed_data = parse_input(idata.input)
                self.assertEqual(parsed_data, idata.output)


class TestInputFileParser(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [testdata.TEST_DATA_FILE_1, testdata.TEST_DATA_FILE_2]

    def test_parse_input(self):
        for idata in self.test_data:
            with self.subTest(idata=idata):
                with open(idata.input) as f:
                    parsed_data = parse_input_file(f)
                    self.assertEqual(parsed_data, idata.output)