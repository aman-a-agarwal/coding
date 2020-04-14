import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.parents = dict()

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        # Build a hashmap of parents <Int, TreeNode>
        self.dfs(root, None)

        level = 0
        q = collections.deque([(target, level)])

        seen = [target.val]
        while len(q) > 0:
            if q[0][1] == K:
                return [x[0].val for x in q]

            ele, level = q.popleft()

            for connectedNode in [ele.left, ele.right,
                                  self.parents.get(ele.val)]:
                if connectedNode is not None and connectedNode.val not in seen:
                    seen.append(connectedNode.val)
                    q.append((connectedNode, level + 1))

            # Edge case where K is bigger than any path in the tree/graph
            if len(q) == 0:
                return []

    def dfs(self, node, parentNode):
        if node is None:
            return

        if parentNode is not None:
            self.parents[node.val] = parentNode

        self.dfs(node.left, node)
        self.dfs(node.right, node)


treeRoot = TreeNode(3)
_5 = TreeNode(5)
_1 = TreeNode(1)
_6 = TreeNode(6)
_2 = TreeNode(2)
_0 = TreeNode(0)
_8 = TreeNode(8)
_7 = TreeNode(7)
_4 = TreeNode(4)

treeRoot.left = _5
treeRoot.right = _1

_5.left = _6
_5.right = _2

_2.left = _7
_2.right = _4

_1.left = _0
_1.right = _8


print(Solution().distanceK(treeRoot, _5, 3))
