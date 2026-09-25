"""
Tic Tac Toe Player
"""

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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count += 1
            elif board[i][j] == O:
                count -= 1
    if count == 0:
        print(count)
        return X
    else:
        print(count)
        return O



def actions(board):
    """
    raise NotImplementedError
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                    action.add((i,j))
    return action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    for i in range(3):
        for j in range(3):
            if i == action[0] and j == action[1]:
                if board[i][j] == EMPTY:
                    board[i][j] = action[0][1]
                else:
                    Exception("Invalid move")




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        count = 0
        for j in range(3):
            #TODO
            print()

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        count = 0
        for j in range(3):
            #TODO
            print()


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
