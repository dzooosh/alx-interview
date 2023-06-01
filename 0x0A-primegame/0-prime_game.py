#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ isWinner determines players with most wins
    Args:
        x: number of rounds
        nums: array of n
    Returns:
        name of the player that won the most rounds
    """
    # players: Maria and Ben
    Maria = 0
    Ben = 0

    # Rounds
    for round in range(x):
        # list_values stores the consecutive integers 1 to n
        list_values = []
        prime_nos = []

        try:  # used to catch indexError if rounds are more than nums
            for n in range(1, (nums[round]+1)):  # the n in nums
                list_values.append(n)
                # determine the prime numbers from the list_values as well
                if n == 2:
                    prime_nos.append(n)
                for j in range(2, n):
                    if n % j == 0:
                        break
                    if j+1 == n:
                        prime_nos.append(n)

            # since the picks starts with Maria,
            # Maria's turn will be odds (1, 3, 5) while Ben on evens
            # check if the len of prime_nos is odd or even
            if len(prime_nos) % 2 == 0:
                Ben += 1
            else:
                Maria += 1

        except IndexError:
            break
    # Winner
    if Maria > Ben:
        return ("Maria")
    elif Ben > Maria:
        return ("Ben")
    elif Ben == Maria:
        return None
