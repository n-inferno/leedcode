# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional

from helpers import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(node, start, end):
            if start >= end:
                return

            mid = start + (end - start) // 2
            node.val = nums[mid]
            node.left = construct(TreeNode(), start, mid)
            node.right = construct(TreeNode(), mid + 1, end)

            return node

        return construct(TreeNode(), 0, len(nums))
