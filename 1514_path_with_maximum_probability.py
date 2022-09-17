# https://leetcode.com/problems/path-with-maximum-probability/
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = defaultdict(list)
        for i, edge in enumerate(edges):
            d[edge[0]].append((edge[1], succProb[i]))
            d[edge[1]].append((edge[0], succProb[i]))

        results = [0.0 for _ in range(n)]
        results[start] = 1

        seen = set()
        q = [(-1, start)]
        while len(seen) < n and q:
            max_val, max_i = heapq.heappop(q)

            for to, prob in d[max_i]:
                results[to] = max(results[to], prob * -max_val)
                if to not in seen:
                    heapq.heappush(q, (-results[to], to))

            seen.add(max_i)
        return results[end]


if __name__ == '__main__':
    assert Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2) == 0.25000
    assert Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2) == 0.30000
    assert Solution().maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2) == 0.00000
    assert Solution().maxProbability(5, [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]], [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
                                     3, 4) == 0.21390
