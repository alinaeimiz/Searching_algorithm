"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
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
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)


    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for index_row, row in enumerate(board):
        for index_col, item in enumerate(row):
            if item == None:
                possible.add((index_row, index_col))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board







def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):

        for row in board:
            if row == [player] * 3:
                return player

        for y in range(3):
            col = [board[x][y] for x in range(3)]
            if col == [player] * 3:
                return player

        if [board[i][i] for i in range(3)] == [player] * 3:
            return player

        elif [board[i][~i] for i in range(3)] == [player] * 3:
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    # moves still possible
    for row in board:
        if EMPTY in row:
            return False

    # no possible moves
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        bestMove = ()
        if terminal(board):
            return utility(board), bestMove
        else:
            v = float('-inf')
            for action in actions(board):
                minValue = min_value(result(board, action))[0]
                if minValue > v:
                    v = minValue
                    bestMove = action
            return v, bestMove

    def min_value(board):
        bestMove = ()
        if terminal(board):
            return utility(board),bestMove
        else:
            v = float('inf')

            for action in actions(board):
                maxValue = max_value(result(board, action))[0]
                if maxValue < v:
                    v = maxValue
                    bestMove = action
            return v, bestMove

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
