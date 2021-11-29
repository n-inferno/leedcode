# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return version >= 4


class Solution:
    def firstBadVersion(self, n):
        lower, upper = 1, n
        while True:
            if upper - lower <= 1:
                return lower if isBadVersion(lower) else upper
            mid = (lower + upper) // 2
            if isBadVersion(mid):
                upper = mid
            else:
                lower = mid


if __name__ == '__main__':
    solution = Solution()
    assert solution.firstBadVersion(n=5) == 4
    # assert solution.firstBadVersion(n=1, bad=1) == 1
