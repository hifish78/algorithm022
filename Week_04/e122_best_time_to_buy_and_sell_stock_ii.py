from typing import List


class Solution:
    # Greedy
    # Time: O(N)
    # Space: O(1)
    """
    股票买卖策略：

    单独交易日： 设今天价格 p1、明天价格 p2, 则今天买入、明天卖出可赚取金额 p2−p1（负值代表亏损）。
    连续上涨交易日： 设此上涨交易日股票价格分别为 p1,p2,...,pn，则第一天买最后一天卖收益最大，即 pn−p1；等价于每天都买卖，
    即 pn−p1=(p2−p1)+(p3−p2)+...+(pn− pn−1)=(p_2 - p_1)+(p_3 - p_2)+...+(p_n - p_{n-1})。
    连续下降交易日： 则不买卖收益最大，即不会亏钱。
    隔天买卖怎么保证利益最大化的问题，看到"等价于每天都在买卖"
    """
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        max_profit = 0
        if not prices or len(prices) <= 1:
            return 0

        cur_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
            else:
                max_profit += prices[i] - cur_min
                cur_min = prices[i]
        return max_profit

