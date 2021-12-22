# https://leetcode.com/problems/reorder-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes_lst = []
        node = head
        while node:
            nodes_lst.append(node)
            node = node.next

        p1, p2 = 0, len(nodes_lst) - 1
        new_head = new = None
        while p1 < p2:
            if new is None:
                new = nodes_lst[p1]
                new_head = new
            else:
                new.next = nodes_lst[p1]
                new = new.next
            new.next = nodes_lst[p2]
            new = new.next
            p1 += 1
            p2 -= 1

        if p1 == p2 and new_head:
            new.next = nodes_lst[p2]
            new = new.next
        elif p1 == p2:
            new = new_head = nodes_lst[p2]
        new.next = None

        head = new_head
        return head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.reorderList(head=to_linked_list([1, 2, 3, 4]))) == [1, 4, 2, 3]
    assert to_list(solution.reorderList(head=to_linked_list([1, 2, 3, 4, 5]))) == [1, 5, 2, 4, 3]
    assert to_list(solution.reorderList(head=to_linked_list([1]))) == [1]
    assert to_list(solution.reorderList(head=to_linked_list([1, 2]))) == [1, 2]
