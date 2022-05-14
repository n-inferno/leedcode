# https://leetcode.com/problems/network-delay-time/
from collections import defaultdict
from queue import PriorityQueue
from functools import partial
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit_index_map = defaultdict(partial(defaultdict, dict))
        for start, finish, path in times:
            visit_index_map[start][finish] = path

        markers = [float("inf") for _ in range(n)]
        markers[k - 1] = 0

        q = PriorityQueue()
        q.put((0, k))

        visited = set()
        while not q.empty():
            pr, el = q.get()
            for destination in visit_index_map[el]:
                distance = markers[el - 1] + visit_index_map[el][destination]
                markers[destination - 1] = min(markers[destination - 1], distance)
                if destination not in visited:
                    q.put((distance, destination))

            visited.add(el)

        return max(markers) if len(visited) == n else -1


if __name__ == '__main__':
    assert Solution().networkDelayTime(times=[[1, 2, 1], [2, 3, 2], [1, 3, 4]], n=3, k=1) == 3
    assert Solution().networkDelayTime(times=[[1, 2, 6], [1, 3, 5], [2, 3, 2], [3, 2, 3]], n=3, k=1) == 6
    assert Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) == 2
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1) == 1
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2) == -1
