# https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root, 1))
        result = []
        while queue:
            el, lvl = queue.popleft()
            if el:
                if len(result) < lvl:
                    result.append([])
                result[-1].append(el.val)
                queue.append((el.left, lvl + 1))
                queue.append((el.right, lvl + 1))

        return result
