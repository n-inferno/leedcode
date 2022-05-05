# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack = []
        values = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif stack:
                current = stack.pop()
                values.append(current.val)
                current = current.right

            else:
                break

        return values


if __name__ == '__main__':
    assert Solution().inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]
