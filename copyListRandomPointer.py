# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

null = None

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if (head == null):
            return null;
        dummy = Node(0)
        current = dummy
        nodeMap = dict()

        while (head != null):
            if (head not in nodeMap.keys()):
                newNode = Node(head.val)
                nodeMap[head] = newNode
            else:
                newNode = nodeMap.get(head)

            if (head.random != null):
                if (head.random not in nodeMap.keys()):
                    newNode.random = Node(head.random.val)
                    nodeMap[head.random] = newNode.random
                else:
                    newNode.random = nodeMap.get(head.random)
            else:
                newNode.random = null

            current.next = newNode
            current = newNode
            head = head.next

        return dummy.next