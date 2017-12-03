import sys


def makeCangeRecur(changeFor, coins):
    if changeFor == 0:
        return 1
    if changeFor < 0:
        return 0

    if len(coins) == 0:
        return 0

    return makeCangeRecur(changeFor-coins[0], coins) + makeCangeRecur(changeFor, coins[1:])

def makeChangeDp(changeFor, coins):

    solution = [[0 for x in range(changeFor+1)] for y in range(len(coins)+1)]
    for y in range(len(coins)+1):
        solution[y][0] = 1

    for y in range(1, len(coins)+1):
        for x in range(1, range(changeFor+1)):
            if coins[y] <= x:
                solution[y][x] = solution[y-1][x] + solution[y][x-coins[y-1]]
            else:
                solution[y][x] = solution[y-1][x]

    return solution[len(coins)][changeFor]

def miniumChange(amt, coins):
    solution = [0 for x in range(amt+1)]

    for toChange in range(1, amt+1):
        options = [sys.maxsize]
        for coin in coins:
            if toChange > coin:
                options.append(1 + solution[toChange-coin])
        solution[toChange] = min(options)

    return solution[amt]

def maxSubArraySum(array):
    solution = [-1 for i in range(len(array))]
    solution[0] = array[0]
    for i in range(1, len(array)):
        solution[i] = max(solution[i-1]+array[i], array[i])

    return max(solution)

def billboardMaxRev(billboards, revenue, distance, milesRes):
    mr = [0 for i in range(distance+1)]
    bIndex = 0
    mr[billboards[0]] = revenue[0]

    for i in range(1, distance+1):
        if bIndex < len(billboards):
            if billboards[bIndex] != i:
                mr[i] = mr[i-1]
            else:
                mr[i] = max(revenue[bIndex]+mr[i-milesRes], mr[i-1])
                bIndex += 1
        else:
            mr[i] = mr[i-1]
    return mr[distance]

print (billboardMaxRev([3,6,7,12,13,14], [3,4,6,5,4,1], 20, 6))

def cutRod(length, prices):
    mp = [0]*(length+1)
    for i in range(1, length+1):
        candidates = []
        for j in range(i):
            candidates.append(prices[j]+mp[i-j-1])

        mp[i] = max(candidates)
    return mp[length]

lookupMap = {"1":"a", "2":"b", "3":"c", "4":"d", "5":"e",
             "6":"f", "7":"g", "8":"h", "9":"i", "10":"j",
             "11":"k", "12":"l", "13":"m", "14":"n", "15":"o",
             "16":"p", "17":"q", "18":"r", "19":"s", "20":"t",
             "21":"u", "22":"v", "23":"w", "24":"x", "25":"y", "26":"z"
             }

def decipher(input):
    return decipherDp(input, {})

def decipherDp(input, dpCache):
    result = []
    if len(input) == 1 and input != "0":
        result.append(lookupMap.get(input))
    else:
        cached = dpCache.get(input, "")
        if cached != "":
            return cached

        if len(input) >= 2:
            first = input[0]
            firstTail = input[1:]
            if firstTail[0] != '0':
                firstDigitDecoded = decipher(first)[0]
                for eachDecoded in decipherDp(firstTail, dpCache):
                    result.append(firstDigitDecoded + eachDecoded)

            firstTwo = input[0:2]
            firstTwoTail = input[2:]
            if lookupMap.has_key(firstTwo) and (len(firstTwoTail) == 0 or (len(firstTwoTail) > 0 and firstTwoTail[0] != '0')):
                firstTwoDecoded = lookupMap.get(firstTwo)
                if len(firstTwoTail) > 0:
                    for eachDecoded in decipherDp(firstTwoTail, dpCache):
                        result.append(firstTwoDecoded + eachDecoded)
                else:
                    result.append(firstTwoDecoded)

    dpCache[input] = result
    return result

def findLargestContiguousSum(numbers):
    sums = [0 for x in range(len(numbers))]
    sums[0] = numbers[0]

    for i in range(1, len(numbers)):
        sums[i] = max(numbers[i], sums[i-1] + numbers[i])

    return max(sums)


