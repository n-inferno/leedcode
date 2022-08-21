# https://leetcode.com/problems/stamping-the-sequence/
from typing import Optional

from helpers import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        r = True

        def walk(node: Optional[TreeNode], curr_height=0):
            nonlocal r
            if not node:
                return curr_height

            max_left = walk(node.left, curr_height + 1)
            max_right = walk(node.right, curr_height + 1)

            r = r and abs(max_left - max_right) <= 1

            return max(max_left, max_right)

        walk(root)
        return r
