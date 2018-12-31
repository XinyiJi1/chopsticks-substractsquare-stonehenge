"""
strategy module
"""
from typing import Any
import random
from game import Game


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


# TODO: Implement a random strategy.
def random_strategy(game: Game) -> Any:
    """
    Return a random move for game
    """
    moves = game.current_state.get_possible_moves()
    move = random.choice(moves)
    return move


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
