# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    # classical
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

    # using sets
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    assert Solution().containsDuplicate(nums=[1, 2, 3, 1])
    assert not Solution().containsDuplicate(nums=[1, 2, 3, 4])
    assert Solution().containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
