# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        result = 0
        for boxes, units in boxTypes:
            for box in range(boxes):
                if truckSize <= 0:
                    return result

                result += units
                truckSize -= 1

        return result


if __name__ == '__main__':
    assert Solution().maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4) == 8
    assert Solution().maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10) == 91
