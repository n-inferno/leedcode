# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            min_amount = dp[i]
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    min_amount = min(min_amount, 1 + dp[i - coin]) if min_amount != -1 else 1 + dp[i - coin]

            dp[i] = min_amount
        return dp[-1]


if __name__ == '__main__':
    assert Solution().coinChange(coins=[1, 2, 5, 9], amount=11) == 2
    assert Solution().coinChange(coins=[1, 2, 5], amount=11) == 3
    assert Solution().coinChange(coins=[2], amount=3) == -1
    assert Solution().coinChange(coins=[1], amount=0) == 0
