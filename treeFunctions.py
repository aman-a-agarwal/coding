class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def isValidBST(self, root: TreeNode) -> bool:
        if (root is None):
            return True
        self.treeList = []
        self.inorderTraversal(root)
        for ele in range(1,len(self.treeList)):
            if (self.treeList[ele-1] >= self.treeList[ele]):
                return False
        return True

    def inorderTraversal (self, root):
        if (root is None):
            return

        self.inorderTraversal(root.left)
        self.treeList.append(root.val)
        self.inorderTraversal(root.right)

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

    def isValidBST3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        self.preOrderList = []
        self.postOrderList = []

        def preOrder(root):
            if (root is not None):
                self.preOrderList.append(None)
                return

            preOrder(root.left)
            self.preOrderList.append(root.val)
            preOrder(root.right)

        def postOrder(root):
            if (root is not None):
                self.postOrderList.append(None)
                return

            preOrder(root.right)
            self.postOrderList.append(root.val)
            preOrder(root.left)

        preOrder(root)
        postOrder(root)

        for idx in range(len(self.preOrderList)):
            if (self.preOrderList[idx] != self.postOrderList[idx]):
                return False

        return True



r = Tree()

a = TreeNode(1)
c = TreeNode(2)
d = TreeNode(2)
e = TreeNode(3)
f = TreeNode(3)


a.left = c
a.right = d
c.left = None
c.right = e
d.left = None
d.right = f

print(r.isSymmetric(a))