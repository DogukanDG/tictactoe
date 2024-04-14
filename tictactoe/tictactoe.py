"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board) == False:
        num_of_x=0
        num_of_o=0
        for i in board:
            for j in i:
                if j == "X":
                    num_of_x += 1
                    continue
                if j == "O":
                    num_of_o += 1
                    continue
        if num_of_x == 0 or num_of_x == num_of_o : 
            return "X"
        if num_of_o < num_of_x : 
            return "O"

    else:
        return "Game is Over"
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = list()
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] is None:
               possible_actions.append((row,cell))
    return possible_actions

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    will return a state
    """
    copy_board = copy.deepcopy(board)
    if action in actions(copy_board):
        if player(board) == "X":
            copy_board[action[0]][action[1]] = "X" 
            return copy_board
        else: 
            copy_board[action[0]][action[1]] = "O" 
            return copy_board
    else:
        raise NameError('Not a possible action')
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check the board horizontally
    for row in board:
        if all(cell == X for cell in row):
            return "X"
        if all(cell == O for cell in row):
            return "O"

    #check vertical
    if (board[0][0]==board[1][0]==board[2][0]):
        return(board[0][0])
    if (board[0][1]==board[1][1]==board[2][1]):
        return(board[0][1])
    if (board[0][2]==board[1][2]==board[2][2]):
        return(board[0][2])

    #check diognals
    if (board[0][0]==board[1][1]==board[2][2]) and board[0][0]:
        return(board[0][0])
    if (board[2][0]==board[1][1]==board[0][2]) and board[2][0]:
        return(board[2][0])
    
    return None
        

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # Check if board is full
    if all(cell is not None for row in board for cell in row):
        return True

    # If there's no winner and the board is not full, the game is not over
    return False
   



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1 
    elif winner(board) == "O":
        return -1
    else:return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if terminal(board) == True:
    #     return utility(board)
    # else:
    #     v = float('-inf')
    #     for i in actions(board):
    #         new_board= result(board,i)
    #         value = minimax(new_board)
    #         v = max(v,minimax(new_board))
    #     return v    
    # if terminal(board):
    #     return utility(board)
    # else:
    #     best_value = float('-inf')
    #     best_action = None
    #     for action in actions(board):
    #         new_board = result(board, action)
    #         value = minimax(new_board)
    #         if value > best_value:
    #             best_value = value
    #             best_action = action
    #     return best_value
    # #raise NotImplementedError
    if terminal(board):
        return None
    else:
        def max_value(board):
            if terminal(board):
                return utility(board)
            v = float("-inf")
            for action in actions(board):
                v = max(v, min_value(result(board, action)))
            return v

        def min_value(board):
            if terminal(board):
                return utility(board)
            v = float("inf")
            for action in actions(board):
                v = min(v, max_value(result(board, action)))
            return v
        
        if player(board) == X:
            best_action = None
            v = float("-inf")
            for action in actions(board):
                min_val = min_value(result(board, action))
                if min_val > v:
                    v = min_val
                    best_action = action
            return best_action
        else:
            best_action = None
            v = float("inf")
            for action in actions(board):
                max_val = max_value(result(board, action))
                if max_val < v:
                    v = max_val
                    best_action = action
            return best_action

