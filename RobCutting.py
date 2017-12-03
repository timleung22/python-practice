def rodCutting(prices, length):

    profits = [0 for i in range(length+1)]
    for i in range(1, length+1):
        possibilities = [0]
        for j in range(0, i):
            possibilities.append(prices[j]+profits[i-j-1])

        profits[i] = max(possibilities)

    return profits[length]

print(rodCutting([2,3,7,8,9], 5))