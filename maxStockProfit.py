def maxStockProfit(prices):
    changes = []
    for i in range(len(prices)):
        if i == 0:
            changes.append(0)
        else:
            changes.append(prices[i] - prices[i-1])

    return findMaxProfit(changes)

def findMaxProfit(changes):

    mp = [0 for i in range(len(changes)+1)]
    for i in range(1, len(changes)+1):
        mp[i] = max(mp[i-1]+changes[i-1], changes[i-1])

    return max(mp)

print(maxStockProfit([1,12,7,0,23,11,52,31,61,69,70,2]))

def longestIncreasingSubsequence(arr):

    lis = [0 for i in range(len(arr)+1)]
    for i in range(1, len(arr)+1):
        candidates = []
        for j in range(1, i-1):
            if arr[j-1] < arr[i]:
                candidates.append(lis[j])