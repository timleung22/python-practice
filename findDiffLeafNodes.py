'''
Given 2 arrays that represent the PreOrder traversal of 2 BSTs.
Find the first pair of leaf node that don't match.
'''
def findLeafNodes(preOrderTraversed):
    leafs = []
    # the first element must be Root.
    # the left subtree follows.  The right subtree begins at the element with
    # value > first element (root)
    if len(preOrderTraversed) == 1:
        leafs += preOrderTraversed
    else:
        left = []
        right = []
        for i in range(1, len(preOrderTraversed)):
            if preOrderTraversed[i] <= preOrderTraversed[0]:
                left.append(preOrderTraversed[i])
            else:
                right.append(preOrderTraversed[i])
        if len(left) > 0:
            leafs += findLeafNodes(left)
        if len(right) > 0:
            leafs += findLeafNodes(right)
    return leafs

def find1stPairDiffLeafs(tree1, tree2):
    #I am just returning the index now
    leafs1 = findLeafNodes(tree1)
    leafs2 = findLeafNodes(tree2)

    for i in range(min(len(leafs1), len(leafs2))):
        if leafs1[i] != leafs2[i]:
            return i

    if i == len(leafs1) and i == len(leafs2):
        return -1
    else:
        return i



