def mergeSort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    mid = len(unsorted) // 2
    left = unsorted[0: mid]
    right = unsorted[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)


def merge(left, right):
    new_length = len(left) + len(right)
    merged = []
    leftPointer = 0
    rightPointer = 0

    while leftPointer < len(left) and rightPointer < len(right):
        leftEle = left[leftPointer]
        rightEle = right[rightPointer]

        if leftEle < rightEle:
            merged.append(leftEle)
        else:
            merged.append(rightEle)

    if leftPointer > len(left) and rightPointer < len(right):
        merged = merge + right[rightPointer:]

    if leftPointer < len(left) and rightPointer > len(right):
        merged = merge + left[leftPointer:]

    return merged

