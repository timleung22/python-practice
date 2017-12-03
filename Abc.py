'''
Problem ABC from TopCoder
'''
class ABC(object):
    def __init__(self):
        pass

    def createABCString(self, sLen, nPairs):
        vPairs = 0
        for k in range(sLen):
            for m in range(k+1, sLen):
                for n in range(k+1, sLen):
                    if m != n:
                        vPairs = 2*sLen-2*k-2*m-2*n
                        print(k, m, n, vPairs)

    def createString(self, strLength, nPairs):
        return self.createStringBruteForce(strLength, nPairs)

    def createStringBruteForce(self, strLength, nPairs):
        resultSet = self.generateStr(strLength)
        for eachResult in resultSet:
            if self.findPairs(eachResult) == nPairs:
                return eachResult

        return ""

    def generateStr(self, strLen):
        if strLen == 1:
            return ["A", "B", "C"]
        result = []
        for s in ["A", "B", "C"]:
            for eachStr in self.generateStr(strLen-1):
                result.append(s+eachStr)
        return result

    def findPairs(self, str):
        count = 0
        for i in range(len(str)):
            for j in range(i+1, len(str)):
                if str[i] < str[j]:
                    count +=1
        return count

    