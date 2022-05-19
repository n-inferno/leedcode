# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

from helpers import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            if slow == fast:
                return True

        return False
