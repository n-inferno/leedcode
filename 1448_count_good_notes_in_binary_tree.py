# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
from helpers import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0

        def walk(node, maxi):
            nonlocal counter
            if not node:
                return
            if maxi <= node.val:
                counter += 1
                maxi = node.val
            walk(node.left, maxi)
            walk(node.right, maxi)

        walk(root, float("-inf"))
        return counter
