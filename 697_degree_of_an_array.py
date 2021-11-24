# https://leetcode.com/problems/degree-of-an-array/
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # count elements and store min and max index
        element_indexes = {}
        each_counter = {}
        for i in range(len(nums)):
            each_counter.setdefault(nums[i], 0)
            if nums[i] not in element_indexes:
                element_indexes[nums[i]] = [i, i]
            else:
                element_indexes[nums[i]][-1] = i
            each_counter[nums[i]] += 1

        # search elements with max occurrence number
        elements = set()
        max_count = 0
        for k, v in each_counter.items():
            if v > max_count:
                max_count = v
                elements = set()
                elements.add(k)
            elif v == max_count:
                elements.add(k)

        # find the minimum one
        min_length = 50001
        for item in elements:
            curr = element_indexes[item]
            min_length = min(min_length, curr[1] - curr[0] + 1)

        return min_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.findShortestSubArray(nums=[1, 2, 2, 3, 1]) == 2
    assert solution.findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]) == 6
