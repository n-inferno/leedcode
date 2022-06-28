# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import defaultdict, Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        max_freq = 0
        d = defaultdict(int)

        for v in count.values():
            d[v] += 1
            max_freq = max(max_freq, v)

        operations = 0
        while max_freq > 0:
            if d[max_freq] > 1:
                operations += d[max_freq] - 1
                d[max_freq - 1] += d[max_freq] - 1

            max_freq -= 1

        return operations


if __name__ == '__main__':
    assert Solution().minDeletions(s="aab") == 0
    assert Solution().minDeletions(s="aaabbbcc") == 2
    assert Solution().minDeletions(s="ceabaacb") == 2
