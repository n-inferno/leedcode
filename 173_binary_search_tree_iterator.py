# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

from helpers import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.keys = []
        self.walk(root)
        self.pointer = 0

    def walk(self, root):
        if not root:
            return
        self.walk(root.left)
        self.keys.append(root.val)
        self.walk(root.right)

    def next(self) -> int:
        val = self.keys[self.pointer]
        self.pointer += 1
        return val

    def hasNext(self) -> bool:
        return self.pointer < len(self.keys)
