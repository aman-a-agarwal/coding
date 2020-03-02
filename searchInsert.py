"""

Data Structures classes

"""

class List:
    def __init__(self, *args):
        pass


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class RecursiveFunctions:

    """
    r = RecursiveFunctions()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)


    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    """
    def __init__(self):
        pass

    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(startindex, endindex, s):
            if ((endindex - startindex) <= 0):
                return

            c = s[endindex]
            s[endindex] = s[startindex]
            s[startindex] = c

            helper(startindex+1, endindex-1, s)

        s = helper(0, len(s) - 1, s)

    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head


        def swap(previous):
            if (previous.next is None or previous.next.next is None):
                return

            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first

            previous.next = second
            swap(first)

        swap(dummy)
        return dummy.next

    def swapPairs2(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        while previous.next != None and previous.next.next:
            node1 = previous.next
            node2 = previous.next.next
            previous.next = node2
            node1.next = node2.next
            node2.next = node1
            previous = node1

        return dummy.next

    def getPascalRow(self, rowIndex: int):
        result_hash = {}

        def generate(i, j):
            if (i == j or j == 1):
                return 1
            if ((str(i) + str(j)) in result_hash):
                return result_hash[str(i) + str(j)]
            else:
                result_hash[str(i) + str(j)] = generate(i - 1, j - 1) + generate(i - 1, j)
            return result_hash[str(i) + str(j)]

        res = []

        for k in range(rowIndex + 1):
            res.append(generate(rowIndex + 1, k + 1))

        return res


    """
    Reverse a singly linked list.
    
    A linked list can be reversed either iteratively or recursively. Could you implement both?
    """

    def reverseList(self, head: ListNode) -> ListNode:

        _prev = None
        _cur = head

        def reverse(_prev, _cur):
            if (_cur.next == None):
                return _cur

            _next = _cur.next
            _cur.next = _prev

            return reverse(_cur, _next)

        return reverse(_prev, _cur)

    # TODO
    def permutationString (self, s, prefix):
        if len(s) == 0:
            print(prefix)
        else:
            for i in range(len(s)):
                rem = s[0:i] + s[(i+1):]
                self.permutationString(rem, prefix + s[i])

r = RecursiveFunctions()

a = ListNode(0)
b = ListNode(0)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)


# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f









