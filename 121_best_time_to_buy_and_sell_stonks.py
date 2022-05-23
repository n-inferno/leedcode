# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        profit = 0
        min_element = prices[0]
        for i, price in enumerate(prices):
            min_element = min(price, min_element)
            profit = max(price - min_element, profit)

        return profit


if __name__ == '__main__':
    assert Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit(prices=[7, 6, 4, 3, 1]) == 0
