#!/usr/bin/python3
""" Making Change Function """
from math import floor


def makeChange(coins: list, total: int) -> int:
    """ make change function
    Args:
        coins - list of values of the coins in your possession
        total - total value of the change
    Return:
        fewest number of coins needed to meet total
    """
    # if total is less or equal to 0 return 0
    if total <= 0:
        return 0

    # sort the coins and reverse to loop from highest to lowest
    coins.sort(reverse=True)
    # create 2 variables before the loop: remainder, num_of_div
    remainder = 1
    num_of_div = 0

    # check if any coin is higher than the total
    if coins[0] > total:
        return -1

    # loop through the coin list
    # starts with the highest coin
    for coin in coins:
        # print(coin)
        if total == 0:
            break
        if remainder != 0:
            # total % coin_value = remainder
            remainder = total % coin
            # total / coin_value = num_of_div
            num_of_div += total / coin
            num_of_div = floor(num_of_div)
            total = remainder

    # if after the loop, remainder is not equal zero,
    # return -1
    if remainder > 0:
        return -1
    else:
        # return num_of_div
        return num_of_div
