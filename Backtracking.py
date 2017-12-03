class BreakWord(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def breakWord(self, word):
        answer = []
        lookup = set()
        if self.breakWordDp(word, answer, lookup):
            answer.reverse()
            return answer
        else:
            return [word, "Cannot be broken"]

    def breakWordDp(self, word, answer, lookup):
        if len(word) == 0:
            return True

        if word in lookup:
            return False

        i = 1
        while i <= len(word):
            toMatch = word[0:i]

            if toMatch in self.dictionary:
                if self.breakWordDp(word[i:], answer, lookup) == True:
                    answer.append(toMatch)
                    return True
                else:
                    i += 1
            else:
                i += 1

        lookup.add(word)
        return False


test = BreakWord({"this", "is", "dog", "ice", "super", "like", "man"})
print(test.breakWord("supermanlikethisdog"))
print(test.breakWord("thisdogeatsicecream"))