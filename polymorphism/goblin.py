from monster import Monster

# The Goblin class inherits from the Monster class
class Goblin(Monster):
    def __init__(self) -> None:
        # Goblins get 5 HP. Pass this to the Monster constructor
        # to be stored in the private _hp attribute
        super().__init__(5)

    # The Goblin class does not override the attack() method, so when
    # goblins attack the player, they simply execute the Monster
    # class's attack() method (which the Goblin class inherits)
