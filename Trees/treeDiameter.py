# Given a binary tree, you need to compute the length of the diameter of the tree. ]
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
#
# This path may or may not pass through the root.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sub_path = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameterHelper(root)
        return self.max_sub_path

    def diameterHelper(self, root):
        if root is None:
            return -1

        left_depth = 1 + self.diameterHelper(root.left)
        right_depth = 1 + self.diameterHelper(root.right)

        self.max_sub_path = max(self.max_sub_path, left_depth + right_depth)

        return max(left_depth, right_depth)
