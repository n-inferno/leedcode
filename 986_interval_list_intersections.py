# https://leetcode.com/problems/interval-list-intersections/
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervals = []
        p1 = p2 = 0
        while p1 < len(firstList) and p2 < len(secondList):
            first = max(firstList[p1][0], secondList[p2][0])
            second = min(firstList[p1][1], secondList[p2][1])
            if second >= first:
                intervals.append([first, second])
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return intervals


if __name__ == '__main__':
    solution = Solution()
    assert solution.intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                         secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10],
                                                                                               [15, 23], [24, 24],
                                                                                               [25, 25]]
    assert solution.intervalIntersection(firstList=[[1, 3], [5, 9]], secondList=[]) == []
    assert solution.intervalIntersection(firstList=[], secondList=[[4, 8], [10, 12]]) == []
    assert solution.intervalIntersection(firstList=[[1, 7]], secondList=[[3, 10]]) == [[3, 7]]
    assert solution.intervalIntersection(firstList=[[1, 8], [12, 16]], secondList=[[8, 10]]) == [[8, 8]]
    assert solution.intervalIntersection(firstList=[[8, 10]], secondList=[[1, 5]]) == []
    assert solution.intervalIntersection(firstList=[[1, 3]], secondList=[[5, 9]]) == []
