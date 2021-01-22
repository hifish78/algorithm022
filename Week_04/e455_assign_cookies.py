from typing import List


class Solution:
    # Time: O(N), N is min(len(g), len(s))
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        if not g or not s:
            return 0
        g_len, s_len = len(g), len(s)
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res

