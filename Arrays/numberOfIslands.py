from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid

        if grid is None or len(grid) is 0:
            return 0

        count = 0

        for row_idx, row in enumerate(grid):
            for col_idx, col in enumerate(row):
                if (col == '1'):
                    count += 1
                    self.dfs(row_idx, col_idx)

        return count

    def dfs(self, row, col):
        if row >= len(self.grid) or row < 0 or col >= len(
                self.grid[row]) or col < 0:
            return
        if self.grid[row][col] == '0':
            return
        self.grid[row][col] = '0'

        self.dfs(row - 1, col)
        self.dfs(row, col + 1)
        self.dfs(row + 1, col)
        self.dfs(row, col - 1)


s = Solution()
print(s.numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
