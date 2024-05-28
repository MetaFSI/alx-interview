#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N Queens problem, which is the challenge of placing N
non-attacking queens on an N×N chessboard.

Usage:
    ./0-nqueens.py N

Where N is the size of the chessboard (an integer greater than or equal to 4).
"""

import sys


def print_solution(board):
    """
    Print the board in the required format.

    Args:
        board (list): The current state of the chessboard.
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col):
    """
    Utilize backtracking to solve the N Queens problem.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column index.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0
    return res


def solve_nqueens(n):
    """
    Solve the N Queens puzzle and print all solutions.

    Args:
        n (int): The size of the chessboard.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")


if __name__ == "__main__":
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
    solve_nqueens(n)
