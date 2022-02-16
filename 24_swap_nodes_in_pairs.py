# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node and node.next:
            if prev is None:
                head = head.next
                prev = head.next
                head.next = node
                head.next.next = prev
            else:
                prev = node.next
                node.next = node.next.next
                temp = node.next.next if node.next else None
                if node.next:
                    node.next.next = prev
                    node.next.next.next = temp
                    node = node.next.next
                else:
                    node.next = prev
                    node.next.next = temp
                    node = node.next

        return head


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.swapPairs(to_linked_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert to_list(solution.swapPairs(to_linked_list([1]))) == [1]
    assert to_list(solution.swapPairs(to_linked_list([1, 2, 3]))) == [2, 1, 3]
