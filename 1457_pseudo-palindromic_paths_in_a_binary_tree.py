# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
from collections import defaultdict
from typing import Optional

from helpers import TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        counter = 0

        def walk(node, pairs, count_nodes):
            nonlocal counter
            if not node:
                return True

            pairs[node.val] += 1
            nodes = count_nodes + 1

            r1 = walk(node.left, pairs, nodes)
            r2 = walk(node.right, pairs, nodes)
            if r1 and r2:
                met = nodes % 2 == 0
                for k, v in pairs.items():
                    if v % 2 != 0 and not met:
                        met = True
                    elif v % 2 != 0:
                        break
                else:
                    counter += 1

            pairs[node.val] -= 1
            return False

        walk(root, defaultdict(int), 0)
        return counter


if __name__ == '__main__':
    nd1 = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)), TreeNode(1, None, TreeNode(1)))
    assert Solution().pseudoPalindromicPaths(nd1) == 2

    nd2 = TreeNode(2, TreeNode(1, TreeNode(1), TreeNode(3, None, TreeNode(1))), TreeNode(1))
    assert Solution().pseudoPalindromicPaths(nd2) == 1

    assert Solution().pseudoPalindromicPaths(TreeNode(9)) == 1

    nd3 = TreeNode(1, TreeNode(9, None, TreeNode(1)), TreeNode(1, None, TreeNode(1, TreeNode(7, None, TreeNode(4)))))
    assert Solution().pseudoPalindromicPaths(nd3) == 1
