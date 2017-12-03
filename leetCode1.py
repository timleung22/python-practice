class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumOfLeavePaths(root, root.val, 0)

    def sumOfLeavePaths(self, node, context, accSum):
        if node.left == None and node.right == None:
            return context + accSum
        if node.left:
            accSum = self.sumOfLeavePaths(node.left, context * 10 + node.left.val, accSum)
        if node.right:
            accSum = self.sumOfLeavePaths(node.right, context * 10 + node.right.val, accSum)

        return accSum


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()
print(s.sumNumbers(root))
