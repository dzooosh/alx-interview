def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]

def winner(state, current_player):
    if len(state) == 0:
        return current_player
    
    for num in state:
        new_state = [x for x in state if x % num != 0]
        winner_name = winner(new_state, "Maria" if current_player == "Ben" else "Ben")
        if winner_name == current_player:
            return current_player
    
    return "Maria" if current_player == "Ben" else "Ben"

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        primes = sieve(n)
        state = [i for i in range(1, n+1) if i not in primes]
        winner_name = winner(state, "Maria")
        if winner_name == "Maria":
            maria_wins += 1
        elif winner_name == "Ben":
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
