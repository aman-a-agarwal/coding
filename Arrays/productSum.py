# ProductSum: Return sum of all the products of each element with their respective depth in a nested list
# For Example: [1,2,3,4,5] ProductSum = 1 + 2 + 3 + 4 + 5 = 15
# For Example: [1,2,[1,2,3],4,5] ProductSum = 1 + 2 + 2*(1 + 2 + 3) + 4 +
# 5 = 24


def productSum(array):
    # Write your code here.
    return productSumHelper(array, 1)


def productSumHelper(array, depth):
    productSum = 0
    for element in array:
        if isinstance(element, int):
            productSum += element
        else:
            productSum += productSumHelper(element, depth + 1)
    return productSum * depth


p = productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
print(p)
