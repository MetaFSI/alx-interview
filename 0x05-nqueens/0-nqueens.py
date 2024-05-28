#!/usr/bin/python3
"""
This module contains a program that solves the N Queens problem.

The N Queens problem is the challenge of placing N non-attacking queens on an
N×N chessboard.
"""

import sys


def solve_n_queens(n):
    """
    Solve the N Queens problem using backtracking.

    Args:
        n (int): The number of queens and the size of the chessboard.

    Returns:
        list: A list of all possible solutions. Each solution is represented
              as a list of integers where the value of i-th integer represents
              the column number of the queen placed in the i-th row.
    """
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queens(n, index, ocuppied_positions, all_ocuppied_positions):
        if index == n:
            all_ocuppied_positions.append(ocuppied_positions[:])
            return

        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queens(n, index + 1, ocuppied_positions,
                             all_ocuppied_positions)
                ocuppied_positions.pop()

    all_ocuppied_positions = []
    place_queens(n, 0, [], all_ocuppied_positions)
    return all_ocuppied_positions


def main():
    """
    The main function of the program. It checks the command line arguments and
    calls the function to solve the N Queens problem.
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

    solutions = solve_n_queens(n)
    for solution in solutions:
        result = [[i, pos] for i, pos in enumerate(solution)]
        print(result)


if __name__ == "__main__":
    main()
