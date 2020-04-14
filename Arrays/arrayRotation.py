def rotLeft(a, d):
    map_pos = [(i - d) for i in range(len(a))]
    returnList = [None for i in range(len(a))]
    for idx, ele in enumerate(map_pos):
        returnList[ele] = a[idx]
    return returnList


arr = [1, 2, 3, 4, 5]
d = 4

r = rotLeft(arr, d)
