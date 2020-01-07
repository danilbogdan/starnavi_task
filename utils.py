from exceptions import ParseError
from typing import List, IO

def parse_input(input_string: str, delimiter: str = ' ') -> List:
    try:
        splitted_lines = filter(lambda x: x != '', input_string.splitlines())
        output_arr = []
        for line in splitted_lines:
            new_line = [(int(val[0]), int(val[1])) for val in line.split(delimiter)]
            output_arr.append(new_line)
        return output_arr
    except Exception as e:
        raise ParseError(f"Can't parse data: {str(e)}")


def parse_input_file(f: IO, delimiter: str = ' ') -> List:
    text = f.read()
    return parse_input(text, delimiter)