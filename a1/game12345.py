"""
Game class material
"""
from typing import Any
from state import State


class Game:
    """
    the parent of all games
    """
    current_state: State

    def __init__(self, turn: bool) -> None:
        """
        create a new game
       """
        if turn:
            self.current_state = None
        else:
            self.current_state = None
        raise NotImplementedError("Subclass this!")

    def __str__(self) -> str:
        """
        return the representation of this game
        """
        raise NotImplementedError("Subclass this!")

    def __eq__(self, other: Any) -> bool:
        """
        return whether the two game is equal to each other
        """
        return type(self) == type(other) and \
            self.current_state == other.current_state

    def get_instructions(self) -> str:
        """represent the instruction to play this game to the players
        """
        raise NotImplementedError("Subclass this!")

    def is_over(self, current_state: State) -> bool:
        """return whether the game is over with the current state
        """
        raise NotImplementedError("Subclass this!")

    def str_to_move(self, move: Any) -> int:
        """convert any syntactically correct move into a movement
        """
        raise NotImplementedError("Subclass this!")

    def is_winner(self, suppose: str) -> bool:
        """
        distinguish whether the people we supposed is the winner
        """
        raise NotImplementedError("Subclass this!")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
