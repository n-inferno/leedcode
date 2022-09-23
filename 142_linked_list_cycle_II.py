# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional

from helpers import ListNode


class Solution:
    # Floyd's algorithm
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return
            fast = fast.next
            if slow == fast:
                break
        else:
            return

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
