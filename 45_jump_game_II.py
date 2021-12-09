# https://leetcode.com/problems/jump-game-ii/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dest = [0]
        while dest[-1] < len(nums) - 1:
            e1, e2 = 0 if len(dest) == 1 else dest[-2] + 1, dest[-1]
            max_in_group = e2
            for i in range(e1, min(e2 + 1, len(nums) - 1)):
                max_in_group = max(max_in_group, i + nums[i])
            dest.append(max_in_group)

        return len(dest) - 1


if __name__ == '__main__':
    solution = Solution()
    assert solution.jump(nums=[2, 3, 1, 1, 4]) == 2
    assert solution.jump(nums=[2, 3, 0, 1, 4]) == 2
    assert solution.jump(nums=[1]) == 0
    assert solution.jump(nums=[2, 1]) == 1
    assert solution.jump(nums=[5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]) == 3
