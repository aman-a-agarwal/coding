from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.row_size = len(grid)
        self.col_size = len(grid[0])
        count = 0
        while (True):
            self.list_of_tuples = []
            for x in range(self.row_size):
                for y in range(self.col_size):
                    isRotten = grid[x][y] == 2
                    if (isRotten):
                        self.checkOrange((x + 1, y))  # right
                        self.checkOrange((x - 1, y))  # left
                        self.checkOrange((x, y + 1))  # down
                        self.checkOrange((x, y - 1))  # up

            if len(self.list_of_tuples) == 0:
                for x in range(self.row_size):
                    for y in range(self.col_size):
                        if grid[x][y] == 1:
                            return -1
                return count
            else:
                for tup in self.list_of_tuples:
                    x, y = tup
                    self.grid[x][y] = 2
                count += 1

    def checkOrange(self, location):
        x, y = location
        if x < 0 or x >= self.row_size:
            return
        if y < 0 or y >= self.col_size:
            return
        if self.grid[x][y] == 1:
            self.list_of_tuples.append((x, y))


s = Solution()
count = s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])

print(count)
