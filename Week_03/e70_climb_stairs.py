"""
https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-lcina-egpz/
"""
class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        f1, f2, f3 = 1, 2, 3
        for i in range(3, n + 1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

    def climbStairs2(self, n: int) -> int:
        prev = 1
        cur = 1
        for i in range(2, n + 1):
            tmp = cur
            cur = prev + cur
            prev = tmp
        return cur

    # dp[0] = 1, dp[1] = 1, dp[i] = dp[i - 2] + dp[i-1]
    # Time Complexity: O(N), Space Complexity: O(1)
    def climbStairs3(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]

