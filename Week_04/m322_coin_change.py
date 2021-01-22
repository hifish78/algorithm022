## look into it later
class Solution:
    def coinChange(self, coins, amount):
        dp = [ amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
