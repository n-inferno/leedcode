# https://leetcode.com/problems/open-the-lock/
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def get_children(parent):
            result = []
            for position in range(4):
                d1 = (int(parent[position]) + 1) % 10
                d2 = (int(parent[position]) - 1 + 10) % 10
                result.append(parent[:position] + str(d1) + parent[position + 1:])
                result.append(parent[:position] + str(d2) + parent[position + 1:])

            return result

        queue = deque()
        queue.append(("0000", 0))
        visited = set(deadends)
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns

            for child in get_children(lock):
                if child not in visited:
                    visited.add(child)
                    queue.append((child, turns + 1))

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202") == 6
    assert solution.openLock(deadends=["8888"], target="0009") == 1
    assert solution.openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888") == -1
