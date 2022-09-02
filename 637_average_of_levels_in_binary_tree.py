# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from collections import deque
from typing import Optional, List

from helpers import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((root, 0))  # (node, lvl)
        averages = []

        curr_sum, curr_level, curr_counter = 0, 0, 0
        while q:
            node, level = q.popleft()
            if level > curr_level:
                averages.append(curr_sum / curr_counter)
                curr_sum, curr_level, curr_counter = 0, level, 0
            curr_sum += node.val
            curr_counter += 1

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        averages.append(curr_sum / curr_counter)
        return averages


if __name__ == '__main__':
    assert Solution().averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [3.00000, 14.50000, 11.00000]

