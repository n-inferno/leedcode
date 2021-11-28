# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List


class Solution:
    def allPathsSourceTargetRec(self, graph, current_node, target, track=None):
        track = track.copy() or []
        track.append(current_node)
        if current_node == target:
            self.result.append(track)
            return
        for i in range(len(graph[current_node])):
            self.allPathsSourceTargetRec(graph, graph[current_node][i], target, track)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        target = len(graph) - 1
        for item in graph[0]:
            track = [0]
            self.allPathsSourceTargetRec(graph, item, target, track)
        return self.result


if __name__ == '__main__':
    solution = Solution()
    assert solution.allPathsSourceTarget(graph=[[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    assert solution.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4],
                                                                                         [0, 1, 3, 4], [0, 1, 2, 3, 4],
                                                                                         [0, 1, 4]]
    assert solution.allPathsSourceTarget(graph=[[1], []]) == [[0, 1]]
    assert solution.allPathsSourceTarget(graph=[[1, 2, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
    assert solution.allPathsSourceTarget(graph=[[1, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 3]]
    assert solution.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4],
                                                                                        [0, 1, 4]]
