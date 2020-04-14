import unittest


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

        if node is None:
            self.setTail(nodeToInsert)
        elif node.prev is not None:
            node.prev.next = nodeToInsert
            nodeToInsert.prev = node.prev
            node.prev = nodeToInsert
            nodeToInsert.next = node
        else:
            self.setHead(nodeToInsert)

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)  # TODO

        if node is None:
            self.setHead(nodeToInsert)
        elif node.next is not None:
            node.next.prev = nodeToInsert
            nodeToInsert.next = node.next
            node.next = nodeToInsert
            nodeToInsert.prev = node
        else:
            self.setTail(nodeToInsert)

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if nodeToInsert.next is not None or nodeToInsert.prev is not None:
            self.remove(nodeToInsert)  # TODO

        if position == 1:
            self.setHead(nodeToInsert)
            return

        currNode = self.head
        i = 1
        while i < position and currNode is not None:
            currNode = currNode.next
            i += 1
        if i == position:
            self.insertBefore(currNode, nodeToInsert)
        else:
            # If the mentioned position is more than the elements in linked list
            # Add the element at the end
            self.setTail(nodeToInsert)

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

        if prevNode is not None:
            prevNode.next = nextNode
        else:
            self.head = nextNode

        if nextNode is not None:
            nextNode.prev = prevNode
        else:
            self.tail = prevNode

        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        currNode = self.head
        while currNode is not None:
            nextNode = currNode.next
            if currNode.value == value:
                return True
            currNode = nextNode
        return False


class TestDoublyLinkedList(unittest.TestCase):

    def test_set_header(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        linkedList.setHead(nodeA)
        self.assertEqual(linkedList.head.value == 1, True)
        self.assertEqual(linkedList.tail.value == 1, True)
        self.assertEqual(linkedList.head.next is None, True)

    def test_set_tail(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        linkedList.setTail(nodeA)
        self.assertEqual(linkedList.head.value == 1, True)
        self.assertEqual(linkedList.tail.value == 1, True)
        self.assertEqual(linkedList.tail.prev is None, True)

    def test_insert_before(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)
        linkedList.setHead(nodeA)
        self.assertEqual(linkedList.tail.prev is None, True)
        linkedList.setTail(nodeC)
        self.assertEqual(linkedList.tail.prev is None, False)
        linkedList.insertBefore(nodeC, nodeB)
        self.assertEqual(linkedList.head is None, False)

        self.complete_linked_list_test(linkedList, nodeA, nodeB, nodeC)

        linkedList.insertBefore(nodeA, nodeB)

        self.complete_linked_list_test(linkedList, nodeB, nodeA, nodeC)

    def test_insert_after(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)
        linkedList.setHead(nodeA)
        self.assertEqual(linkedList.tail.prev is None, True)
        linkedList.setTail(nodeB)
        self.assertEqual(linkedList.tail.prev is None, False)
        linkedList.insertAfter(nodeB, nodeC)
        self.assertEqual(linkedList.head is None, False)

        self.complete_linked_list_test(linkedList, nodeA, nodeB, nodeC)

    def test_insert_at_position(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)
        linkedList.setHead(nodeA)
        self.assertEqual(linkedList.tail.prev is None, True)
        linkedList.setTail(nodeC)
        self.assertEqual(linkedList.tail.prev is None, False)
        linkedList.insertAtPosition(2, nodeB)

        self.assertEqual(linkedList.head is None, False)

        self.complete_linked_list_test(linkedList, nodeA, nodeB, nodeC)

        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)

        # should be set as tail
        linkedList.insertAtPosition(1, nodeB)
        # should be set as head
        linkedList.insertAtPosition(2, nodeA)
        # should be set as tail
        linkedList.insertAtPosition(4, nodeC)

        self.assertEqual(linkedList.head is None, False)

        self.complete_linked_list_test(linkedList, nodeB, nodeA, nodeC)

    def test_remove(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)

        linkedList.insertAtPosition(1, nodeA)
        self.assertEqual(linkedList.tail is nodeA, True)
        self.assertEqual(linkedList.head is nodeA, True)

        linkedList.insertAfter(nodeA, nodeB)
        self.assertEqual(linkedList.head.next is nodeB, True)
        self.assertEqual(linkedList.tail is nodeB, True)

        linkedList.insertAfter(nodeB, nodeC)
        self.assertEqual(linkedList.head.next is nodeB, True)
        self.assertEqual(linkedList.tail is nodeB, False)

        linkedList.remove(nodeB)
        self.assertEqual(linkedList.head.next is nodeC, True)
        self.assertEqual(linkedList.tail is nodeB, False)

        linkedList.remove(nodeA)
        self.assertEqual(linkedList.head.next is nodeC, False)
        self.assertEqual(linkedList.tail is nodeB, False)
        self.assertEqual(linkedList.tail is nodeC, True)
        self.assertEqual(linkedList.head is nodeC, True)

        linkedList.insertAtPosition(1, nodeB)
        self.assertEqual(linkedList.tail is nodeB, False)
        self.assertEqual(linkedList.tail is nodeC, True)
        self.assertEqual(linkedList.head is nodeB, True)

        linkedList.insertBefore(nodeB, nodeA)
        self.assertEqual(linkedList.tail is nodeB, False)
        self.assertEqual(linkedList.tail is nodeC, True)
        self.assertEqual(linkedList.head is nodeA, True)

        # Remove Node A
        linkedList.removeNodesWithValue(1)
        self.assertEqual(linkedList.head.next is nodeC, True)
        self.assertEqual(linkedList.tail is nodeB, False)
        self.assertEqual(linkedList.tail is nodeC, True)
        self.assertEqual(linkedList.head is nodeB, True)

        linkedList.removeNodesWithValue(2)
        self.assertEqual(linkedList.head.next is nodeC, False)
        self.assertEqual(linkedList.tail is nodeB, False)
        self.assertEqual(linkedList.tail is nodeC, True)
        self.assertEqual(linkedList.head is nodeC, True)

    def test_node_exists(self):
        linkedList = DoublyLinkedList()
        nodeA = Node(1)
        nodeB = Node(2)
        nodeC = Node(3)

        linkedList.insertAtPosition(1, nodeA)
        self.assertEqual(linkedList.tail is nodeA, True)
        self.assertEqual(linkedList.head is nodeA, True)
        self.assertEqual(linkedList.containsNodeWithValue(1), True)

    def complete_linked_list_test(self, linkedList, first, second, third):
        # Forward Direction Tests
        self.assertEqual(linkedList.head is first, True)
        self.assertEqual(linkedList.head.next is second, True)
        self.assertEqual(linkedList.head.next.next is third, True)

        # Backward Direction Tests
        self.assertEqual(linkedList.tail is third, True)
        self.assertEqual(linkedList.tail.prev is second, True)
        self.assertEqual(linkedList.tail.prev.prev is first, True)


if __name__ == '__main__':
    unittest.main()
