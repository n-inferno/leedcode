# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        q.append((root, 0))

        while q:
            element, lvl = q.popleft()

            if q and q[0][1] == lvl:
                element.next = q[0][0]
            else:
                element.next = None

            if element.left:
                q.append((element.left, lvl + 1))
            if element.right:
                q.append((element.right, lvl + 1))

        return root
