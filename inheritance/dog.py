from pet import Pet

class Dog(Pet):
    _name: str

    def __init__(self, owners_name: str, name: str) -> None:
        super().__init__(owners_name)
        self._name = name

    def vocalize(self) -> None:
        print(f'Bark! Bark!')

    def print(self) -> None:
        super().print()
        print(f'Name: {self._name}')
