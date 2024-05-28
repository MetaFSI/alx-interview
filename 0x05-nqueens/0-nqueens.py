#!/usr/bin/python3
''' solve the quench problem using backtracking'''
import sys


if len(sys.argv) < 2:
    print('Usage: nqueens N')
    exit(1)
if not isinstance(int(sys.argv[1]), int):
    print('N must be a number')
    exit(1)
N = int(sys.argv[1])
if N < 4:
    print('N must be at least 4')
    exit(1)


class solution:
    def solveNquens(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in col or (row + c) in posDiag or (row - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(row + c)
                negDiag.add(row - c)
                board[row][c] = 'Q'
                backtrack(row + 1)
                col.remove(c)
                posDiag.remove(row + c)
                negDiag.remove(row - c)
                board[row][c] = '.'
        backtrack(0)

        def format_result(res):
            for solution in res:
                formatted_solution = []
                for i in range(len(solution)):
                    for j in range(len(solution[i])):
                        if solution[i][j] == 'Q':
                            formatted_solution.append([i, j])
                print(formatted_solution)
        format_result(res)


sol = solution()
sol.solveNquens(N)
