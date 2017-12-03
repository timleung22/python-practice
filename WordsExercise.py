def findMatchings(words):
    matchKeys = {}

    for eachWord in words:
        sortedWord = ''.join(sorted((set(eachWord.lower()))))
        sortedWordMatch = matchKeys.get(sortedWord, [])
        sortedWordMatch.append(eachWord)
        matchKeys[sortedWord] = sortedWordMatch

    for eachKey in matchKeys.keys():
        print(matchKeys[eachKey])

def permutateStr(input):
    result = set()
    if len(input) == 1:
        result.add(input)
    else:
        result = result.union(weave(input[0], permutateStr(input[1:])))
    return result

def weave(weavingChar, weaveSet):
    weaved = set()
    for eachToWeave in weaveSet:
        for i in range(len(eachToWeave)):
            weaved.add(eachToWeave[0:i]+weavingChar+eachToWeave[i:])
        weaved.add(eachToWeave+weavingChar)
    return weaved

class Abba:
    def canObtain(self, initial, target):
        if initial == target:
            return "Possible"
        elif len(target) == len(initial) and target != initial:
            return "Impossible"
        else:
            if target[-1] == 'B':
                return self.canObtain(initial, (target[0:-1])[::-1])
            elif target[-1] == 'A':
                return self.canObtain(initial, target[0:-1])
            else:
                return 'Impossible'

