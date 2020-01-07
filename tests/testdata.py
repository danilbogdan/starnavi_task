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

test_file_1 = "inputdata_1.txt"
test_file_2 = "inputdata_2.txt"

parsed_map_1 = (
    ((3,4), (2,1), (3,2), (4,1), (2,5)),
    ((1,4), (4,2), (4,3), (1,4), (3,1)),
    ((5,4), (4,5), (5,2), (4,2), (2,3)),
    ((3,3), (1,5), (5,1), (3,1), (3,5)),
    ((2,1), (5,2), (3,3), (1,3), (2,3)),
)

parsed_map_2 = (
    ((5,5), (1,4), (2,5), (5,2), (2,1)),
    ((4,4), (3,1), (1,1), (5,3), (4,3)),
    ((2,4), (1,3), (4,5), (1,2), (3,4)),
    ((4,2), (2,2), (4,3), (3,2), (4,1)),
    ((5,1), (2,3), (3,3), (5,4), (1,5)),
)


TEST_DATA_STRING_1 = Testdata(input=test_string_1, output=parsed_map_1)
TEST_DATA_STRING_2 = Testdata(input=test_string_2, output=parsed_map_2)
TEST_DATA_FILE_1 = Testdata(input=test_file_1, output=parsed_map_1)
TEST_DATA_FILE_2 = Testdata(input=test_file_2, output=parsed_map_2)