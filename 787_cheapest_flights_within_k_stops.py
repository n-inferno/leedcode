# https://leetcode.com/problems/cheapest-flights-within-k-stops/
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(dict)
        for fr, to, price in flights:
            g[fr][to] = price

        min_prices = defaultdict(lambda: float("inf"))
        min_prices[src] = 0

        to_see = {(src, 0)}
        while k >= 0:
            new = set()
            for item, curr_price in to_see:
                for to, price in g[item].items():
                    if min_prices[to] > curr_price + price:
                        min_prices[to] = curr_price + price
                        new.add((to, curr_price + price))

            to_see = new
            k -= 1

        return -1 if min_prices[dst] == float("inf") else min_prices[dst]


if __name__ == '__main__':
    assert Solution().findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0,
                                        dst=3, k=1) == 700
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1) == 200
    assert Solution().findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0) == 500
