def insertionSort (array):
    for outer in range(1, len(array)):
        inner = outer
        while inner > 0 and array[inner] < array[inner - 1]:
            # swap
            array[inner], array[inner - 1] = array[inner - 1], array[inner]
            inner -= 1
    return array

s = insertionSort([43,5,22,1,13,91])
print(s)