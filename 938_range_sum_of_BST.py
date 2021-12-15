# https://leetcode.com/problems/range-sum-of-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summa = 0
        def helper(root):
            nonlocal summa
            if not root:
                return
            if low <= root.val <= high:
                summa += root.val
            helper(root.left)
            helper(root.right)

        helper(root)
        return summa



if __name__ == '__main__':
    solution = Solution()
    assert solution.rangeSumBST(root=TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)),
                                              TreeNode(15, None, TreeNode(18))), low=7, high=15) == 32
