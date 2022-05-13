# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
from typing import Optional

from helpers import TreeNode


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        global_result_counter = 0

        def average_walk(root):
            nonlocal global_result_counter
            if not root:
                return 0, 0

            if not root.left and not root.right:
                global_result_counter += 1
                return root.val, 1

            sum_left, counter_left = average_walk(root.left)
            sum_right, counter_right = average_walk(root.right)

            subtree_sum = sum_left + sum_right + root.val
            counter = counter_left + counter_right + 1

            if subtree_sum // counter == root.val:
                global_result_counter += 1

            return subtree_sum, counter

        average_walk(root)
        return global_result_counter


if __name__ == '__main__':
    assert Solution().averageOfSubtree(TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))) == 5
