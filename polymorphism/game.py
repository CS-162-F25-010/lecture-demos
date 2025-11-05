from player import Player
from zombie import Zombie
from vampire import Vampire
from goblin import Goblin
from monster import Monster

# This function is the main "game loop". In other words, it contains
# the loop that runs the monsters' turns over and over again until the
# game ends (i.e., until the player loses)
def game_loop(
        p: Player,
        monsters: list[Monster]) -> None:
    # Until the player loses, keep running turns of the game
    turn_counter = 1 # Keeps track of what turn it is
    while p.get_hp() > 0:
        # The zombies attack the player
        for m in monsters:
            m.attack(p)

        # Print the player's remaining HP
        print(f"After turn {turn_counter}, the player's remaining "
            f"HP is {p.get_hp()}")
        
        # Update the turn counter
        turn_counter += 1


# What the heck is polymorphism?
# Polymorphism stands for "many forms".
# It means that you can have a function that has a parameter of a certain type,
#   but at runtime, when that function is called, the actual argument
#   supplied might be one of MANY types.

# A looser definition is this: Polymorphism  means a single variable
# can take on one of many types

def main() -> None:
    # Upcasting is a sort of type casting. Specifically, it refers to
    # the case where you type-cast a derived-class object to one of its
    # ancestor types.

    # Create the player object
    p = Player()

    # Suppose we want the game to have 3 zombies, 4 vampires, and 5
    # goblins. Let's create a list for each (we should use list
    # comprehensions in practice, but they're beyond the scope of
    # this course):
    monsters: list[Monster] = []
    for _ in range(3):
        monsters.append(Zombie())

    for _ in range(4):
        monsters.append(Vampire())

    for _ in range(5):
        monsters.append(Goblin())

    # Now run the game loop, executing turns until the game is over
    game_loop(p, monsters)
    

if __name__ == '__main__':
    main()

