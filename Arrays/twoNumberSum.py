# O(n^2) solution
def twoNumberSum(array, targetSum):
    # Write your code here.
    for idx, num1 in enumerate(array):
        for num2 in array[idx:]:
            if (num1 != num2 and num1 + num2 == targetSum):
                return [num1, num2]
    return []

# O(n) solution
def twoNumberSum(array, targetSum):
    # Write your code here.
    map = dict()
    for idx, num1 in enumerate(array):
        difference = targetSum - num1
        if (difference in map):
            return [num1, difference]
        else:
            map[difference] = True
    return []

twoNumberSum([], 168)