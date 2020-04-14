# Binary Tree Maximum Path Sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.maxVal = None

    def maxPathSum(self, rootNode: TreeNode) -> int:
        self.maxVal = rootNode.val
        self.maxPathHelper(rootNode)
        return self.maxVal

    def maxPathHelper(self, parentNode):
        if parentNode is None:
            return 0
        # Alternate 1: Using max function
        # leftNodeSum = max(self.maxPathHelper(parentNode.left), 0)
        # rightNodeSum = max(self.maxPathHelper(parentNode.right), 0)
        #
        # completeNodeSum = leftNodeSum + rightNodeSum + parentNode.val
        # self.maxVal = max(completeNodeSum, self.maxVal)
        # return max(leftNodeSum + parentNode.val, rightNodeSum + parentNode.val)

        # Alternate 2: without max function
        leftNodeSum = self.maxPathHelper(parentNode.left)
        rightNodeSum = self.maxPathHelper(parentNode.right)

        completeNodeSum = max(leftNodeSum + rightNodeSum + parentNode.val, leftNodeSum +
                              parentNode.val, rightNodeSum + parentNode.val, parentNode.val)
        self.maxVal = max(completeNodeSum, self.maxVal)
        return max(leftNodeSum + parentNode.val, rightNodeSum + parentNode.val, parentNode.val)


# Driver program
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)
print("Max path sum is ", Solution().maxPathSum(root))
