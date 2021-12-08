# https://leetcode.com/problems/binary-tree-tilt/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = 0

        def helper(root):
            nonlocal result
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            result += abs(left - right)

            return left + right + root.val

        helper(root)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.findTilt(TreeNode(1, TreeNode(2), TreeNode(3))) == 1
    assert solution.findTilt(TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7)))) == 15
