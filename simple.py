def findPairs(x, K):

    pairs = 0
    cache = {}

    for eachV in x:
        if (K-eachV) in cache:
            pairs += cache[(K-eachV)]
        if eachV in cache.keys():
            cache[eachV] += 1
        else:
            cache[eachV] = 1

    return pairs

print(findPairs([], 10))
print(findPairs([-1,1,0], 0))
print(findPairs([1,1,1], 2))
