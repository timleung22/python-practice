CHARS = 26

def isValid(count, k):
    val = 0
    for i in range(CHARS):
        if count[i] > 0:
            val += 1
    return k >= val

def kUniques(s, k):
    uniques = set()
    for eachC in s:
        uniques.add(eachC)

    if len(uniques) < k:
        print("Not enough unique chars")
        return

    currStart = 0
    currEnd = 0
    maxWindowSize = 1
    maxWindowStart = 0

    count = [0 for i in range(CHARS)]
    count[ord(s[0]) - ord('a')] += 1
    for i in range(1, len(s)):
        count[ord(s[i]) - ord('a')] += 1
        currEnd += 1

        while not isValid(count, k):
            count[ord(s[currStart]) - ord('a')] -= 1
            currStart += 1

        if currEnd - currStart + 1 > maxWindowSize:
            maxWindowSize = currEnd - currStart + 1
            maxWindowStart = currStart

    print("Max substring is " + s[maxWindowStart:])

kUniques('aabacbebebe', 3)