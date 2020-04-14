class DoublyLinkedListNode():
    def __init__(self, n):
        self.val = n
        self.next = None
        self.prev = None
        self.count = 1


def restoreArray(pairs):
    nodes = dict()
    counter = dict()
    for pair in pairs:
        num1 = pair[0]
        num2 = pair[1]

        num1Node = None
        num2Node = None

        if num1 not in nodes:
            num1Node = DoublyLinkedListNode(num1)
            nodes[num1] = num1Node
        else:
            num1Node = nodes[num1]
            num1Node.count += 1

        if num2 not in nodes:
            num2Node = DoublyLinkedListNode(num2)
            nodes[num2] = num2Node
        else:
            num2Node = nodes[num2]
            num2Node.count += 1

        if num1Node.next is None and num2Node.prev is None:
            num1Node.next = num2Node
            num2Node.prev = num1Node
        elif num2Node.next is None and num1Node.prev is None:
            num2Node.next = num1Node
            num1Node.prev = num2Node
        else:
            if num1Node.next is None:
                node = num2Node
                while node is not None:
                    tempNode = node.prev
                    node.next = tempNode
                    node = tempNode
            elif num1Node.prev is None:
                node = num2Node
                while node is not None:
                    tempNode = node.next
                    node.prev = tempNode
                    node = tempNode
    returnList = []
    for node_val in nodes.keys():
        node = nodes.get(node_val)
        if node.count == 1 and node.prev is not None:
            while (node is not None):
                returnList.append(node.val)
                node = node.prev
    return returnList


pairs = [[5, 3], [1, 5], [7, 3], [4, 6], [2, 1], [2, 4]]
sampleOutput = [6, 4, 2, 1, 5, 3, 7]
dictionary = {1: [1, 4], 2: [4, 5], 3: [0, 2],
              4: [3, 5], 5: [0, 1], 6: [3], 7: [2]}

pairs2 = [[3, 5], [1, 4], [2, 4], [1, 5]]
sampleOutput2 = [3, 5, 1, 4, 2]

a = restoreArray(pairs)
print(a)
