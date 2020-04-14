from typing import List


def rob(nums: List[int]) -> int:
    if not len(nums):
        return 0
    elif len(nums) == 1:
        return nums[0]
    dp = [(nums[0], True)]

    for num_idx in range(1, len(nums)):
        if num_idx == 1:
            dp.append((max(nums[num_idx], dp[num_idx - 1][0]), True if dp[num_idx - 1][0] > nums[num_idx] else False))
        elif num_idx == len(nums) - 1:
            if not dp[num_idx - 2][1]:
                dp.append((max(dp[num_idx - 2][0] + nums[num_idx], dp[num_idx - 1][0]),
                           dp[num_idx - 1][1] if dp[num_idx - 1][0] > dp[num_idx - 2][0] + nums[num_idx] else
                           dp[num_idx - 2][1]))
            elif not dp[num_idx - 1][1]:
                return dp[-1][0]
        else:
            dp.append((max(dp[num_idx - 2][0] + nums[num_idx], dp[num_idx - 1][0]),
                       dp[num_idx - 1][1] if dp[num_idx - 1][0] > dp[num_idx - 2][0] + nums[num_idx] else
                       dp[num_idx - 2][1]))
    return dp[-1][0]


print(rob([2, 1, 1, 2]))
