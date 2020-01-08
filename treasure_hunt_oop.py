class TreasureMap:

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._validate_data(data)
        self._data = data

    def _validate_data(self, data):
        pass

    def find_treasure(self):
        pass