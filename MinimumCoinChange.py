import sys
def minCoinChange(change, coins):
    if change <= 0:
        return 0

    possibles = [sys.maxsize]
    for coin in coins:
        if change >= coin:
            possibles.append(1+minCoinChange(change-coin, coins))

    return min(possibles)

print(minCoinChange(13, [1,2,5]))

def minCoinChangeDp(change, coins):
    solutions = [sys.maxsize for x in range(change+1)]

    solutions[0] = 0
    for i in range(1, change+1):
        possibles = [sys.maxsize]
        for coin in coins:
            if i - coin >= 0:
                possibles.append(solutions[i-coin])

        solutions[i] = 1+min(possibles)

    return solutions[change]

print (minCoinChangeDp(13,[1,2,5]))