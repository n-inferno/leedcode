# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

from helpers import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False
