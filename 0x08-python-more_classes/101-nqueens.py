#!/usr/bin/python3
"""The N-queens puzzle.

Determines N
N non-attacking queens on an NxN chessboard

Example:
    $ ./101-nqueens.py N

N >= 4

Attributes:
    board: A list representing the chessboard
    answers: A list of containing answers

Format [[r, c], [r, c], [r, c], [r, c]]
where `r` represent row & `c` represent column, where a
queen must be placed on the chessboard.
"""
import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in chessboard]
    return (chessboard)


def board_deepcopy(chessboard):
    """Return a chessboard deepcopy"""
    if isinstance(chessboard, list):
        return list(map(board_deepcopy, chessboard))
    return (chessboard)


def get_solution(chessboard):
    """Return the list of solved chessboard"""
    answers = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                answers.append([r, c])
                break
    return (answers)


def xout(chessboard, row, col):
    """X out spots on a chessboard

    All spots where non-attacking queens can no
    longer be played are X-ed out

    Args:
        board: The current working chessboard
        row: The row where a queen was last played
        col: The column where a queen was last played
    """
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(chessboard, row, queens, answers):
    """solve an N-queens puzzle.

    Args:
        board: The current working chessboard
        row: The current working row
        queens: The current number of placed queens
        answers: A list of lists of answers
    Returns:
        answers
    """
    if queens == len(chessboard):
        answers.append(get_solution(chessboard))
        return (answers)

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_board = board_deepcopy(chessboard)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            answers = recursive_solve(tmp_board, row + 1, queens + 1, answers)

    return (answers)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = init_board(int(sys.argv[1]))
    answers = recursive_solve(chessboard, 0, 0, [])
    for answer in answers:
        print(answer)
