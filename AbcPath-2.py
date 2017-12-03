class AbcPath(object):

    def longest(self, grid):
        lengthsFound = [0]
        for row, eachRow in enumerate(grid):
            for col in range(len(eachRow)):
                if eachRow[col] == 'A':
                    lengthsFound.append(1+self.findMaxPathLength(grid, row, col, ord("B"), len(grid), len(eachRow)))

        return max(lengthsFound)

    def getPathLength(self, grid, rowIndex, charIndex, target, nRows, nChars):
        if target == ord("Z"):
            return 1
        else:
            return 1 + self.findMaxPathLength(grid, rowIndex, charIndex, target+1, nRows, nChars)

    def findMaxPathLength(self, grid, row, col, target, nRows, nCols):
        pathLengths = [0]
        if row-1 >= 0:
            rowFromGrid = grid[row-1]
            if col-1 >= 0 and ord(rowFromGrid[col-1]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col-1, target, nRows, nCols))
            if ord(rowFromGrid[col]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col, target, nRows, nCols))
            if col+1 < nCols and ord(rowFromGrid[col+1]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col+1, target, nRows, nCols))

        rowFromGrid = grid[row]
        if col - 1 >= 0 and ord(rowFromGrid[col - 1]) == target:
            pathLengths.append(self.getPathLength(grid, row - 1, col - 1, target, nRows, nCols))
        if col + 1 < nCols and ord(rowFromGrid[col + 1]) == target:
            pathLengths.append(self.getPathLength(grid, row - 1, col + 1, target, nRows, nCols))

        if row+1 < nRows:
            rowFromGrid = grid[row+1]
            if col-1 >= 0 and ord(rowFromGrid[col-1]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col-1, target, nRows, nCols))
            if ord(rowFromGrid[col]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col, target, nRows, nCols))
            if col+1 < nCols and ord(rowFromGrid[col+1]) == target:
                pathLengths.append(self.getPathLength(grid, row-1, col+1, target, nRows, nCols))

        return max(pathLengths)
