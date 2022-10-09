# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import Optional

from helpers import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def rec(node):
            nonlocal seen
            if not node:
                return False
            if k - node.val in seen:
                return True

            seen.add(node.val)
            return rec(node.left) or rec(node.right)

        return rec(root)
