# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = track = None

        def helper(node):
            nonlocal result, track

            if not node:
                return

            helper(node.next)
            if not result:
                result = track = ListNode()
            track.val = node.val

            if node != head:
                track.next = ListNode()

            track = track.next

        helper(head)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.reverseList(head=to_linked_list([1, 1, 2, 3, 4, 4]))) == [4, 4, 3, 2, 1, 1]
    assert to_list(solution.reverseList(head=to_linked_list([]))) == []
    assert to_list(solution.reverseList(head=to_linked_list([1]))) == [1]
    assert to_list(solution.reverseList(head=to_linked_list([1, 2]))) == [2, 1]
