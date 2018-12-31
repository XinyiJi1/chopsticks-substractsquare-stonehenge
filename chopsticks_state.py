"""
Chopsticksstate class material
"""
from typing import Any, List
from state import State


class Chopsticksstate(State):
    """
    the current state of the game Chopsticks
    p1l is the left hand of player1
    p1r is the right hand of player1
    p2l is the left hand of player2
    p2r is the right hand of player2
    player is the current player
    """
    p1l: int
    p1r: int
    p2l: int
    p2r: int
    player: str

    def __init__(self, player: str) -> None:
        """create the state of a game with current player,overriden
        >>> a = Chopsticksstate('p1')
        >>> a.p1l
        1
        >>> a.p1r
        1
        >>> a.p2l
        1
        >>> a.p2r
        1
        >>> a.player
        'p1'
        """
        self.p1l, self.p1r = 1, 1
        self.p2l, self.p2r = 1, 1
        self.player = player

    def __str__(self) -> str:
        """return the representation of the state,overriden
        >>> a = Chopsticksstate('p1')
        >>> print(a)
        Player 1: 1 - 1; Player 2: 1 - 1
        """
        return "Player 1: {} - {}; Player 2: {} - {}".\
            format(self.p1l, self.p1r, self.p2l, self.p2r)

    def __eq__(self, other: Any) -> bool:
        """distinguish whether the two state is the same,overriden
        >>> a = Chopsticksstate('p1')
        >>> b = Chopsticksstate('p2')
        >>> a == b
        False
        """
        return type(self) == type(other) and self.p1l == other.p1l\
            and self.player == other.player and self.p1r == other.p1r\
            and self.p2l == other.p2l and self.p2r == other.p2r

    def get_possible_moves(self) -> List[str]:
        """get all the possible moves that the player can take,overriden
        >>> a = Chopsticksstate('p1')
        >>> a.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        result = []
        player1 = ''
        player2 = ''
        if self.p1l % 5 != 0:
            player1 += 'l'
        if self.p1r % 5 != 0:
            player1 += 'r'
        if self.p2l % 5 != 0:
            player2 += 'l'
        if self.p2r % 5 != 0:
            player2 += 'r'
        if self.player == 'p1':
            for i in player1:
                for j in player2:
                    result.append(i+j)
        else:
            for i in player2:
                for j in player1:
                    result.append(i+j)
        return result

    def is_valid_move(self, move: str) -> bool:
        """distinguish whether the move is a valid move,extended
        >>> a = Chopsticksstate('p1')
        >>> a.is_valid_move('ll')
        True
        >>> a.is_valid_move('lr')
        True
        """
        return State.is_valid_move(self, move)

    def make_move(self, move: str) -> "Chopsticksstate":
        """return the next game state after the move,overriden
        >>> a = Chopsticksstate('p1')
        >>> b = a.make_move('ll')
        >>> b.p1l
        1
        >>> b.p1r
        1
        >>> b.p2l
        2
        >>> b.p2r
        1
        >>> b.player
        'p2'
        """
        if self.player == 'p1':
            b = Chopsticksstate('p2')
            if move == 'll':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, self.p1r, \
                                             (self.p2l + self.p1l) % 5, self.p2r
            elif move == 'lr':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, self.p1r, self.p2l, \
                                             (self.p2r + self.p1l) % 5
            elif move == 'rl':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, self.p1r, \
                                             (self.p2l + self.p1r) % 5, self.p2r
            elif move == 'rr':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, self.p1r, self.p2l, \
                                             (self.p2r + self.p1r) % 5
        else:
            b = Chopsticksstate('p1')
            if move == 'll':
                b.p1l, b.p1r, b.p2l, b.p2r = (self.p1l + self.p2l) % 5, \
                                             self.p1r, self.p2l, self.p2r
            elif move == 'lr':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, \
                                             (self.p1r + self.p2l) % 5, \
                                             self.p2l, self.p2r
            elif move == 'rl':
                b.p1l, b.p1r, b.p2l, b.p2r = (self.p1l+self.p2r) % 5, \
                                             self.p1r, self.p2l, self.p2r
            elif move == 'rr':
                b.p1l, b.p1r, b.p2l, b.p2r = self.p1l, \
                                             (self.p1r+self.p2r) % 5, \
                                             self.p2l, self.p2r
        return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
