# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
from helpers import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        path = None

        def search_for_target(root, curr_path):
            nonlocal path
            if root == target:
                path = curr_path[:]
                return

            if root.left:
                search_for_target(root.left, [*curr_path, "l"])

            if root.right:
                search_for_target(root.right, [*curr_path, "r"])

        search_for_target(original, [])

        def follow_path(root, index):
            if index >= len(path):
                return root

            if path[index] == "l":
                return follow_path(root.left, index + 1)
            return follow_path(root.right, index + 1)

        return follow_path(cloned, 0)
