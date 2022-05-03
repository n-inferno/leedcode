# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from helpers import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        tracker = []
        paths = {}

        def helper(root):
            if not root:
                return

            tracker.append(root)
            if p == root:
                paths[p] = tracker.copy()
            elif q == root:
                paths[q] = tracker.copy()
            helper(root.left)
            helper(root.right)
            tracker.pop()

        helper(root)

        i = 0
        while i < min(len(paths[p]), len(paths[q])):
            if paths[p][i] != paths[q][i]:
                return paths[p][i - 1]
            i += 1

        return paths[p][i - 1]
