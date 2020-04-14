def maxSubsetSum(nums):
    dp = [nums[0]]
    maxSum = nums[0]

    for idx in range(1, len(nums)):
        dp.append(max(nums[idx], dp[-1] + nums[idx]))
        maxSum = max(maxSum, dp[-1])
    return maxSum


print(maxSubsetSum([1, -2, 6, -3, 4, -1]))
