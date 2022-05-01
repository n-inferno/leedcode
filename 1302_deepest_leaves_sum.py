# https://leetcode.com/problems/deepest-leaves-sum/
from collections import defaultdict
from typing import Optional

from helpers import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_deep = 0
        sums = defaultdict(int)

        def calculate(root, curr_deep):
            nonlocal max_deep
            if not root:
                max_deep = max(max_deep, curr_deep)
                return

            curr = curr_deep + 1
            sums[curr_deep] += root.val
            calculate(root.left, curr)
            calculate(root.right, curr)

        calculate(root, 0)
        return sums[max_deep - 1]
