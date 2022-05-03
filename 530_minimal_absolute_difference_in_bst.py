# https://leetcode.com/problems/minimum-absolute-difference-in-bst
from typing import Optional

from helpers import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        last_value = None
        min_diff = float("inf")

        def helper(root):
            nonlocal last_value, min_diff
            if not root:
                return

            helper(root.left)

            if last_value is not None:
                min_diff = min(abs(last_value - root.val), min_diff)
            last_value = root.val

            helper(root.right)

        helper(root)
        return min_diff
