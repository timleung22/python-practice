class WordBreak(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def breakWordMain(self, word):
        output = []
        if self.breakWord(word, output):
            return output
        else:
            return "Cannot break word"


    def breakWord(self, word, output):
        match = ""
        for i in range(len(word)+1):
            match = word[0:i]
            if match in self.dictionary:
                output.append(match)
                rest = word[i:]
                if len(rest) > 0:
                    restResult = self.breakWord(rest, output)
                    if not restResult:
                        output.remove(match)
                    else:
                        return True
                else:
                    return True

        return False


wb = WordBreak(["I", "am", "this", "is", "Super", "Man", "dog", "cat"])
print(wb.breakWordMain("SuperManisMe"))
print(wb.breakWordMain("thisdogisSuper"))
