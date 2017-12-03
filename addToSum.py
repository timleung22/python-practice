def addToSum(denoms, target):
    sums = set([0])

    for sum in range(denoms[0], target+1):
        for eachD in denoms:
            if sum - eachD in sums and sum not in sums:
                sums.add(sum)

    print(sorted(sums))
        #if (sum - denoms[0]) in sums or (sum - denoms[1]) in sums or (sum - denoms[2]) in sums:
        #    sums.add(sum)
        #    print(sum)

#addToSum([10, 15, 55], 1000)

def climbStairs(steps):
    sol = [0 for i in range(steps+1)]

    for i in range(1, steps+1):
        if i >= 3:
            sol[i] = sol[i-3]+sol[i-2]+sol[i-1]+1
        elif i >= 2:
            sol[i] = sol[i-2]+sol[i-1]+1
        else:
            sol[i] = sol[i-1]+1

    return sol[steps]

def subsetSum(arr, target):
    ss = [[False for j in range(target+1)] for i in range(len(arr)+1)]
    for i in range(1,len(arr)+1):
        ss[i][0] = True

    for i in range(1, len(arr)+1):
        for j in range(1, target+1):
            if j >= arr[i-1]:
                ss[i][j] = ss[i-1][j] or ss[i][j-arr[i-1]]
            else:
                ss[i][j] = ss[i-1][j]

    return ss[len(arr)][target]

print(subsetSum([3,2,7,10,14,15], 22))


#print(climbStairs(8))