def longestPalindrome(s: str) -> str:
    start = end = 0
    maxString = 0
    grid = [[None for x in range(len(s))] for y in range(len(s))]
    for row_idx in range(len(s)):
        for col_idx in range(row_idx + 1):
            if row_idx == col_idx:
                grid[row_idx][col_idx] = True
            elif row_idx - col_idx == 1:
                grid[row_idx][col_idx] = s[row_idx] == s[col_idx]
            else:
                grid[row_idx][col_idx] = grid[row_idx - 1][col_idx + 1] and s[row_idx] == s[col_idx]

            if grid[row_idx][col_idx] and maxString < row_idx - col_idx + 1:
                maxString = row_idx - col_idx + 1
                start = col_idx
                end = row_idx

    return s[start:end]

longestPalindrome("babad")