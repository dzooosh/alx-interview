#!/usr/bin/python3

""" Minimum Operations
"""


def minOperations(n: int) -> int:
    """ fewest number of operations needed to result
    in exactly n H characters in the file
    Args:
        n - number to achieve after all operations
    Returns:
        number of operations (int)
    """
    if n == 0:
        return 0
    num_of_operation = 0
    prev = pres = 1

    # if n can be divided by present_num - copy and paste
    # if n cannot be divided by present_num - paste
    while True:
        if pres == 1 and n > 1:
            # copy
            pres = prev
            num_of_operation += 1
            # paste
            pres = pres + prev
            num_of_operation += 1
        elif n % pres == 0 and pres > 1:
            # copy
            prev = pres
            num_of_operation += 1
            # paste
            pres = pres + prev
            num_of_operation += 1
        else:
            # paste
            pres = pres + prev
            num_of_operation += 1
        # check if present is eq to n to break the loop
        if pres == n:
            break
        elif pres > n:
            # if present number is higher than n then its impossible
            return 0

    return num_of_operation
