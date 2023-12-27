from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        i, j = 0, 1
        removed_intervals_counter = 0
        while j < len(intervals):
            if intervals[j][0] >= intervals[i][1]:
                i += 1
                j += 1
            elif intervals[i][0] <= intervals[j][0] < intervals[i][1]:
                if intervals[j][1] >= intervals[i][1]:
                    intervals[j] = None
                    j += 1
                else:
                    intervals[i] = None
                    i = j
                    j += 1
                removed_intervals_counter += 1

            while i < j and intervals[i] is None:
                i += 1

        return removed_intervals_counter


if __name__ == "__main__":
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    assert Solution().eraseOverlapIntervals([[1, 4], [2, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 4], [3, 4]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2]]) == 0
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 4
    assert Solution().eraseOverlapIntervals([[2, 4], [3, 5], [4, 6], [5, 7], [6, 8]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
    assert Solution().eraseOverlapIntervals([[-100, -87], [-90, -44], [-86, 7], [-85, -76], [-70, 33]]) == 2
    assert Solution().eraseOverlapIntervals([[2, 5], [3, 6]]) == 1
    assert Solution().eraseOverlapIntervals([[-73, -26], [-65, -11], [-62, -49]]) == 2
