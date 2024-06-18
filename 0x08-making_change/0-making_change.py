#!/usr/bin/python3
""" making_change module """


def makeChange(coins, total):
    """
    Returns: the fewest number of coins needed to meet total
    if total is 0 or less, return 0
    if total cannot be met by any combination of the coins
    return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    changes = 0
    coins = sorted(coins)[::-1]
    for coinz in coins:
        while coinz <= total:
            total -= coinz
            changes += 1
        if (total == 0):
            return changes
    return -1
