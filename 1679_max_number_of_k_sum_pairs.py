# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)

        operation_counter = 0
        for item in list(counter):
            while counter[item] > 0:
                counter[item] -= 1
                if counter.get(k - item) and counter[k - item] > 0:
                    counter[k - item] -= 1
                    operation_counter += 1
                else:
                    counter[item] += 1
                    break

        return operation_counter


if __name__ == '__main__':
    assert Solution().maxOperations(nums=[4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], k=2) == 2
    assert Solution().maxOperations(nums=[1, 1], k=2) == 1
    assert Solution().maxOperations(nums=[1, 2], k=4) == 0
    assert Solution().maxOperations(nums=[1, 2, 3, 4], k=5) == 2
    assert Solution().maxOperations(nums=[3, 1, 3, 4, 3], k=6) == 1
