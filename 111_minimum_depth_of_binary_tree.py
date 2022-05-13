# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = None

        def walk(root, curr_depth):
            nonlocal min_depth
            if not root:
                return

            if not root.left and not root.right:
                min_depth = min(min_depth, curr_depth) if min_depth is not None else curr_depth
                return

            walk(root.left, curr_depth + 1)
            walk(root.right, curr_depth + 1)

        walk(root, 1)
        return min_depth or 0
