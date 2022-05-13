# https://leetcode.com/problems/symmetric-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def walk(root, nodes, reverse=False):
            if not root:
                nodes.append(None)
                return

            nodes.append(root.val)
            if not reverse:
                walk(root.left, nodes, reverse)
            walk(root.right, nodes, reverse)
            if reverse:
                walk(root.left, nodes, reverse)

            return nodes

        return walk(root.left, []) == walk(root.right, [], reverse=True)
