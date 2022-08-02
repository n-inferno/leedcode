# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
import queue
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = queue.PriorityQueue(maxsize=k)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                el = -matrix[i][j]
                if q.full():
                    last = q.get()
                    if last >= el:
                        el = last
                q.put(el)

        return -q.get()


if __name__ == '__main__':
    assert Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8) == 13
    assert Solution().kthSmallest(matrix=[[-5]], k=1) == -5
