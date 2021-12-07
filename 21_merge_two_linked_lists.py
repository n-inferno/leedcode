# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

from helpers import ListNode, to_list, to_linked_list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = result_node = ListNode()
        first = True
        while list1 and list2:
            if list1.val >= list2.val:
                result_node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                result_node.next = ListNode(list1.val)
                list1 = list1.next
            if first:
                result = result.next
                first = False
            result_node = result_node.next

        if list1:
            result_node.next = list1
        elif list2:
            result_node.next = list2
        if first:
            result = result.next

        return result


if __name__ == '__main__':
    solution = Solution()
    assert to_list(solution.mergeTwoLists(list1=to_linked_list([1, 2, 4]), list2=to_linked_list([1, 3, 4]))) \
           == [1, 1, 2, 3, 4, 4]
    assert to_list(solution.mergeTwoLists(list1=to_linked_list([]), list2=to_linked_list([]))) \
           == []
    assert to_list(solution.mergeTwoLists(list1=to_linked_list([]), list2=to_linked_list([0]))) \
           == [0]
    assert to_list(solution.mergeTwoLists(list1=to_linked_list([1]), list2=to_linked_list([0, 1, 2]))) \
           == [0, 1, 1, 2]
