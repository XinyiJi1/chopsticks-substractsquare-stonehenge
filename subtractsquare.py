"""
subtractsquare class material
"""
from subtractsquare_state import Subtractsquarestate
from game import Game


class Subtractsquare(Game):
    """
    a game called subtractsquare, you can find it in the webset
    current_state is the current state
    """
    current_state: Subtractsquarestate

    def __init__(self, turn: bool) -> None:
        """
        create a new game with the turn of the player,overriden
       """
        a = input("Enter the number to subtract form:")
        a = int(a)
        if turn:
            self.current_state = Subtractsquarestate(a, 'p1')
        else:
            self.current_state = Subtractsquarestate(a, 'p2')

    def __str__(self) -> str:
        """
        return the representation of this game,overriden
        """
        return "this is Subtractsquare game" +\
            "the current state of this game is{}.".format(self.current_state)

    def get_instructions(self) -> str:
        """represent the instruction to play this game to the players,overriden
        """
        return "Players take turns subtracting square numbers " +\
            "from the starting number. The looser is the " +\
               "person who cannot substract anymore"

    def is_over(self, current_state: Subtractsquarestate) -> bool:
        """return whether the game is over with the current_state,overriden
        """
        return current_state.number == 0

    def str_to_move(self, move: str) -> int:
        """convert any syntactically correct move into a movement,overriden
        """
        a = int(move)
        return a

    def is_winner(self, suppose: str) -> bool:
        """
        distinguish whether the people we supposed is the winner,overriden
        """
        if not self.is_over(self.current_state):
            return False
        if self.current_state.player == 'p1':
            winner = 'p2'
        else:
            winner = 'p1'
        return suppose == winner


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
