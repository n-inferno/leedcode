# https://leetcode.com/problems/evaluate-boolean-binary-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left or not root.right:
            return bool(root.val)

        left = self.evaluateTree(root.left) == 1
        if root.val == 2 and left:
            right = True
        elif root.val == 3 and not left:
            right = False
        else:
            right = self.evaluateTree(root.right)

        if root.val == 2 and (left or right):
            root.val = 1
        elif root.val == 2:
            root.val = 0

        elif root.val == 3 and left and right:
            root.val = 1
        elif root.val == 3:
            root.val = 0

        return bool(root.val)


if __name__ == '__main__':
    assert Solution().evaluateTree(TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1))))
