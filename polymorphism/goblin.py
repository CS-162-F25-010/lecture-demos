from typing_extensions import override

import random

from player import Player
from monster import Monster

# The Goblin class inherits from the Monster class
class Goblin(Monster):
    def __init__(self) -> None:
        # Goblins get 5 HP. Pass this to the Monster constructor
        # to be stored in the private _hp attribute
        super().__init__(5)

    @override
    def attack(self, p: Player) -> None:
        p.take_damage(random.randint(1, 2))
