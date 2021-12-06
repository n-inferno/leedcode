class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head):
    node = head
    lst = []
    while node:
        lst.append(node.val) if node.val else None
        node = node.next
    return lst


def to_linked_list(lst):
    if len(lst) <= 1:
        return ListNode()
    head = node = ListNode(lst[0])
    for i in range(1, len(lst)):
        node.next = ListNode(lst[i])
        node = node.next

    return head
