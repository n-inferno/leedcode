# https://leetcode.com/problems/find-the-difference/
from collections import defaultdict
from itertools import zip_longest


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for f, s in zip_longest(s, t):
            counter1[f] += 1
            counter2[s] += 1

        for s in counter2:
            if counter1[s] != counter2[s]:
                return s


if __name__ == '__main__':
    solution = Solution()
    assert solution.findTheDifference(s='abcd', t='abcde') == 'e'
    assert solution.findTheDifference(s='', t='y') == 'y'
    assert solution.findTheDifference(s='a', t='aa') == 'a'
