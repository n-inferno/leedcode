# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def __init__(self):
        self.var = 0
        self.from_start_node = None
        self.from_end_node = None

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def helper(node, count=1):
            if not node:
                return

            helper(node.next, count + 1)
            if count == k:
                self.from_start_node = node
            count -= 1
            self.var += 1
            if self.var == k:
                self.from_end_node = node

        if not head or not head.next:
            return head

        start_node = head
        helper(start_node)
        self.from_end_node.val, self.from_start_node.val = self.from_start_node.val, self.from_end_node.val
        return head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.swapNodes(head=to_linked_list([1, 2, 3, 4, 5]), k=2)) == [1, 4, 3, 2, 5]
    solution = Solution()
    assert to_list(solution.swapNodes(head=to_linked_list([7, 9, 6, 6, 7, 8, 3, 0, 9, 5]), k=5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9,
                                                                                                     5]
    solution = Solution()
    assert to_list(solution.swapNodes(head=to_linked_list([7, 6]), k=1)) == [6, 7]
    solution = Solution()
    assert to_list(solution.swapNodes(head=to_linked_list([100, 90]), k=2)) == [90, 100]
