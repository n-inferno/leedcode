# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def __init__(self):
        self.letters = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }

    def letterCombinations(self, digits: str) -> List[str]:
        result = set()

        def helper(left_digits, curr_result):
            if not left_digits:
                if curr_result:
                    result.add(curr_result)
                return
            d = left_digits[0]
            for variant in self.letters[d]:
                helper(left_digits[1:], curr_result + variant)

        helper(digits, '')
        return list(result)


if __name__ == '__main__':
    solution = Solution()
    assert set(solution.letterCombinations(digits='23')) == {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}
    assert set(solution.letterCombinations(digits='')) == set()
    assert set(solution.letterCombinations(digits='2')) == {'a', 'b', 'c'}
