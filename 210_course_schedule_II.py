# https://leetcode.com/problems/course-schedule-ii/
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = defaultdict(list)
        for to_take_course, requirement in prerequisites:
            courses_map[to_take_course].append(requirement)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in courses_map[course]:
                if not dfs(pre):
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output


if __name__ == '__main__':
    solution = Solution()
    assert solution.findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert solution.findOrder(numCourses=6, prerequisites=[[0, 5], [0, 4], [1, 0], [2, 0], [3, 1], [2, 3]]) == [5, 4, 0,
                                                                                                                1, 3, 2]
    assert solution.findOrder(numCourses=4, prerequisites=[[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]]) == []
    assert solution.findOrder(numCourses=1, prerequisites=[]) == [0]
