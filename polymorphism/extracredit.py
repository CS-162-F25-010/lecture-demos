from abc import ABC, abstractmethod
from typing_extensions import override

class Shape(ABC):
    # TODO Create an abstract area() method that returns the shape's area as
    # a float. Put @abstractmethod just above the method
    # definition, then put `pass` in its definition.
    
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    _side_length: float

    def __init__(self, side_length: float) -> None:
        self._side_length = side_length

    # TODO Override the area() method, returning self._side_length squared
    def area(self) -> float:
        return self._side_length ** 2.0


class Triangle(Shape):
    _base: float
    _height: float

    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    # TODO Override the area() method, returning 1/2 * _base * _height
    def area(self) -> float:
        return 1 / 2 * self._base * self._height

def main() -> None:
    shapes: list[Shape] = []
    shapes.append(Square(20))
    shapes.append(Triangle(20, 41))

    print(f'Area of first shape: {shapes[0].area()}') # area should be 400
    print(f'Area of second shape: {shapes[1].area()}') # area should be 410

if __name__ == '__main__':
    main()
