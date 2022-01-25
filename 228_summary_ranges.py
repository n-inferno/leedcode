# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result = []
        first, last = None, None
        for i in range(len(nums)):
            if first is None:
                first = nums[i]
                last = nums[i]
            elif nums[i] - nums[i - 1] == 1:
                last = nums[i]
            else:
                if first == last:
                    result.append(str(first))
                else:
                    result.append(f'{first}->{last}')
                first = last = nums[i]

        if first is not None:
            if last == first:
                result.append(str(first))
            else:
                result.append(f'{first}->{last}')

        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.summaryRanges(nums=[0, 1, 2, 4, 5, 7]) == ['0->2', '4->5', '7']
    assert solution.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]) == ['0', '2->4', '6', '8->9']
