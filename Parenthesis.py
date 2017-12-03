def replaceAsterisk(source):
    replaced = set()
    idx = source.find('*')
    if idx != -1:
        prefix = source[0:idx]
        replaced = replaced.union(replaceAsterisk(prefix+source[idx+1:]))
        replaced = replaced.union(replaceAsterisk(prefix+"("+source[idx+1:]))
        replaced = replaced.union(replaceAsterisk(prefix+")"+source[idx+1:]))
    else:
        replaced.add(source)

    return replaced

def applyTransformation(inputSet, mergeWith):
    outputSet = []
    while len(inputSet) > 0:
        inputStr = inputSet.pop(0)
        outputSet.append(inputStr+mergeWith)
        outputSet.append(inputStr+"("+mergeWith)
        outputSet.append(inputStr+")"+mergeWith)

    return outputSet

def checkValidParentheses(expression):
    stack = []
    for i in range(len(expression)):
        ch = expression[i]
        if ch == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop(0)
        else:
            stack.append(ch)

def countValidParenthesesAfterTransformation(input):
    count = 0
    for x in replaceAsterisk(input):
        if checkValidParentheses(x):
            count += 1

    return count

