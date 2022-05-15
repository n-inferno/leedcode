# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

from helpers import ListNode, to_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        counter = 0
        node = head
        while node:
            counter += 1
            node = node.next

        stack = []
        mid = counter // 2
        skipped = counter % 2 != 0
        while head:
            if mid > 0:
                stack.append(head.val)
                mid -= 1
            elif skipped:
                skipped = False
            else:
                if stack and stack[-1] == head.val:
                    stack.pop()
                else:
                    return False

            head = head.next

        return not stack


if __name__ == '__main__':
    assert Solution().isPalindrome(to_linked_list([1, 2, 2, 1]))
    assert not Solution().isPalindrome(to_linked_list([1, 2, 3, 1]))
    assert Solution().isPalindrome(to_linked_list([1, 2, 3, 2, 1]))
    assert not Solution().isPalindrome(to_linked_list([1, 2, 3, 4, 1]))
    assert Solution().isPalindrome(to_linked_list([]))
    assert Solution().isPalindrome(to_linked_list([1]))
    assert not Solution().isPalindrome(to_linked_list([1, 2]))
    assert Solution().isPalindrome(to_linked_list([1, 1]))
