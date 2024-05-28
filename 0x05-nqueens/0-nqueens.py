#!/usr/bin/python3
"""0-nqueens.py"""
import sys


def is_safe(board, row, col, n):
    """
    is_safe func to check if there is a queen in the same column
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    """
    print the solution
    """
    if row == n:
        print([[i, j] for i in range(n) for j in range(n) if board[i][j] == 1])
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0

    return False


if __name__ == '__main__':
    """
    main
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for j in range(n)] for i in range(n)]
    """
    running this shit recursively
    """
    solve(board, 0, n)