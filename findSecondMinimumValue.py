# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.treeElements = []
        self.inorder(root)
        if (len(self.treeElements) > 1):
            return self.treeElements[1]
        else:
            return -1

    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        if (len(self.treeElements) == 0):
            self.treeElements.append(root.val)
        else:
            for idx in range(len(self.treeElements)):
                if (self.treeElements[idx] == root.val):
                    break
                if len(self.treeElements) == idx + 1:
                    self.treeElements.append(root.val)
                    break
                if (self.treeElements[idx] > root.val):
                    self.treeElements.insert(idx, root.val)
                    break

        self.inorder(root.right)


a = TreeNode(5)
b = TreeNode(5)
c = TreeNode(8)

a.left = b
a.right = c

s = Solution()
s.findSecondMinimumValue(a)