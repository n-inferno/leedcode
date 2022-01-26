# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
from typing import List

from helpers import TreeNode


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        tree = []

        def get_tree_elements(root):
            if not root:
                return
            tree.append(root.val)
            get_tree_elements(root.left)
            get_tree_elements(root.right)

        get_tree_elements(root1)
        get_tree_elements(root2)

        tree.sort()
        return tree


if __name__ == '__main__':
    solution = Solution()
    assert solution.getAllElements(root1=TreeNode(2, TreeNode(1), TreeNode(4)),
                                   root2=TreeNode(1, TreeNode(0), TreeNode(3))) == [0, 1, 1, 2, 3, 4]
    assert solution.getAllElements(root1=TreeNode(1, None, TreeNode(8)),
                                   root2=TreeNode(8, TreeNode(1))) == [1, 1, 8, 8]
