# https://leetcode.com/problems/construct-string-from-binary-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""

        def walk(node):
            nonlocal result
            if not node:
                return
            result += f"({node.val}"
            walk(node.left)
            if not node.left and node.right:
                result += "()"
            walk(node.right)
            result += ")"

        walk(root)
        return result[1:-1]
