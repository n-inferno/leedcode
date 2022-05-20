# https://leetcode.com/problems/linked-list-cycle-ii/
from typing import Optional

from helpers import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            if hasattr(head, "visited"):
                return head
            head.visited = True
            head = head.next
