from typing import List
import collections


class Solution:
    def __init__(self):
        self.nodeIndexes = dict()

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.preorder = collections.deque(preorder)
        for idx, node in enumerate(inorder):
            self.nodeIndexes[node] = idx

        return self.buildTreeHelper(0, len(inorder) - 1)

    def buildTreeHelper(self, minIdx, maxIdx):
        if minIdx > maxIdx:
            return None

        curRoot = self.preorder.popleft()
        curRootIdx = self.nodeIndexes.get(curRoot)

        treeNode = TreeNode(curRoot)

        treeNode.left = self.buildTreeHelper(minIdx, curRootIdx - 1)
        treeNode.right = self.buildTreeHelper(curRootIdx + 1, maxIdx)
        return treeNode
