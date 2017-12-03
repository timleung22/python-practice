nMap = {
    "1":"a","2":"b","3":"c","4":"d","5":"e",
    "6":"f","7":"g","8":"h","9":"i","10":"j",
    "11":"k", "12":"l", "13":"m", "14":"n", "15":"o",
    "16":"p", "17":"q", "18":"r", "19":"s", "20":"t",
    "21":"u","22":"v","23":"w","24":"x","25":"y","26":"z"
}

def numToLetter(number):
    result = []
    if len(number) == 0 or number[0] == '0':
        return result

    if len(number) == 1:
        result.append(nMap[number])
        return result

    if number[1] != '0':
        subResult = numToLetter(number[1:])
        for eachSubResult in subResult:
            result.append(nMap[number[0]]+eachSubResult)

    if number[0:2] in nMap.keys() and number[2] != '0':
        subResult = numToLetter(number[2:])
        for eachSubResult in subResult:
            result.append(nMap[number[0:2]]+eachSubResult)

    return result

'''
Given an encoded string 3[ab2[3[cd][4[g]]]] ], it should return
abcdcdcdggggcdcdcdggggabcdcdcdggggcdcdcdggggabcdcdcdggggcdcdcdgggg
'''
class EncodedString:
    def __init__(self, str):
        self.encoded = str

    def decode(self):
        stack = []
        contextNum = 0
        contextStr = ""
        decoded = ""
        for c in self.encoded:
            if c.isdigit():
                contextNum = contextNum*10+int(c)
            elif c == "[":
                if contextNum == 0:
                    contextNum = 1
                stack.append((contextNum, contextStr))
                contextNum = 0
                contextStr = ""
            elif c == "]":
                context = stack.pop(-1)
                str = contextStr * context[0]
                str = context[1]+str
                contextStr = str

            else:
                contextStr = contextStr + c

        return contextStr


encoded = EncodedString("ab2[e3[cd]]fg")
print(encoded.decode())
print(numToLetter("11227"))