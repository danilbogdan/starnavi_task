import unittest
from utils import parse_input, parse_input_file
from tests import parser_testdata



class TestInputStringParser(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [parser_testdata.TEST_DATA_STRING_1, parser_testdata.TEST_DATA_STRING_2]
        self.bad_data = parser_testdata.TEST_DATA_STRING_BAD

    def test_parse_input(self):
        for idata in self.test_data:
            with self.subTest(idata=idata):
                parsed_data = parse_input(idata.input)
                self.assertEqual(idata.output, parsed_data)


class TestInputFileParser(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = [parser_testdata.TEST_DATA_FILE_1, parser_testdata.TEST_DATA_FILE_2]

    def test_parse_input(self):
        for idata in self.test_data:
            with self.subTest(idata=idata):
                with open(idata.input) as f:
                    parsed_data = parse_input_file(f)
                    self.assertEqual(idata.output, parsed_data)