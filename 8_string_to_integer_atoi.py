# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        result = ''
        positive = True
        previous_integer = False
        for i in s:
            if ord(i) in (45, 43) and not previous_integer:
                positive = False if ord(i) == 45 else True
            elif ord(i) not in range(48, 58):
                if i == ' ' and not previous_integer:
                    continue
                else:
                    break
            else:
                result += i
            previous_integer = True

        mult = 0
        integer = 0
        for i in range(len(result) - 1, -1, -1):
            integer += (ord(result[i]) - 48) * (10 ** mult)
            mult += 1

        integer = -integer if not positive else integer

        if integer < -2147483648:
            integer = -2147483648
        elif integer > 2147483647:
            integer = 2147483647

        return integer


if __name__ == '__main__':
    solution = Solution()
    assert solution.myAtoi(s="42") == 42
    assert solution.myAtoi(s="   -42") == -42
    assert solution.myAtoi(s="4193 with words") == 4193
    assert solution.myAtoi(s="words and 987") == 0
    assert solution.myAtoi(s="-91283472332") == -2147483648
    assert solution.myAtoi(s="00000-42a1234") == 0
    assert solution.myAtoi(s="  +  413") == 0
