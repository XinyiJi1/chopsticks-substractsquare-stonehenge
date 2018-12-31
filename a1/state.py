"""
State class material
"""
from typing import Any


class State:
    """
    the current state of the game subtractsquare
    """
    player: str

    def __init__(self, player: str) -> None:
        """create the state of a game
        """
        self.player = player
        raise NotImplementedError("Subclass this!")

    def __str__(self) -> str:
        """return the representation of the state
        """
        raise NotImplementedError("Subclass this!")

    def __eq__(self, other: Any) -> bool:
        """distinguish whether the two state is the same
        """
        raise NotImplementedError("Subclass this!")

    def get_possible_moves(self) -> list:
        """get all the possible moves that the player can take
        """
        raise NotImplementedError("Subclass this!")

    def is_valid_move(self, move: Any) -> bool:
        """distinguish whether the num is a valid move
        """
        return move in self.get_possible_moves()

    def get_current_player_name(self) -> str:
        """return the player who make the current move
        """
        return self.player

    def make_move(self, move: Any) -> "State":
        """return the next game state after the move
        """
        raise NotImplementedError("Subclass this!")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
