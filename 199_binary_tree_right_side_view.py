# https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append((root, 0))
        values = []
        prev_lvl, prev_val = 0, root.val
        while q:
            node, lvl = q.popleft()
            if prev_lvl != lvl:
                prev_lvl = lvl
                values.append(prev_val)

            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))

            prev_val = node.val

            if not q:
                values.append(node.val)

        return values

