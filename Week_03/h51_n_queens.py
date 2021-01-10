from typing import List

'''
https://leetcode-cn.com/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
第一个皇后有N列可以选择，第二个皇后最多有N−1列可以选择，第三个皇后最多有N−2列可以选择（如果考虑到不能在同一条斜线上，可能的选择数量更少），
因此所有可能的情况不会超过 N!种，遍历这些情况的时间复杂度是 O(N!)。

为了降低总时间复杂度，每次放置皇后时需要快速判断每个位置是否可以放置皇后，显然，
最理想的情况是在 O(1)的时间内判断该位置所在的列和两条斜线上是否已经有皇后。BUT 算法的总时间复杂度都是 O(N!)

空间复杂度：O(N)，其中 N是皇后数量。空间复杂度主要取决于递归调用层数、记录每行放置的皇后的列下标的数组以及三个集合，
递归调用层数不会超过N，数组的长度为N，每个集合的元素个数都不会超过 N。

'''
class Solution:
    # Time: O(N!)
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        chess = [['.'] * n for _ in range(n)]
        self.solve(res, chess, 0)
        return res

    def solve(self, res, chess, row):
        if row == len(chess):
            # tmp = ["".join(chess[i]) for i in range(len(chess))]
            # res.append(tmp)
            res.append(["".join(chess[i]) for i in range(len(chess))])
            return

        # 遍历每一列
        for col in range(len(chess)):
            if self.valid(chess, row, col):
                chess[row][col] = 'Q'
                self.solve(res, chess, row + 1)
                chess[row][col] = '.'

    def valid(self, chess, row, col):
        # 因为是一行一行往下走的，所以只需要检查竖着的一列是否有皇后
        for i in range(row):  # 判断当前坐标位置(row, col)的正上方（列）有没有Queen
            if chess[i][col] == 'Q':
                return False

        # 检查左上斜线是否有Queen
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chess[i][j] == 'Q':
                return False
            i, j = i - 1, j - 1

        # 判断右上斜线有没有皇后
        i, j = row - 1, col + 1
        while i >= 0 and j < len(chess):
            if chess[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        return True

sol = Solution()
res = sol.solveNQueens(4)
print(res)