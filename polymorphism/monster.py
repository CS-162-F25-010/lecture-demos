from player import Player

class Monster:
    _hp: int

    def __init__(self, hp: int) -> None:
        # Different monsters will start out with different amounts
        # of hp, so we pass the monster's starting HP as an argument
        # to this constructor's hp parameter. It then stores it in
        # the self._hp attribute.
        self._hp = hp

    # Attacks the player
    def attack(self, p: Player) -> None:
        # Reduce the player's HP by 1
        p.take_damage(1)
