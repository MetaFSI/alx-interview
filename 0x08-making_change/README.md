Certainly! Here's an updated README.md file with links to the directory and file:

# Project: 0x08. Making Change

## Overview
This repository contains the solution for the "0. Change comes from within" project, which is part of the ALX Africa Intranet curriculum. The project focuses on solving the coin change problem using algorithms, specifically dynamic programming and greedy algorithms.

## Project Description
The goal of the project is to determine the fewest number of coins needed to meet a given total amount, given a list of coin denominations. The solution is implemented in Python and must adhere to certain requirements and guidelines.

## Project Details
- **Project Title:** 0x08. Making Change
- **Author:** Carrie Ybay, Software Engineer at Holberton School
- **Project Start:** Feb 26, 2024 4:00 AM
- **Project Deadline:** Mar 1, 2024 4:00 AM
- **Checker Release:** Feb 27, 2024 4:00 AM
- **Auto Review:** Will be launched at the deadline

## Concepts Covered
The project covers the following key concepts:
- **Greedy Algorithms:**
  - Understanding how greedy algorithms work
  - Recognizing limitations and scenarios where they might not provide optimal solutions
- **Dynamic Programming:**
  - Basic principles as a method to solve optimization problems
  - Overlapping subproblems and optimal substructure in the context of the coin change problem
- **Algorithmic Complexity:**
  - Analyzing the time and space complexity of algorithms
  - Striving for solutions with lower complexity to meet runtime constraints
- **Problem-Solving Strategies:**
  - Breaking down the problem into smaller, manageable sub-problems
  - Iterative vs recursive approaches to dynamic programming
- **Python Programming:**
  - Manipulating lists and using list comprehensions
  - Implementing functions with efficient looping and conditional statements

## Additional Resources
- [Python Official Documentation](https://docs.python.org/3/): More Control Flow Tools (for loops, if statements)
- [GeeksforGeeks Articles](https://www.geeksforgeeks.org/): Coin Change | DP-7 Greedy Algorithm to find Minimum number of Coins
- [YouTube Tutorials](https://www.youtube.com/): Dynamic Programming - Coin Change Problem for a visual and step-by-step explanation of the dynamic programming approach

## Project Requirements
### General
- Allowed Editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

### Task Details
#### 0. Change comes from within
- Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- Assume you have an infinite number of each denomination of coin in the list
- Solution’s runtime will be evaluated in this task

### Testing
To test the solution, use the provided `0-main.py` file. Example:
```bash
$ cat 0-main.py
#!/usr/bin/python3
""" Main file for testing """
makeChange = __import__('0-making_change').makeChange
print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
$ ./0-main.py
7
-1
```

## Repository Structure
The repository is organized as follows:
- **Directory:** [0x08-making_change](https://github.com/sabrallah/alx-interview/tree/master/0x08-making_change)
- **File:** [0-making_change.py](https://github.com/sabrallah/alx-interview/blob/master/0x08-making_change/0-making_change.py)

## Acknowledgments
This project is part of the ALX Africa Intranet curriculum, and credit goes to Carrie Ybay, Software Engineer at Holberton School, for creating and guiding through the project.

## License
Copyright © 2024 ALX, All rights reserved.