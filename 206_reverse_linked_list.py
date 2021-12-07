# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_node = result = None

        def helper(head):
            nonlocal result_node, result
            if not head:
                return
            helper(head.next)
            if not result_node:
                result_node = result = ListNode(head.val)
            else:
                result_node.next = ListNode(head.val)
                result_node = result_node.next

        helper(head)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.reverseList(head=to_linked_list([1, 1, 2, 3, 4, 4]))) == [4, 4, 3, 2, 1, 1]
    assert to_list(solution.reverseList(head=to_linked_list([]))) == []
    assert to_list(solution.reverseList(head=to_linked_list([1]))) == [1]
    assert to_list(solution.reverseList(head=to_linked_list([1, 2]))) == [2, 1]
