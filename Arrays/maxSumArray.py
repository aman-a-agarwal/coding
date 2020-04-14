def maxSubsetSum(arr):
    result = 0
    useSum = 0
    notUseSum = 0
    for number in arr:
        result = max(result, notUseSum + number)

        nextUseSum = notUseSum + number
        nextNotUseSum = max(useSum, notUseSum)

        useSum = nextUseSum
        notUseSum = nextNotUseSum
    return result


if __name__ == '__main__':
    n = 5

    arr = list(map(int, "3 7 4 6 5".rstrip().split()))

    res = maxSubsetSum(arr)

    print(res)
