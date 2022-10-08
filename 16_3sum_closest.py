# https://leetcode.com/problems/3sum-closest/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            fixed = nums[i]

            while l < r:
                suggest = nums[l] + nums[r] + fixed

                if abs(closest - target) > abs(suggest - target):
                    closest = suggest

                if suggest == target:
                    return suggest
                elif suggest > target:
                    r -= 1
                else:
                    l += 1

        return closest


if __name__ == '__main__':
    assert Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1) == 2
    assert Solution().threeSumClosest(nums=[0, 0, 0], target=1) == 0
    assert Solution().threeSumClosest(nums=[-2, 4, 6, 8, 9, 10, 12], target=13) == 13
