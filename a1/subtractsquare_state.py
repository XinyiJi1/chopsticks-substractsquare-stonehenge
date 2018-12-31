"""
Subtractsquarestate class material
"""
from typing import Any, List
from state import State


class Subtractsquarestate(State):
    """
    the current state of the game subtractsquare
    number is the current number
    player is the current player
    """
    number: int
    player: str

    def __init__(self, number: int, player: str) -> None:
        """create the state of a game with number and player,overriden
        >>> a = Subtractsquarestate(8, 'p1')
        >>> a.number
        8
        >>> a.player
        'p1'
        """
        self.number = number
        self.player = player

    def __str__(self) -> str:
        """return the representation of the state,overriden
        >>> a = Subtractsquarestate(8, 'p1')
        >>> print(a)
        value8
        """
        return 'value' + str(self.number)

    def __eq__(self, other: Any) -> bool:
        """distinguish whether the two state is the same,overriden
        >>> a = Subtractsquarestate(8, 'p1')
        >>> b = Subtractsquarestate(8, 'p1')
        >>> a == b
        True
        """
        return type(self) == type(other) and self.number == other.number\
            and self.player == other.player

    def get_possible_moves(self) -> List[int]:
        """get all the possible moves that the player can take,overriden
        >>> a = Subtractsquarestate(8, 'p1')
        >>> a.get_possible_moves()
        [1, 4]
        """
        result = []
        for i in range(1, self.number + 1):
            if i**2 <= self.number:
                result.append(i**2)
        return result

    def is_valid_move(self, move: int) -> bool:
        """distinguish whether the move is a valid move,extended
        >>> a = Subtractsquarestate(8, 'p1')
        >>> a.is_valid_move(1)
        True
        >>> a.is_valid_move(18)
        False
        """
        return State.is_valid_move(self, move)

    def make_move(self, move: int) -> "Subtractsquarestate":
        """return the next game state after the move,overriden
        >>> a = Subtractsquarestate(8, 'p1')
        >>> b = a.make_move(1)
        >>> b.number
        7
        >>> b.player
        'p2'
        """
        a = self.number
        a -= move
        if self.player == 'p1':
            b = 'p2'
        else:
            b = 'p1'
        return Subtractsquarestate(a, b)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
