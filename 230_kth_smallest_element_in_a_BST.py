# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional

from helpers import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        keys = []

        def walk(root):
            if not root:
                return
            walk(root.left)
            keys.append(root.val)
            walk(root.right)

        walk(root)
        return keys[k - 1]
