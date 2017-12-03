class EditDistance(object):

    def __init__(self):
        pass

    def getDistance(self, word1, word2):
        solutions = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]

        # if word1 is empty, then we add the number of characters in each possible length of word2
        for i in range(len(word2)+1):
            solutions[i][0] = i

        # conversely, the same solution when word2 is empty.
        for i in range(len(word1)+1):
            solutions[0][i] = i

        for j in range(1, len(word1)+1):
            for i in range(1, len(word2)+1):
                if word1[j-1] == word2[i-1]:
                    solutions[i][j] = solutions[i-1][j-1]
                else:
                    solutions[i][j] = 1 + min(solutions[i][j-1],
                                          solutions[i-1][j],
                                          solutions[i-1][j-1])

        return solutions[len(word2)][len(word1)]

solution = EditDistance()
print(solution.getDistance('hello', 'jellyfish'))