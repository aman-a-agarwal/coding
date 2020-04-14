# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


null = None


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None

        dummy = Node(0)
        current = dummy
        nodeMap = dict()

        while (head is not None):
            if (head.val not in nodeMap):
                newNode = Node(head.val)
            else:
                newNode = nodeMap.get(head.val)

            if head.random is None:
                randomNode = None
            elif head.random.val not in nodeMap:
                randomNode = Node(head.random.val)
            else:
                randomNode = nodeMap.get(head.random.val)

            newNode.random = randomNode
            nodeMap[newNode.val] = newNode
            if randomNode is not None:
                nodeMap[randomNode.val] = randomNode

            current.next = newNode
            head = head.next
            current = current.next

        return dummy.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

a.random = c
b.random = None
c.random = e
d.random = a
e.random = d

s = Solution()
copyList = s.copyRandomList(a)

print(copyList)
