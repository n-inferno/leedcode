# https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[-1], dp[-2])


if __name__ == '__main__':
    assert Solution().minCostClimbingStairs(cost=[10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
