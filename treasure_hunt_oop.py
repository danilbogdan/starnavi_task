from abc import abstractmethod, ABC
from typing import List

from exceptions import ValidationError


class TreasureMapComponent(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    @classmethod
    @abstractmethod
    def _split_string(cls, component_str):
        pass

    @classmethod
    @abstractmethod
    def fromstring(cls, *args, **kwargs):
        pass


class Array(TreasureMapComponent):
    element_class = None

    def __init__(self, seq: List):
        self.sequence = seq

    def __repr__(self):
        return str(self.sequence)

    def __str__(self):
        return ' '.join([str(comp) for comp in self.sequence])

    def __getitem__(self, item):
        return self.sequence[item]

    def __len__(self):
        return len(self.sequence)

    @classmethod
    def _split_string(cls, component_str):
        return component_str.split(' ')

    @classmethod
    def fromstring(cls, component_str: str) -> 'Array':
        return cls([cls.element_class.fromstring(sub_str) for sub_str in cls._split_string(component_str)])


class Clue(Array):
    element_class = int

    def __repr__(self):
        return f"Clue({str(self.sequence)})"

    def __str__(self):
        return ''.join([str(comp) for comp in self.sequence])

    @classmethod
    def _split_string(cls, component_str):
        return [int(component_str[0]), int(component_str[1])]

    @classmethod
    def fromstring(cls, row_col_str: str) -> 'Clue':
        if len(row_col_str) != 2:
            raise ValidationError('Clue size must be 2')
        return cls(cls._split_string(row_col_str))



class Row(Array):
    element_class = Clue


class Map(Array):
    element_class = Row

    def __getitem__(self, item: Clue):
        return self.sequence[item[0] - 1][item[1] - 1]

    def __len__(self):
        return len(self.sequence) * len(self.sequence[0])

    @classmethod
    def _split_string(cls, component_str):
        return filter(lambda x: x != '', component_str.splitlines())


class TreasureMapResolver:

    def __init__(self, raw_data):
        self.map = Map.fromstring(raw_data)
        self.clues = [Clue([1, 1])]

    @property
    def last_clue(self):
        return self.clues[-1]

    def find_treasure(self):
        while len(self.clues) <= len(self.map):
            item = self.map[self.last_clue]
            if item == self.last_clue:
                return Array(self.clues)
            self.clues.append(item)
        return None


if __name__ == '__main__':

    with open('tests/inputdata.txt') as f:
        m = TreasureMapResolver(f.read()).find_treasure()
        pass