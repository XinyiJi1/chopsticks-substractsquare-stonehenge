"""
an implement of the game and the state of stonehenge
"""
from typing import Any
from game_state import GameState
from game import Game


class StonehengeState(GameState):
    """
    The state of a game stonehenge state at a certain point in time.
    p1 - the score of player1
    p2 - the score of player2
    lenn - the length of the state
    cell - the list of the list of the cells in one row
    ley - the list of the ley-line

    """
    p1: int
    p2: int
    lenn: int
    cell: list
    ley: list

    def __init__(self, is_p1_turn: bool, lenn: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.
        extended
        >>> a = StonehengeState(True, 2)
        >>> a.lenn
        2

        """
        super().__init__(is_p1_turn)
        self.p1, self.p2, self.lenn = 0, 0, lenn
        self.cell, self.ley = [], []
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(lenn):
            a = []
            for _j in range(i+2):
                a.append(s[0])
                s = s[1:]
            self.cell.append(a)
        self.cell.append([s[x] for x in range(lenn)])
        self.ley.append(['@' for _i in range(lenn + 1)])
        self.ley.append(['@' for _i in range(lenn + 1)])
        self.ley.append(['@' for _i in range(lenn + 1)])

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        override
        """
        n = self.lenn
        s = ' ' * (4+2 * n) + self.ley[0][0] + '   ' + self.ley[0][1]
        s += "\n" + ' ' * (3+2 * n) + '/   ' * 2 + '\n'
        for i in range(n):
            s += '  ' * (n-1-i) + self.ley[1][i]
            for j in range(len(self.cell[i])):
                s += ' - ' + self.cell[i][j]
            if i < n-1:
                s += '   ' + self.ley[0][2 + i] + '\n'
                s += ' ' * (2 * n + 1 - 2 * i) + '/ \\ ' * (len(self.cell[i])) \
                     + '/'
            s += '\n'
        s += ' ' * 5 + '\\ / ' * n + "\\" + '\n' + '  ' + self.ley[1][n]
        for i in range(n):
            s += ' - ' + self.cell[n][i]
        s += '   ' + self.ley[2][0] + '\n' + '       ' + '\\   ' * n + '\n' \
             + ' ' * 8
        for i in range(n, 0, -1):
            s += self.ley[2][i] + '   '
        return s

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        override
        >>> a = StonehengeState(True, 2)
        >>> a.get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        """
        result = []
        half = 3 * (self.lenn + 1) / 2
        if self.p1 >= half or self.p2 >= half:
            return result
        for i in range(self.lenn + 1):
            for j in range(len(self.cell[i])):
                if self.cell[i][j] != '1' and self.cell[i][j] != '2':
                    result += self.cell[i][j]
        return result

    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        override
        >>> a = StonehengeState(True, 2)
        >>> b = a.make_move('A')
        >>> b.lenn
        2
        """
        a, b = 0, 0
        new = StonehengeState(not self.p1_turn, self.lenn)
        new.p1, new.p2 = self.p1, self.p2
        for i in range(self.lenn + 1):
            for j in range(len(self.cell[i])):
                new.cell[i][j] = self.cell[i][j]
        for i in range(3):
            for j in range(len(self.ley[i])):
                new.ley[i][j] = self.ley[i][j]
        for i in range(new.lenn + 1):
            for j in range(len(new.cell[i])):
                if new.cell[i][j] == move:
                    new.cell[i][j] = '1' if self.p1_turn else '2'
                    a, b = i, j
        new.row(a)
        new.left(a, b)
        new.right()
        return new

    def row(self, a: int) -> None:
        """
        change the ley for the row after the move
        >>> b = StonehengeState(True, 2)
        >>> b.row(1)
        >>> b.lenn
        2
        """
        summ = 0
        if self.p1_turn:
            for j in range(len(self.cell[a])):
                if self.cell[a][j] == '2':
                    summ += 1
            if summ >= len(self.cell[a]) / 2 and self.ley[1][a] == '@':
                self.ley[1][a] = '2'
                self.p2 += 1
        else:
            for j in range(len(self.cell[a])):
                if self.cell[a][j] == '1':
                    summ += 1
            if summ >= len(self.cell[a]) / 2 and self.ley[1][a] == '@':
                self.ley[1][a] = '1'
                self.p1 += 1

    def left(self, a: int, b: int) -> None:
        """
        change the ley for the left diagonal after the move
        >>> b = StonehengeState(True, 2)
        >>> b.left(1,1)
        >>> b.lenn
        2
        """
        suml = []
        result = 0
        if a == self.lenn:
            a -= 1
            b += 1
        for i in range(self.lenn):
            if len(self.cell[i]) > b:
                suml.append(self.cell[i][b])
        if b != 0:
            suml.append(self.cell[self.lenn][b - 1])
        if self.p1_turn:
            for element in suml:
                if element == '2':
                    result += 1
            if result >= len(suml) / 2:
                if self.ley[0][b] == '@':
                    self.ley[0][b] = '2'
                    self.p2 += 1
        else:
            for element in suml:
                if element == '1':
                    result += 1
            if result >= len(suml) / 2:
                if self.ley[0][b] == '@':
                    self.ley[0][b] = '1'
                    self.p1 += 1

    def right(self) -> None:
        """
        change the ley for the right diagonal after the move
        >>> b = StonehengeState(True, 2)
        >>> b.right()
        >>> b.lenn
        2
        """
        suml = [[], [], [], [], [], []]
        for i in range(self.lenn):
            m = 0
            for j in range(len(self.cell[i])-1, -1, -1):
                suml[m].append(self.cell[i][j])
                m += 1
        j = 1
        for i in range(self.lenn - 1, -1, -1):
            suml[j].append(self.cell[self.lenn][i])
            j += 1
        for i in range(self.lenn + 1):
            result = 0
            for element in suml[i]:
                if element == '2':
                    result += 1
            if result >= len(suml[i]) / 2 and self.ley[2][i] == '@':
                self.p2 += 1
                self.ley[2][i] = '2'
            result = 0
            for element in suml[i]:
                if element == '1':
                    result += 1
            if result >= len(suml[i]) / 2 and self.ley[2][i] == '@':
                self.p1 += 1
                self.ley[2][i] = '1'

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).override
        """
        return "p1_turn:{},p1:{},p2{},length{},cell:{},ley:{}".\
            format(self.p1_turn, self.p1, self.p2, self.lenn, self.cell,
                   self.ley)

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.override
        >>> a = StonehengeState(True, 2)
        >>> a.rough_outcome()
        0
        """
        half = 3 * (self.lenn + 1) / 2
        for move in self.get_possible_moves():
            state1 = self.make_move(move)
            if state1.p1 >= half or state1.p2 >= half:
                return self.WIN
        for move in self.get_possible_moves():
            state1 = self.make_move(move)
            n = 0
            for move2 in state1.get_possible_moves():
                state2 = state1.make_move(move2)
                if state2.p1 >= half or state2.p2 >= half:
                    n = 1
            if n == 0:
                return self.DRAW
        return self.LOSE


class StonehengeGame(Game):
    """
    Abstract class for a game stonehenge to be played with two players.
    current_state-the current state of this game
    current_state: the state of the game

    """
    current_state: StonehengeState

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        override
        """
        lenn = int(input("Enter the side length of the board:"))
        self.current_state = StonehengeState(p1_starts, lenn)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.override
        """
        return "instruction is the following"

    def is_over(self, state: StonehengeState) -> bool:
        """
        Return whether or not this game is over at state.override
        """
        half = 3 * (state.lenn + 1) / 2
        return state.p1 >= half or state.p2 >= half

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.override

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player
                and self.is_over(self.current_state))

    def str_to_move(self, string: str) -> Any:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.override
        """
        assert string in "QWERTYUIOPASDFGHJKLZXCVBNM"
        return string


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
