# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from helpers import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(curr):
            if not curr:
                return
            if curr.val > p.val and curr.val > q.val:
                return search(curr.left)
            elif curr.val < p.val and curr.val < q.val:
                return search(curr.right)

            return curr

        return search(root)
