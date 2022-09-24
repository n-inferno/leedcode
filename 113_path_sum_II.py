# https://leetcode.com/problems/path-sum-ii/
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result

        def walk(node, curr_sum, path):
            nonlocal result
            if not node:
                return False

            path.append(node.val)
            curr_sum += node.val

            left = walk(node.left, curr_sum, path)
            right = walk(node.right, curr_sum, path)
            if not left and not right:
                if curr_sum == targetSum:
                    result.append(path.copy())

            path.pop()
            return True

        walk(root, 0, [])
        return result


if __name__ == '__main__':
    assert Solution().pathSum(TreeNode(1, TreeNode(2)), 1) == []
    assert Solution().pathSum(TreeNode(1, TreeNode(2), TreeNode(2)), 3) == [[1, 2], [1, 2]]
