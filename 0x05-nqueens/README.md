# 0x05. N Queens

## Algorithm

This repository contains a Python implementation of the N Queens puzzle-solving algorithm. The challenge is to place N non-attacking queens on an N×N chessboard. The solution is provided in the file `0-nqueens.py`.

### Author
- Alexa Orrico, Software Engineer at Holberton School

### Project Information
- Weight: 1
- Project Start: Feb 5, 2024, 4:00 AM
- Project End: Feb 9, 2024, 4:00 AM
- Checker Release: Feb 6, 2024, 4:00 AM
- Auto Review Deadline: Feb 9, 2024, 4:00 AM

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.*)
- All files must be executable

## Tasks

### 0. N queens (mandatory)

#### Description
Chess grandmaster Judit Polgár, the strongest female chess player of all time.

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

#### Usage
```bash
nqueens N
```

- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1.
- N must be an integer greater or equal to 4.
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1.
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1.
- The program should print every possible solution to the problem.
- One solution per line.
- Format: see example.
- Solutions don’t have to be printed in a specific order.
- Only allowed to import the sys module.

#### Example
```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Repo Information

- GitHub repository: [alx-interview](https://github.com/sabrallah/alx-interview/tree/master)
- Directory: [0x05-nqueens](https://github.com/sabrallah/alx-interview/tree/master/0x05-nqueens) 
- File: `0-nqueens.py`