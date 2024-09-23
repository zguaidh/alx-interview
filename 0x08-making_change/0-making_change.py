#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    coins_count = 0
    remainder = total

    for coin in sorted_coins:
        if remainder == 0:
            break

        coin_count = remainder // coin
        coins_count += coin_count
        remainder -= coin_count * coin

    if remainder > 0:
        return -1

    return coins_count
