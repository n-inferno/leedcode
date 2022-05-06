# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            else:
                stack.append([ch, 1])
            if stack[-1][1] == k:
                stack.pop()

        return "".join([item[0] * item[1] for item in stack])


if __name__ == '__main__':
    assert Solution().removeDuplicates(s="abcd", k=2) == "abcd"
    assert Solution().removeDuplicates(s="deeedbbcccbdaa", k=3) == "aa"
    assert Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2) == "ps"
