# https://leetcode.com/problems/insertion-sort-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node.next:
            value = node.next.val
            copy_head = head
            if value <= head.val:
                head = ListNode(value, copy_head)
            else:
                while copy_head != node:
                    if copy_head.next and copy_head.next.val >= value:
                        copy_head.next = ListNode(value, copy_head.next)
                        break
                    copy_head = copy_head.next
                else:
                    node = node.next
                    continue
            node.next = node.next.next

        return head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.insertionSortList(head=to_linked_list([4, 2, 1, 3]))) == [1, 2, 3, 4]
    assert to_list(solution.insertionSortList(head=to_linked_list([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
    assert to_list(solution.insertionSortList(head=to_linked_list([1]))) == [1]
    assert to_list(solution.insertionSortList(head=to_linked_list([2, 1]))) == [1, 2]

