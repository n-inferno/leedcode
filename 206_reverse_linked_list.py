# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        def helper(head):
            nonlocal new_head

            if not head or not head.next:
                new_head = head
                return head

            node = helper(head.next)
            node.next = head
            head.next = None
            return head

        helper(head)
        return new_head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.reverseList(head=to_linked_list([1, 2]))) == [2, 1]
    assert to_list(solution.reverseList(head=to_linked_list([1, 1, 2, 3, 4, 4]))) == [4, 4, 3, 2, 1, 1]
    assert to_list(solution.reverseList(head=to_linked_list([1]))) == [1]
