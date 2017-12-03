
class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def bst(self):
        result = []
        queue = []
        queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
            result.append(node.value)

        return result

    def preOrder(self):
        result = []
        result.append(self.value)
        if self.left != None:
            for x in self.left.preOrder():
                result.append(x)
        if self.right != None:
            for x in self.right.preOrder():
                result.append(x)
        return result

    def inOrder(self):
        result = []
        if self.left != None:
            for x in self.left.inOrder():
                result.append(x)
        result.append(self.value)
        if self.right != None:
            for x in self.right.inOrder():
                result.append(x)
        return result

    def postOrder(self):
        result = []
        if self.left != None:
            for x in self.left.postOrder():
                result.append(x)
        if self.right != None:
            for x in self.right.postOrder():
                result.append(x)
        result.append(self.value)
        return result

    def printFullNodes(self):
        if self.left and self.right:
            print(self.value)

        if self.left:
            self.left.printFullNodes()
        if self.right:
            self.right.printFullNodes()

    def iterativePreOrder(self):
        traversed = []
        stack = []
        stack.append(self)
        while len(stack) > 0:
            popped = stack.pop(-1)
            traversed.append(popped.value)
            if popped.right:
                stack.append(popped.right)
            if popped.left:
                stack.append(popped.left)

        return traversed


    def printTree(self):
        # return an array demonstrating the BST
        result = []
        parents = []
        parents.append([self])
        while len(parents) != 0:
            parentsList = parents.pop(0)
            thisLevel = []
            nextLevelParents = []
            for i in range(len(parentsList)):
                parentNode = parentsList[i]
                thisLevel.append(parentNode.value)
                if parentNode.left != None:
                    nextLevelParents.append(parentNode.left)
                if parentNode.right != None:
                    nextLevelParents.append(parentNode.right)

            result.append(thisLevel)
            if len(nextLevelParents) > 0:
                parents.append(nextLevelParents)

        return result

    def isBstHelper(self, minValue, maxValue):
        retValue = False
        if self.value > minValue and self.value <= maxValue :
            retValue = True
        if self.left:
            retValue = retValue and self.left.isBstHelper(minValue, self.Value)
        if self.right:
            retValue = retValue and self.right.isBstHelper(self.value, maxValue)

        return retValue

    def sumOfLeavePaths(self, context, accSum):
        if self.left == None and self.right == None:
            #this is a leaf, return value
            return context+accSum
        else:
            if self.left:
                accSum = self.left.sumOfLeavePaths(context*10+self.left.value, accSum)
            if self.right:
                accSum = self.right.sumOfLeavePaths(context*10+self.right.value, accSum)

            return accSum

    def getSumOfLeaves(self):
        return self.sumOfLeavePaths(self.value, 0)


    def serializeHelper(self):
        vSerialized = []

        vSerialized.append(self.value)
        if self.left != None:
            vSerialized += self.left.serializeHelper()
        else:
            vSerialized.append("#")
        if self.right != None:
            vSerialized += self.right.serializeHelper()
        else:
            vSerialized.append("#")

        return vSerialized

    def serialize(self):
        result = ''
        serializedList = self.serializeHelper()
        for i, c in enumerate(serializedList):
            result += str(c)
            if i != len(serializedList) - 1:
                result += ','
        return result

    @staticmethod
    def deserialize(serialized):
        splittedValues = serialized.split(",")
        dVal = int(splittedValues.pop(0))
        dRoot = TreeNode(dVal)
        dRoot.left = TreeNode.deserializeHelper(splittedValues, dRoot)
        dRoot.right = TreeNode.deserializeHelper(splittedValues, dRoot)

        return dRoot

    @staticmethod
    def deserializeHelper(listOfValues, node):
        dVal = listOfValues.pop(0)
        if dVal == '#':
            return None
        else:
            dNode = TreeNode(dVal)
            dNode.left = TreeNode.deserializeHelper(listOfValues, dNode)
            dNode.right = TreeNode.deserializeHelper(listOfValues, dNode)
            return dNode

    def printTargetSumPathFromRoot(self, target, contextPath=[], goodPaths=[]):
        if self.value > target:
            return False

        if self.value == target:
            contextPath.append(self.value)
            goodPaths.append(str(contextPath))
            contextPath.pop(-1)
            return True

        if self.value < target and self.left == None and self.right == None:
            return False

        leftCheck = False
        rightCheck = False
        if self.left:
            contextPath.append(self.value)
            leftCheck = self.left.printTargetSumPathFromRoot(target-self.value, contextPath, goodPaths)
            contextPath.pop(-1)

        if self.right:
            contextPath.append(self.value)
            rightCheck = self.right.printTargetSumPathFromRoot(target-self.value, contextPath, goodPaths)
            contextPath.pop(-1)

        return leftCheck or rightCheck

    def pathTargetSum(self, target):
        paths = []
        self.printTargetSumPathFromRoot(target, goodPaths=paths)
        print(paths)



    def findTargetSum(self, target):
        if target < 0:
            return False

        if self.value == target:
            return True

        if self.left == None and self.right == None and self.value != target:
            return False

        foundTarget = False
        if self.left:
            foundTarget = self.left.findTargetSum(target-self.value) or self.left.findTargetSum(target)

        if self.right and foundTarget == False:
            foundTarget = self.right.findTargetSum(target-self.value) or self.right.findTargetSum(target)

        return foundTarget

    def toListOfList(self):
        result = []
        treeLevelStack = []
        treeLevelStack.append([self])
        while len(treeLevelStack) > 0:
            parents = treeLevelStack.pop(0)
            parentsValues = []
            nextTreeLevel = []
            for i in range(len(parents)):
                parentsValues.append(parents[i].value)
                if parents[i].left != None:
                    nextTreeLevel.append(parents[i].left)
                if parents[i].right != None:
                    nextTreeLevel.append(parents[i].right)
            if len(parentsValues) > 0:
                result.append(parentsValues)
            if len(nextTreeLevel) > 0:
                treeLevelStack.append(nextTreeLevel)
        return result


'''
root = TreeNode(17)
l1 = TreeNode(10)
r1 = TreeNode(25)
l11 = TreeNode(6)
l12 = TreeNode(13)
r11 = TreeNode(20)
r12 = TreeNode(34)
l111 = TreeNode(2)
l121 = TreeNode(15)
r111 = TreeNode(18)
r112 = TreeNode(22)

root.left = l1
root.right = r1
l1.left = l11
l1.right = l12
r1.left = r11
r1.right = r12
l11.left = l111
l12.left = l121
r11.left = r111
r11.right = r112

print(root.bst())
print(TreeNode.deserialize(root.serialize()).serialize())
'''
root = TreeNode(7)
left = TreeNode(1)
right = TreeNode(2)
leftleft = TreeNode(3)
leftright = TreeNode(1)
leftrightleft = TreeNode(5)
rightleft = TreeNode(9)
rightright = TreeNode(7)
rightleftright = TreeNode(6)
root.left = left
root.right = right
left.left = leftleft
left.right = leftright
leftright.left = leftrightleft
right.left = rightleft
right.right = rightright
rightleft.right = rightleftright

#713, 7115, 7296, 727
print(713+7115+7296+727)
print(root.getSumOfLeaves())
print(root.findTargetSum(14))
print(root.findTargetSum(6))
print(root.findTargetSum(523))
root.pathTargetSum(16)
print(root.findTargetSum(16))
print(root.findTargetSum(17))
print(root.toListOfList())

root.printFullNodes()

print(root.preOrder())
print(root.iterativePreOrder())