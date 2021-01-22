from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        self.dirs = [(0,1), (0,-1), (-1, 0), (1, 0)]

        res = 0
        self.m, self.n = len(grid), len(grid[0])

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return

        if grid[x][y] != '1':
            return

        grid[x][y] = '0'
        for k in range(4):
            self.dfs(grid, x + self.dirs[k][0], y + self.dirs[k][1])