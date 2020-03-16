# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if node.next is not None or node.prev is not None:
            self.remove(node)  # TODO

        node.next = self.head
        if (self.head is not None):
            self.head.prev = node
        self.head = node

        if self.head.next is None:
            self.tail = self.head

    def setTail(self, node):
        # Write your code here.
        if node.next is not None or node.prev is not None:
            self.remove(node)  # TODO

        node.prev = self.tail
        if (self.tail is not None):
            self.tail.next = node
        self.tail = node

        if self.tail.prev is None:
            self.head = self.tail

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)  # TODO

        if (node.prev is not None):
            node.prev.next = nodeToInsert
            nodeToInsert.next = node
            node.prev = nodeToInsert
        else:
            self.setHead(nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)  # TODO

        if (node.next is not None):
            node.next.prev = nodeToInsert
            nodeToInsert.prev = node
            node.next = nodeToInsert
        else:
            self.setTail(nodeToInsert)

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)  # TODO

        currNode = self.head
        i = 0
        while (i < position):
            currNode = currNode.next
        self.insertBefore(currNode, nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        currNode = self.head
        while (currNode is not None):
            nextNode = currNode.next
            if (currNode.value == value):
                self.remove(currNode)
            currNode = nextNode

    def remove(self, node):
        # Write your code here.
        # remove from middle
        prevNode = node.prev
        nextNode = node.next

        if (prevNode is not None):
            prevNode.next = nextNode
        else:
            self.head = nextNode

        if (nextNode is not None):
            nextNode.prev = prevNode
        else:
            self.tail = prevNode

        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        currNode = self.head
        while (currNode is not None):
            nextNode = currNode.next
            if (currNode.value == value):
                return True
            currNode = nextNode
        return False

linkedList = DoublyLinkedList()
nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
linkedList.setHead(nodeA)
linkedList.setTail(nodeC)
linkedList.insertBefore(nodeC, nodeB)
print(linkedList)