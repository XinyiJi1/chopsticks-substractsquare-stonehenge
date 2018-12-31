"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from game import Game
from game_state import GameState


# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Game) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.
def recursive_strategy(game: Any) -> Any:
    """return a move for the game using minimax with recursive"""
    result = main_recursive(game, game.current_state)
    for key in result:
        if result[key] == 1:
            return key
    for key in result:
        if result[key] == 0:
            return key
    for key in result:
        if result[key] == -1:
            return key
    return None


def main_recursive(game: Any, state: GameState) -> dict:
    """return the final dictionary for strategy to pick the best one"""
    s = {}
    moves = state.get_possible_moves()
    for move in moves:
        newstate = state.make_move(move)
        if game.is_over(newstate):
            old_state = game.current_state
            game.current_state = newstate
            if game.is_winner(game.current_state.get_current_player_name()):
                s[move] = -1
            elif (not game.is_winner('p1')) and (not game.is_winner('p2')):
                s[move] = 0
            else:
                s[move] = 1
            game.current_state = old_state
        else:
            inner = main_recursive(game, newstate)
            s[move] = -maxx(inner)
    return s


def maxx(inner: dict) -> int:
    """return the max value of a dictionary to implement in main_recursive
    >>> maxx({'A': 2, 'B': 3})
    3
    """
    maxxx = -5
    for key in inner:
        if inner[key] > maxxx:
            maxxx = inner[key]
    return maxxx


# TODO: Implement an iterative version of the minimax strategy.
# taken from class(lab)
class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []

    def __repr__(self) -> str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])


# taken from class(lab)
class Stack:
    """
    Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """
        Create a new, empty Stack self.

        """
        self._contents = []

    def add(self, obj: Tree) -> None:
        """
        Add object obj to top of Stack self.

        """
        self._contents.append(obj)

    def remove(self) -> Tree:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty.


        """
        return self._contents.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True

        """
        return len(self._contents) == 0


def iterative_strategy(game: Any) -> Any:
    """return a move of game of minimax in iteration methods"""
    s = Stack()
    olditem = []
    node1 = Tree([game.current_state, None, None])
    s.add(node1)
    a = node1
    while not s.is_empty():
        a = s.remove()
        if game.is_over(a.value[0]):
            old_state = game.current_state
            game.current_state = a.value[0]
            if game.is_winner(game.current_state.get_current_player_name()):
                a.value[1] = 1
            elif (not game.is_winner('p1')) and (not game.is_winner('p2')):
                a.value[1] = 0
            else:
                a.value[1] = -1
            game.current_state = old_state
            olditem.append(a)
        elif a.children != []:
            smalllist = []
            for children in a.children:
                smalllist.append(children.value[1] * (-1))
            a.value[1] = max(smalllist)
            olditem.append(a)
        else:
            moves = a.value[0].get_possible_moves()
            s.add(a)
            for move in moves:
                b = a.value[0].make_move(move)
                node2 = Tree([b, None, move])
                a.children.append(node2)
                s.add(node2)
    for children in a.children:
        if children.value[1] == a.value[1] * (-1):
            return children.value[2]
    return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
