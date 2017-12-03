'''
def friendCircle(friends):
    n = len(friends)
    count = 0
    checkedSet = set()
    for i in range(n):
        if i not in checkedSet:
            count += 1
            dfs(i, n, friends, checkedSet)

    return count

def dfs(num, n, friends, checkedSet):
    for j in range(num+1, n):
        if friends[num][j] == "Y" and j not in checkedSet:
            checkedSet.add(j)
            dfs(j, n, friends, checkedSet)
'''


def friendCircle(friends):
    count = 0
    checkedSet = set()

    for eachP in range(len(friends)):
        if eachP not in checkedSet:
            count += 1
            checkedSet.add(0)
            dfs(eachP, friends, checkedSet)
    return count


def dfs(person, friends, checkedSet):
    for fIdx in range(len(friends[person])):
        if friends[person][fIdx] == "Y" and fIdx not in checkedSet:
            checkedSet.add(fIdx)
            dfs(fIdx, friends, checkedSet)


friends= [
    "YYNNN", "YYNYN", "NNYYN", "YYYYN", "NNNNY"
]
'''
friends= [
    "YNNNN", "NYNNN", "NNYNN", "NNNYN", "NNNNY"
]
'''
print(friendCircle(friends))