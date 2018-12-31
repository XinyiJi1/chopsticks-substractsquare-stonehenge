"""
chopsticks class material
"""
from chopsticks_state import Chopsticksstate
from game import Game


class Chopsticks(Game):
    """
    a game called chopsticks, you can find it in the webset
    current_state is the current state
    """
    current_state: Chopsticksstate

    def __init__(self, turn: bool) -> None:
        """
        create a new game with turn to p1 or p2,overriden
        >>> a = Chopsticks(True)
        >>> a.current_state.player
        'p1'
        """
        if turn:
            self.current_state = Chopsticksstate('p1')
        else:
            self.current_state = Chopsticksstate('p2')

    def __str__(self) -> str:
        """
        return the representation of this game,overriden
        >>> a = Chopsticks(True)
        >>> 'this is Chopsticks game' in str(a)
        True
        """
        return "this is Chopsticks game" +\
            "the current state of this game is{}".format(self.current_state)

    def get_instructions(self) -> str:
        """represent the instruction to play this game to the players,overriden
        >>> a = Chopsticks(True)
        >>> "Players take turns adding" in a.get_instructions()
        True
        """
        return "Players take turns adding the value of" +\
               "one of their hands to one of " +\
            "their opponents(modulo 5).A hand with a total of five " +\
               "(or 0; 5 module 5) is considered 'dead',the first player to" +\
            "have two dead hands is the looser."

    def is_over(self, current_state: Chopsticksstate) -> bool:
        """return whether the game is over,overriden
        """
        if current_state.p1l % 5 == 0 and current_state.p1r % 5 == 0:
            a1 = 'True'
        else:
            a1 = 'False'
        if current_state.p2l % 5 == 0 and current_state.p2r % 5 == 0:
            a2 = 'True'
        else:
            a2 = 'False'
        return a1 == 'True' or a2 == 'True'

    def str_to_move(self, move: str) -> str:
        """convert any syntactically correct move into a movement,overriden
        """
        assert len(move) == 2, "we actually need a correct movement"
        return move

    def is_winner(self, suppose: str) -> bool:
        """
        distinguish whether the people we supposed is the winner,overriden
        """
        if not self.is_over(self.current_state):
            return False
        if self.current_state.p1l % 5 == 0 and self.current_state.p1r % 5 == 0:
            a1 = 'True'
        else:
            a1 = 'False'
        if a1 == 'True':
            winner = 'p2'
        else:
            winner = 'p1'
        return suppose == winner


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
