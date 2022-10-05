# https://leetcode.com/problems/add-one-row-to-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def rec(node, depth):
            if not node:
                return
            if depth <= 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
                return
            rec(node.left, depth - 1)
            rec(node.right, depth - 1)

        if depth == 1:
            return TreeNode(val, root)

        rec(root, depth - 1)
        return root
