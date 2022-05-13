# https://leetcode.com/problems/path-sum/
from typing import Optional

from helpers import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum: int = 0) -> bool:
        if not root:
            return False

        currentSum += root.val
        if not root.left and not root.right:
            return currentSum == targetSum

        return self.hasPathSum(root.left, targetSum, currentSum) or self.hasPathSum(root.right, targetSum, currentSum)
