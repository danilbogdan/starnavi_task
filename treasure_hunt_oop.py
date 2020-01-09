from abc import abstractmethod, ABC
from typing import Sequence, Any, Union

from exceptions import ValidationError


class TreasureMapComponent(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __getitem__(self, item: Any):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __eq__(self, other: 'TreasureMapComponent'):
        pass


class Array(TreasureMapComponent):
    element_class = int

    def __init__(self, component_str: str):
        self._raw = component_str
        self.sequence = self._fromstring(component_str)

    def __repr__(self):
        return str(self.sequence)

    def __str__(self):
        return self._raw

    def __getitem__(self, item: Any):
        return self.sequence[item]

    def __len__(self):
        return len(self.sequence)

    def __eq__(self, other: 'Array'):
        return self.sequence == other.sequence

    @classmethod
    def _split_string(cls, component_str: str):
        return component_str

    def _fromstring(cls, component_str: str) -> 'Sequence':
        try:
            return [cls.element_class(sub_str) for sub_str in cls._split_string(component_str)]
        except (ValueError, ValidationError) as e:
            raise ValidationError(str(e))

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, seq: Sequence):
        self._validate_sequence(seq)
        self._sequence = seq

    def _validate_sequence(self, seq: Sequence):
        pass


class Clue(Array):

    def __repr__(self):
        return f"Clue({str(self.sequence)})"

    def _validate_sequence(self, seq: Sequence):
        if len(seq) != 2:
            raise ValidationError('Clue size must be 2')


class Row(Array):
    element_class = Clue

    @classmethod
    def _split_string(cls, component_str: str):
        return component_str.split(' ')

    def _validate_sequence(self, seq: Sequence):
        if len(seq) != 5:
            raise ValidationError('Row size must be 5')


class Map(Array):
    element_class = Row

    def __getitem__(self, item: Clue):
        return self.sequence[item[0] - 1][item[1] - 1]

    def __len__(self):
        return len(self.sequence) * len(self.sequence[0])

    @classmethod
    def _split_string(cls, component_str: str):
        return filter(lambda x: x != '', component_str.splitlines())

    def _validate_sequence(self, seq: Sequence):
        if len(seq) != 5:
            raise ValidationError('Map size must be 5 x 5')


class TreasureMapResolver:

    def __init__(self, raw_data: str):
        self.map = Map(raw_data)
        self.clues = None

    @property
    def clues(self):
        return self._clues

    @clues.setter
    def clues(self, val: Union[Sequence, None]):
        if val is None:
            val = [Clue('11')]
        self._clues = val

    @property
    def _last_clue(self):
        return self.clues[-1]

    def find_treasure(self):
        while len(self.clues) <= len(self.map):
            item = self.map[self._last_clue]
            if item == self._last_clue:
                return ' '.join(str(c) for c in self.clues)
            self.clues.append(item)
        return None