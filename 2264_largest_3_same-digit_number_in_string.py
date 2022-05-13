# https://leetcode.com/problems/largest-3-same-digit-number-in-string/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        prev = num[0]
        counter = 1
        met_max_good = ""
        for i in range(1, len(num)):
            if num[i] == prev:
                counter += 1
            else:
                counter = 1
            prev = num[i]
            if counter == 3:
                if not met_max_good or met_max_good < prev:
                    met_max_good = prev

        return met_max_good * 3


if __name__ == '__main__':
    assert Solution().largestGoodInteger(num="6777133339") == "777"
    assert Solution().largestGoodInteger(num="2300019") == "000"
    assert Solution().largestGoodInteger(num="42352338") == ""
