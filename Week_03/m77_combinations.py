from typing import List


class Solution:
    # time complexity: K*N!/(N-K)!K!
    # Space: N!/(N-K)!K!
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(n, k, 1, [], res)
        return res

    # 1, 2, 3, 4 [1, 2]
    def helper(self, n, k, start, item, res):
        if len(item) == k:
            res.append(list(item))
            return

        for i in range(start, n + 1):
            item.append(i)
            self.helper(n, k, i + 1, item, res)
            item.pop()
sol = Solution()
res = sol.combine(4, 2)
print(res)
