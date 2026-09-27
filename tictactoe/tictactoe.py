"""
Tic Tac Toe Player
"""

import math
import copy

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
        return X
    else:
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
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid move: Out of bounds")

    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid move")
    else:
        new_board = copy.deepcopy(board)
        play = player(new_board)
        new_board[action[0]][action[1]] = play
        return new_board





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == X:
                count += 1
            else:
                 count = 0
            if count == 3:
                return X

    for i in range(3):
            count = 0
            for j in range(3):
                if board[j][i] == X:
                    count += 1
                else:
                     count = 0
                if count == 3:
                    return X

    for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == O:
                    count += 1
                else:
                     count = 0
                if count == 3:
                    return O

    for i in range(3):
                count = 0
                for j in range(3):
                    if board[j][i] == O:
                        count += 1
                    else:
                         count = 0
                    if count == 3:
                        return O


    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
                return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
                return O
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
                    return X
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
                    return O
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:

        return True
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if count == 9:
        return True
    else:
         return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
          return -1
    else:
        return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    play = player(board)
    if play == X:
        best_score = -math.inf
        best_move = None
    else:
        best_score = math.inf
        best_move = None


    for action in actions(board):

      simulated_board = result(board, action)

      if play == X:
        score = min_value(simulated_board)
      else:
        score = max_value(simulated_board)

      if play == X:
        if score > best_score:
          best_score = score
          best_move = action
      else:
          if score < best_score:
                    best_score = score
                    best_move = action

    return best_move




def min_value(simulated_board):
    v = math.inf
    if terminal(simulated_board):
          return utility(simulated_board)
    for action in actions(simulated_board):
        new_board = result(simulated_board,action)
        score = max_value(new_board)
        if score < v:
            v = score
    return v



def max_value(simulated_board):
        v = -math.inf
        if terminal(simulated_board):
                return utility(simulated_board)
        for action in actions(simulated_board):
            new_board = result(simulated_board,action)
            score = min_value(new_board)
            if score > v:
                v = score
        return v