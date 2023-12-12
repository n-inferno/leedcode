from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        water = 0
        while left < len(height):
            for i in range(left, len(height) - 1):
                if height[i] > height[i + 1]:
                    left = i
                    break
            else:
                return water

            right = left + 1
            max_el, max_i = height[right], right
            while right < len(height) and height[right] < height[left]:
                if max_el < height[right]:
                    max_el = height[right]
                    max_i = right
                right += 1

            if right >= len(height):
                min_lvl = max_el
                right = max_i
            else:
                min_lvl = height[left]

            for i in range(left, right):
                if min_lvl > height[i]:
                    water += min_lvl - height[i]

            left = right

        return water


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([4, 2, 3]) == 1
