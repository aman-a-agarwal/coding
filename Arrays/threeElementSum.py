# O (n^3) Solution | O(1) Space
def threeNumberSum(array, targetSum):
    # Write your code here.
    returnArr = []
    array.sort()
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    returnArr.append([array[i], array[j], array[k]])
    return returnArr
