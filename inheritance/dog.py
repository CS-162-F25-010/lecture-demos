class Dog:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def bark(self) -> None:
        print(f'Bark! My name is {self._name}')
