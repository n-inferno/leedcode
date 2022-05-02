# https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        def helper(node, origin):
            if origin in visited:
                return
            visited[origin] = node
            node.val = origin.val
            for neighbor in origin.neighbors:
                new = Node() if neighbor not in visited else visited[neighbor]
                helper(new, neighbor)
                node.neighbors.append(new)

        start = Node()
        helper(start, node)
        return start
