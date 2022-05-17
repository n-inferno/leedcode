# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
from helpers import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        found_node = None

        def search_for_target(root, cloned):
            nonlocal found_node
            if root == target:
                found_node = cloned
                return

            if found_node:
                return

            if root.left:
                search_for_target(root.left, cloned.left)

            if root.right:
                search_for_target(root.right, cloned.right)

        search_for_target(original, cloned)
        return found_node
