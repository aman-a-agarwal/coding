def maxSubsetSum(arr):
    # initialize the DP array
    dp = [arr[0]]
    dp.append(max(arr[0], arr[1]))

    for idx in range(2, len(arr)):
        ele = arr[idx]
        dp.append(max(ele, dp[idx - 1], ele + dp[idx - 2]))
        print(dp)
        print(ele)
    return dp[-1]


if __name__ == '__main__':

    arr = list(map(int, "3 7 4 6 5".rstrip().split()))

    res = maxSubsetSum(arr)