def moveZerosToRight(arrayOfNumbers):

    for tail in range(len(arrayOfNumbers)-1, 0, -1):
        if arrayOfNumbers[tail] != 0:
            break

    for head in range(0, tail):
        if arrayOfNumbers[head] == 0:
            arrayOfNumbers[head] = arrayOfNumbers[tail]
            arrayOfNumbers[tail] = 0
            for i in range(tail-1, head, -1):
                if arrayOfNumbers[i] != 0:
                    break
            tail = i
    return arrayOfNumbers

def removeOddNumbers(input):
    firstEven = -1

    for i in range(len(input)-1, -1, -1):
        if input[i] % 2 == 0:
            firstEven = i
            break

    if firstEven == -1:
        return []

    for i in range(firstEven-1, -1, -1):
        if input[i] % 2 != 0:
            temp = input[firstEven]
            input[firstEven] = input[i]
            input[i] = temp
            firstEven -= 1

    return input[0: firstEven+1]

def findLargestContiguousSequence(numbers):
    maxSum = numbers[0]
    runningSum = numbers[0]
    startIdx = 0
    endIdx = 0
    maxStart = 0

    for i, number in enumerate(numbers):
        runningSum += number
        if runningSum > maxSum:
            maxSum = runningSum
            maxStart = startIdx
            endIdx = i

        if runningSum < 0:
            runningSum = number
            startIdx = i
            endIdx = i

    return (maxStart, endIdx, maxSum)

def findMostAmazingNumbers(input):
    startIdxMap = {}
    size = len(input)

    for i in range(size):
        val = input[i]
        if val < size:
            for s in range(size):
                if val <= ((size+i-s) % size):
                    startIdxMap[s] += 1

    maxAmazingNumber = 0
    startIdx = 0
    for i in range(size):
        if startIdxMap[i] > maxAmazingNumber:
            startIdx = i
            maxAmazingNumber = startIdxMap[i]

    return startIdx

def findKthLargest(inputArr, kth):
    if kth >= len(inputArr):
        raise ValueError

    if len(inputArr) == 1:
        return inputArr[0]

    larger = []
    smaller = []
    pivot = inputArr[0]

    for eachInput in inputArr:
        if eachInput > pivot:
            larger.append(eachInput)
        else:
            smaller.append(eachInput)

    if kth < len(larger):
        return findKthLargest(larger, kth)
    elif kth == len(larger):
        return smaller[0]
    else:
        return findKthLargest(smaller[1:], kth-len(larger)-1)

