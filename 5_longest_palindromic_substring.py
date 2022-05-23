# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longest_substring(left, right):
            while 0 <= left < len(s) and 0 <= right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        max_substring = s[0]
        for mid in range(len(s)):
            odd = longest_substring(mid, mid)
            max_substring = s[odd[0]: odd[1]] if odd[1] - odd[0] > len(max_substring) else max_substring
            even = longest_substring(mid, mid + 1)
            max_substring = s[even[0]: even[1]] if even[1] - even[0] > len(max_substring) else max_substring

        return max_substring


if __name__ == '__main__':
    assert Solution().longestPalindrome(s="babad") == "bab"
    assert Solution().longestPalindrome(s="cbbd") == "bb"
    assert Solution().longestPalindrome(s="aaaaaa") == "aaaaaa"
