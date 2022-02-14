# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0

        def helper(root, curr):
            nonlocal result
            if not root:
                result = max(curr, result)
                return
            helper(root.left, curr + 1)
            helper(root.right, curr + 1)

        helper(root, 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxDepth(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 3
