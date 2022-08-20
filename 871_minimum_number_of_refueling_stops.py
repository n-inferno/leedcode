# https://leetcode.com/problems/minimum-number-of-refueling-stops/
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        hp = []
        point = -1
        count = 0
        while startFuel < target and (hp or point < len(stations)):
            while point < len(stations) - 1 and stations[point + 1][0] <= startFuel:
                point += 1
                heapq.heappush(hp, (-stations[point][1], stations[point][0]))

            if not hp:
                break

            next_max_gs = hp[0] if hp else None
            while next_max_gs and (
                    (point + 1 < len(stations) and startFuel < stations[point + 1][0]) or (
                    point + 1 >= len(stations) and startFuel < target)):
                startFuel += -next_max_gs[0]
                count += 1
                heapq.heappop(hp)
                next_max_gs = hp[0] if hp else None

        if startFuel >= target:
            return count
        return -1


if __name__ == '__main__':
    assert Solution().minRefuelStops(100, 50, [[25, 25], [50, 50]]) == 1
    assert Solution().minRefuelStops(target=100, startFuel=1, stations=[[10, 100]]) == -1
    assert Solution().minRefuelStops(target=100, startFuel=10,
                                     stations=[[10, 60], [20, 30], [30, 30], [60, 40]]) == 2
    assert Solution().minRefuelStops(1, 1, []) == 0
    assert Solution().minRefuelStops(100, 25, [[25, 25], [50, 25], [75, 25]]) == 3
    assert Solution().minRefuelStops(1000, 299,
                                     [[13, 21], [26, 115], [100, 47], [225, 99], [299, 141],
                                      [444, 198], [608, 190], [636, 157], [647, 255],
                                      [841, 123]]) == 4
