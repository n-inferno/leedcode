# https://leetcode.com/problems/binary-tree-paths/
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def walk(root, current_path):
            nonlocal paths
            current_path.append(str(root.val))
            if not root.left and not root.right:
                paths.append("->".join(current_path))

            if root.left:
                walk(root.left, current_path)
            if root.right:
                walk(root.right, current_path)
            current_path.pop()

        walk(root, [])
        return paths
