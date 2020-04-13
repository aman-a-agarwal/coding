def selectionSort(array):
    # Write your code here.
    for outer in range(len(array)):
        smallestIdx = outer
        for inner in range(outer, len(array)):
            if array[inner] <= array[smallestIdx]:
                smallestIdx = inner
        array[smallestIdx], array[outer] = array[outer], array[smallestIdx]
    return array


s = selectionSort([43,5,22,1,13,91])
print(s)