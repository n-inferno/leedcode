# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
from helpers import ListNode, to_linked_list


class Solution:
    # intuitive
    def getDecimalValue(self, head: ListNode) -> int:
        number = ''
        while head:
            number += str(head.val)
            head = head.next
        return int(number, base=2)

    # space O(1)
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next

        return num


if __name__ == '__main__':
    solution = Solution()
    assert solution.getDecimalValue(head=to_linked_list([1, 0, 1])) == 5
    assert solution.getDecimalValue(head=to_linked_list([0])) == 0
    assert solution.getDecimalValue(head=to_linked_list([1])) == 1
    assert solution.getDecimalValue(head=to_linked_list([1, 0])) == 2
