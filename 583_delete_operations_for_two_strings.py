# https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return len(word1) + len(word2) - 2 * dp[-1][-1]


if __name__ == '__main__':
    assert Solution().minDistance(word1="sea", word2="eat") == 2
    assert Solution().minDistance(word1="leetcode", word2="etco") == 4
    assert Solution().minDistance(word1="q", word2="etcoaaa") == 8
    assert Solution().minDistance(word1="aa", word2="etcoaaa") == 5
    assert Solution().minDistance(word1="park", word2="spake") == 3
