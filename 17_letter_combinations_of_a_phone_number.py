# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        if len(digits) == 1:
            return letters[digits[0]]
        combinations = []

        def helper(current_digit, prefix):
            if current_digit >= len(digits):
                combinations.append("".join(prefix))
                return

            for variant in letters[digits[current_digit]]:
                helper(current_digit + 1, [*prefix, variant])

        helper(0, [])
        return combinations


if __name__ == '__main__':
    solution = Solution()
    assert set(solution.letterCombinations(digits='23')) == {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert set(solution.letterCombinations(digits='')) == set()
    assert set(solution.letterCombinations(digits='2')) == {'a', 'b', 'c'}
