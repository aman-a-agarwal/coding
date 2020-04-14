# Time Complexity: O(n)


def moveElementToEnd(array, toMove):
    # Write your code here.
    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer < rightPointer:
        if array[leftPointer] == toMove:
            while array[rightPointer] == toMove and rightPointer > leftPointer:
                rightPointer -= 1
            array[leftPointer], array[rightPointer] = array[rightPointer], array[leftPointer]
        leftPointer += 1
    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
moveElementToEnd(array, toMove)
