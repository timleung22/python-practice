class AbcPath(object):

    def __init__(self):
        pass

    def maxPath(self, input):
        candidates = [0]
        for i, eachLine in enumerate(input):
            for j, eachChar in enumerate(eachLine):
                if eachChar == 'A':
                    candidates.append(1+self.findPathLength(ord('B'), input, i, j))

        return max(candidates)

    def checkAndFindNext(self, target, matrix, row, col):
        if ord(matrix[row][col]) == target:
            if target == ord('Z'):
                return 1
            else:
                return 1+self.findPathLength(target+1, matrix, row, col)
        else:
            return 0

    def findPathLength(self, target, matrix, row, col):
        candidates = [0]
        if row > 0:
            if col > 0:
                candidates.append(self.checkAndFindNext(target, matrix, row - 1, col - 1))
            candidates.append(self.checkAndFindNext(target, matrix, row - 1, col))
            if col < len(matrix[0]) - 1:
                candidates.append(self.checkAndFindNext(target, matrix, row - 1, col + 1))

        if col > 0:
            candidates.append(self.checkAndFindNext(target, matrix, row, col - 1))
        if col < len(matrix[0]) - 1:
            candidates.append(self.checkAndFindNext(target, matrix, row, col + 1))

        if row < len(matrix) - 1:
            candidates.append(self.checkAndFindNext(target, matrix, row + 1, col))
            if col > 0:
                candidates.append(self.checkAndFindNext(target, matrix, row + 1, col - 1))
            if col < len(matrix[0]) - 1:
                candidates.append(self.checkAndFindNext(target, matrix, row + 1, col + 1))

        return max(candidates)


myTest = AbcPath()
pathLength = myTest.maxPath([
    "ABG",
    "CFE",
    "BDH",
    "ABC"
])

print(pathLength)