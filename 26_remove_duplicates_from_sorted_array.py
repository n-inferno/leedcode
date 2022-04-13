# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        k = 0
        curr = nums[0]
        while i < len(nums) - k:
            j = i + k
            while j < len(nums) and nums[j] == curr:
                j += 1
                k += 1

            if j >= len(nums):
                break

            nums[i], nums[j] = nums[j], nums[i]
            curr = nums[i]
            i += 1

        return len(nums) - k


if __name__ == '__main__':
    solution = Solution()
    case1 = [1, 1, 2]
    k = solution.removeDuplicates(case1)
    assert case1[:k] == [1, 2]
    assert k == 2

    case2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(case2)
    assert case2[:k] == [0, 1, 2, 3, 4]
    assert k == 5

    case3 = [1, 1]
    k = solution.removeDuplicates(case3)
    assert case3[:k] == [1]
    assert k == 1

    case4 = [2, 3]
    k = solution.removeDuplicates(case4)
    assert case4[:k] == [2, 3]
    assert k == 2

    case5 = [2]
    k = solution.removeDuplicates(case5)
    assert case5[:k] == [2]
    assert k == 1
