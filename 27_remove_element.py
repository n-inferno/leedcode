# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = j = 0
        while j < len(nums):
            while j < len(nums) and nums[j] == val:
                j += 1
                k += 1

            if j >= len(nums):
                break

            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j += 1

        return len(nums) - k


if __name__ == '__main__':
    solution = Solution()
    case1 = [3, 2, 2, 3]
    k = solution.removeElement(case1, 3)
    assert case1[:k] == [2, 2]
    assert k == 2

    case2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k = solution.removeElement(case2, 2)
    assert case2[:k] == [0, 1, 3, 0, 4]
    assert k == 5

    case3 = [1]
    k = solution.removeElement(case3, 1)
    assert case3[:k] == []
    assert k == 0

    case4 = [2]
    k = solution.removeElement(case4, 3)
    assert case4[:k] == [2]
    assert k == 1
