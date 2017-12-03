changeMap = {25:10, 10:5, 5:1, 1:0}

def waysOfChange(cents, changeWith) :
    if changeWith == 1:
        return 1
    else:
        ways = 0
        i = 0
        while cents - i*changeWith >= 0:
            ways += waysOfChange(cents-i*changeWith, changeMap[changeWith])
            i+=1

    return ways

#print(waysOfChange(83, 25))

def makeChange(change, coins):
    if change == 0:
        return 0

    return makeChangeUsingDenom(change, coins, 0)

def makeChangeUsingDenom(amt, coins, denomIdx):
    i = 0
    ways = 0
    if coins[denomIdx] == 1:
        return 1

    while amt - i*coins[denomIdx] >= 0:
        ways += makeChangeUsingDenom(amt - i*coins[denomIdx], coins, denomIdx+1)
        i += 1

    return ways

#print(makeChange(36, [25,10,5,1]))

def coinChange(amt, coins):
    if amt == 0:
        return 1

    if amt < 0:
        return 0

    if len(coins) == 0:
        return 0

    return coinChange(amt, coins[1:]) + coinChange(amt-coins[0], coins)

#print(coinChange(36, [25,10,5,1]))

def coinChangeDp(amt, coins):

    changes = [[0 for y in range(amt+1)] for x in range(len(coins)+1)]
    for x in range(len(coins)+1):
        changes[x][0] = 1

    #changes(amt, coins, N) = changes(amt, coins, N-1) + changes(amt-coins[n-1], N)
    for x in range(1, len(coins)+1):
        for y in range(1, amt+1):
            if (y < coins[x-1]):
                changes[x][y] = changes[x-1][y]
            else:
                withoutCoinX = changes[x-1][y]
                withCoinX = changes[x][y-coins[x-1]]
                changes[x][y] = withoutCoinX + withCoinX

    print(changes)
    return changes[len(coins)][amt]

def concat(input, addition):
    if input == [-1]:
        return [-1]
    return input+[addition]

def coinChangeOptionsDp(amt, coins):
    changes = [[[[]] for y in range(amt+1)] for x in range(len(coins)+1)]

    for y in range(amt+1):
        changes[0][y] = [[-1]]

    for x in range(1, len(coins)+1):
        for y in range(1, amt+1):
            if y < coins[x-1]:
                changes[x][y] = changes[x-1][y]
            else:
                withoutCoinX = changes[x-1][y]
                withCoinX = list(map(lambda e: concat(e, coins[x-1]), changes[x][y-coins[x-1]]))

                if withoutCoinX == [[-1]] and withCoinX == [[-1]]:
                    changes[x][y] = [[-1]]
                elif withoutCoinX == [[-1]]:
                    changes[x][y] = withCoinX
                elif withCoinX == [[-1]]:
                    changes[x][y] = withoutCoinX
                else:
                    changes[x][y] = withoutCoinX + withCoinX

    print(changes)

    return changes[len(coins)][amt]

print(coinChangeOptionsDp(36, [25,10,5,1]))
