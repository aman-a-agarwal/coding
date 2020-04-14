from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.generateBST(nums)

    def generateBST(self, nums):
        if len(nums) == 0:
            return None

        start = 0
        end = len(nums)
        mid = (start + end) // 2

        curNode = TreeNode(nums[mid])

        # Indexing was a key issue to understand here.
        # Note that in python, List[start:end] => [start position: end position - 1],
        # i.e end index is not inclusive

        curNode.left = self.generateBST(nums[start:mid])
        curNode.right = self.generateBST(nums[mid + 1:end + 1])

        return curNode
