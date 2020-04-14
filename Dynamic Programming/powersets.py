def powerset(array):
    # Write your code here.
    dp = [[]]
    for num in array:
        for sets in range(len(dp)):
            newSet = dp[sets]
            dp.append(newSet + [num])
    return dp


powerset([1, 2, 3])
