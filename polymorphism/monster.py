from abc import ABC, abstractmethod
# ABC stands for abstract base class

from player import Player

# Now, the Monster class is abstract.
class Monster(ABC):
    _hp: int

    def __init__(self, hp: int) -> None:
        # Different monsters will start out with different amounts
        # of hp, so we pass the monster's starting HP as an argument
        # to this constructor's hp parameter. It then stores it in
        # the self._hp attribute.
        self._hp = hp

    # Abstract classes are allowed to have abstract methods.
    @abstractmethod
    def attack(self, p: Player) -> None:
        # This makes the attack() method an abstract method.
        # An abstract method is a method that is not fully defined within
        # the base class, but instead is going to be defined by overrides
        # in the derived classes.
        pass
