# https://leetcode.com/problems/consecutive-characters/


class Solution:
    def maxPower(self, s: str) -> int:
        max_length = curr_length = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr_length += 1
            else:
                curr_length = 1
            max_length = max(max_length, curr_length)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxPower(s="leetcode") == 2
    assert solution.maxPower(s="abbcccddddeeeeedcba") == 5
    assert solution.maxPower(s="triplepillooooow") == 5
    assert solution.maxPower(s="hooraaaaaaaaaaay") == 11
    assert solution.maxPower(s="tourist") == 1
