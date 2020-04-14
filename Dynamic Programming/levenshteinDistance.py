def levenshteinDistance(str1, str2):
    # Write your code here.
    str1 = " " + str1
    str2 = " " + str2
    dp = [[x for x in range(len(str1))] for y in range(len(str2))]
    for idx1 in range(len(str2)):
        dp[idx1][0] = idx1
    for idx1 in range(1, len(str2)):
        for idx2 in range(1, len(str1)):
            if str1[idx2] == str2[idx1]:
                dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
            else:
                dp[idx1][idx2] = 1 + min(dp[idx1 - 1][idx2 - 1],
                                         dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
    return dp[-1][-1]


print(levenshteinDistance("abc", "yabd"))
