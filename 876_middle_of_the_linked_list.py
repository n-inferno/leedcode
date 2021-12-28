# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    # store nodes
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        return nodes[len(nodes) // 2]

    # two pointers
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        while head:
            head = head.next
            if head:
                head = head.next
                mid = mid.next

        return mid


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.middleNode(head=to_linked_list([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(solution.middleNode(head=to_linked_list([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    assert to_list(solution.middleNode(head=to_linked_list([1]))) == [1]
    assert to_list(solution.middleNode(head=to_linked_list([1, 2]))) == [2]
