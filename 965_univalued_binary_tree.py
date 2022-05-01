# https://leetcode.com/problems/univalued-binary-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val

        def helper(root):
            if not root:
                return True
            if root.val != val:
                return False

            return helper(root.left) and helper(root.right)

        return helper(root)
