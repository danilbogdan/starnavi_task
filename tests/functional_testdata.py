from collections import namedtuple

Testdata = namedtuple('Testdata', 'input output')

test_string_1 = '''
34 21 32 41 25

14 42 43 14 31

54 45 52 42 23

33 15 51 31 35

21 52 33 13 23
'''

test_string_2 = '''
55 14 25 52 21

44 31 11 53 43

24 13 45 12 34

42 22 43 32 41

51 23 33 54 15
'''


test_file_1 = "inputdata.txt"
test_file_2 = "inputdata_2.txt"





TEST_DATA_STRING_1 = Testdata(input=test_string_1, output=parsed_map_1)
TEST_DATA_STRING_2 = Testdata(input=test_string_2, output=parsed_map_2)

TEST_DATA_FILE_1 = Testdata(input=test_file_1, output=parsed_map_1)
TEST_DATA_FILE_2 = Testdata(input=test_file_2, output=parsed_map_2)