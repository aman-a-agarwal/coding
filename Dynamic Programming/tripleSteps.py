# A child can choose 1, 2, or 3 steps to climb n stairs
# How many ways can he do this


def take_steps_1(remaining):
    """Recursive Solution"""

    if remaining == 1 or remaining == 0:
        return 1
    if remaining == 2:
        return 2
    if remaining < 0:
        return 0

    count = 0

    for i in [1, 2, 3]:
        count += take_steps_1(remaining - i)

    return count


def take_steps_2(remaining):
    """Memoization"""

    path_store = {0: 1, 1: 1, 2: 2}

    if remaining in path_store:
        return path_store.get(remaining)

    count = 0

    for i in [1, 2, 3]:
        count += take_steps_2(remaining - i)

    return count


def take_steps_3(remaining):
    """Dynamic Programming"""

    dp = [1, 1, 2, 4]

    if remaining <= 3:
        return dp[remaining]

    for cur_step in range(4, remaining + 1):
        count = 0
        dp.append(dp[cur_step - 1] + dp[cur_step - 2] + dp[cur_step - 3])

    return dp[remaining]


print(take_steps_1(50))
