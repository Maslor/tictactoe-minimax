"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    flattened_board = sum(board, [])
    count_x = flattened_board.count(X)
    count_o = flattened_board.count(O)

    if count_o < count_x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))
            j += 1
        i += 1

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    manipulated_board = copy.deepcopy(board)
    current_player = player(board)

    manipulated_board[action[0]][action[1]] = current_player

    return manipulated_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for line in board:
        if all_the_same(line):
            return line[0]

    diagonals = [[board[0][0], board[1][1], board[2][2]],
                 [board[0][2], board[1][1], board[2][0]]]
    for diagonal in diagonals:
        if all_the_same(diagonal):
            return diagonal[0]

    columns = [[board[0][0], board[1][0], board[2][0]],
               [board[0][1], board[1][1], board[2][1]],
               [board[0][2], board[1][2], board[2][2]]]

    for column in columns:
        if all_the_same(column):
            return column[0]


def all_the_same(list):
    if len(set(list)) <= 1 and list[0] is not EMPTY:
        return True
    else:
        return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flattened_board = sum(board, [])
    if winner(board) is not None or flattened_board.count(EMPTY) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        scores = dict()
        for action in actions(board):
            minimum = min_value(result(board, action))
            scores[action] = minimum
        return max(scores, key=scores.get)

    else:
        scores = dict()
        for action in actions(board):
            maximum = max_value(result(board, action))
            scores[action] = maximum
        return min(scores, key=scores.get)


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -2
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def min_value(board):
    value = 2
    if terminal(board):
        return utility(board)
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
