from tictactoe import player
from tictactoe import initial_state
from tictactoe import terminal
from tictactoe import actions
from tictactoe import result
from tictactoe import *
EMPTY = None
test_board = [["X", "O", "X"],
            ["O", None, "X"],
            ["O", "X", None]]
empty_board=[["X","X", "O"],
            ["O", "X", None],
            ["X", "X", None]]

print(minimax(empty_board),end=("\n"))