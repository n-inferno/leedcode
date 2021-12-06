# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        nth_node = None
        i = 1
        while node:
            if i > n:
                nth_node = head if not nth_node else nth_node.next
            node = node.next
            i += 1

        if not nth_node:
            head = head.next
        elif nth_node and nth_node.next:
            nth_node.next = nth_node.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.removeNthFromEnd(head=to_linked_list([1, 2, 3, 4, 5]), n=2)) == [1, 2, 3, 5]
    assert to_list(solution.removeNthFromEnd(head=to_linked_list([1]), n=1)) == []
    assert to_list(solution.removeNthFromEnd(head=to_linked_list([1, 2]), n=1)) == [1]
    assert to_list(solution.removeNthFromEnd(head=to_linked_list([1, 2]), n=2)) == [2]
