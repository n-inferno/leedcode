# https://leetcode.com/problems/deepest-leaves-sum/
from typing import Optional

from helpers import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_deep = 0
        result = 0

        def find_deep(root, curr_deep=0):
            nonlocal max_deep
            if not root:
                max_deep = max(max_deep, curr_deep)
                return
            curr = curr_deep + 1
            find_deep(root.left, curr)
            find_deep(root.right, curr)

        def calculate(root, curr_deep=0):
            nonlocal result, max_deep
            if not root:
                return
            if curr_deep == max_deep - 1:
                result += root.val
            curr = curr_deep + 1
            calculate(root.left, curr)
            calculate(root.right, curr)

        find_deep(root)
        calculate(root)
        return result