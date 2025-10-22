class Circle:
    _diameter: float # Every circle's radius should always be positive
    
    # This is a class invariant. Every circle ever created will always,
    # guaranteed, have a positive radius.
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('Error. Non-positive radius provided.')
        else:
            self._diameter = radius * 2

    # Setters are methods where you give them a value, and they store that
    # value in a private attribute within the object
    def set_radius(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('Error. Non-positive radius provided.')
        else:
            self._diameter = radius * 2

    # Getters are methods that simply return a copy of the value of a private
    # attribute within the object
    def get_radius(self) -> float:
        return self._diameter / 2

# Getters and setters should often be avoided. They often break encapsuluation.
def main() -> None:
    try:
        c = Circle(-1)
    except ValueError as e:
        print(e)

    c = Circle(5.4)
    c.set_radius(12.5)

    print(c.get_radius())
    


if __name__ == '__main__':
    main()
