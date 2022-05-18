# https://leetcode.com/problems/design-linked-list/
from helpers import ListNode, to_list


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        node = self.head
        pointer = 0
        while node and pointer < index:
            node = node.next
            pointer += 1

        return node.val

    def addAtHead(self, val: int) -> None:
        self.head, tmp = ListNode(val), self.head
        self.head.next = tmp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        to_add = ListNode(val)
        if not self.head:
            self.head = to_add
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = to_add
        self.size += 1

    def _find_node_before_index(self, index: int) -> ListNode:
        node = self.head
        while index > 1:
            node = node.next
            index -= 1
        return node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size:
            return self.addAtTail(val)

        node = self._find_node_before_index(index)
        tmp = node.next
        node.next = ListNode(val, tmp)

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size - 1:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        node = self._find_node_before_index(index)
        if not node.next:
            node.next = None
        else:
            node.next = node.next.next

        self.size -= 1

