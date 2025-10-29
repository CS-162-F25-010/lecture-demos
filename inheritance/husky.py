from dog import Dog
from sled import Sled

# In this case, Husky is
# - A child class
# - A derived class
# - A subclass

# In this case, Dog is
# - A parent class
# - A base class
# - A superclass

# This technique is known as inheritance

# Inheritance sort of establishes "is-a" relationships.
class Husky(Dog):
    # Any and all attributes and methods that are declared / defined in the
    # Dog class are all implicitly and automatically declared and defined
    # in the Husky class. Attributes and methods are inherited from the
    # base / parent / superclass into the derived / child / subclass.

    # I can define attributes / methods of the Husky class here

    # Usually, you'd want to add more stuff to the child class. This is
    # referred to as Extension.

    # Any attributes / methods that I put in the Husky class will NOT be present
    # in the Dog class. Inheritance is one-directional.
    _energy: int
    
    def __init__(self, name: str) -> None:
        # I want the Husky constructor to call the Dog constructor.
        # Here's how you do this
        super().__init__(name)
        self._energy = 100


    def pull_sled(self, sled: Sled) -> None:
        if self._energy > 50:
            sled.distance_traveled += 10
            self._energy -= 10
        elif self._energy > 20:
            sled.distance_traveled += 5
            self._energy -= 10
