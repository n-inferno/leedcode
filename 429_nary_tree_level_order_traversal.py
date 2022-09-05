# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []

        def walk(node, lvl):
            nonlocal result
            if not node:
                return

            while len(result) <= lvl:
                result.append([])

            result[lvl].append(node.val)

            for child in node.children:
                walk(child, lvl + 1)

        walk(root, 0)
        return result
