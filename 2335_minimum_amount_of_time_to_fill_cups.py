import heapq
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        counter = 0
        amount = [-1 * i for i in amount]
        heapq.heapify(amount)

        while amount[0] < 0:
            max_element = heapq.heappop(amount)
            if amount[0] < 0:
                item = heapq.heappop(amount)
                heapq.heappush(amount, item + 1)

            max_element += 1
            heapq.heappush(amount, max_element)

            counter += 1

        return counter


if __name__ == '__main__':
    assert Solution().fillCups([1, 4, 2]) == 4
    assert Solution().fillCups([5, 4, 4]) == 7
    assert Solution().fillCups([1, 2, 3]) == 3
