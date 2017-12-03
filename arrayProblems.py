def findKthLargest(inputArr, index):
    if index >= len(inputArr):
        raise ValueError

    pivot = inputArr[0]
    if len(inputArr) == 1:
        return pivot

    smaller = []
    larger = []
    for num in inputArr:
        if num > pivot:
            larger.append(num)
        else:
            smaller.append(num)

    if index == len(larger):
        return pivot

    if index < len(larger):
        return findKthLargest(larger, index)
    else:
        return findKthLargest(smaller[1:], index-len(larger)-1)

kthLargest = findKthLargest([5,4,9,7,18,16,11,10,3,2,0], 7)
print(kthLargest)

def moveZeros(input):
    # move from the end of the array to find the first non-zero spot
    start = 0
    for end in range(len(input), 0, -1):
        if input[end-1] != 0:
            for begin in range(start, end-1):
                if input[begin] == 0:
                    input[begin] = input[end-1]
                    input[end-1] = 0
                    start = begin


input = [1,0,2,3,0,4,5,0]
moveZeros(input)
print(input)
input = [0,1,1,1,0,0,0,2]
moveZeros(input)
print(input)

def findStockGain(stockQuotes):
    deltas = [0]
    for i in range(1, len(stockQuotes)):
        deltas.append(stockQuotes[i]-stockQuotes[i-1])

    maxGain = 0
    currentGain = 0
    for i in range(len(deltas)):
        if deltas[i] >= 0:
            currentGain += deltas[i]
        else:
            if currentGain > maxGain:
                maxGain = currentGain
            currentGain = 0
    return maxGain

print(findStockGain([17, 23, 20, 15, 25, 30, 33, 40, 38, 42, 42]))

def checkIfTwoArraysMatch(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    result = True
    check = arr2.copy()
    for each1 in arr1:
        result = result and (each1 in check)
        check.remove(each1)

    return result


a = [1,3,1,3,5,7]
b = [7,5,1,3,3,1]
print(checkIfTwoArraysMatch(a, b))
print(a)
print(b)