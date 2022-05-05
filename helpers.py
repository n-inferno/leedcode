from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(to_list(self))


def to_list(head):
    node = head
    lst = []
    while node:
        lst.append(node.val) if node else None
        node = node.next
    return lst


def to_linked_list(lst):
    if len(lst) < 1:
        return ListNode()
    head = node = ListNode(lst[0])
    for i in range(1, len(lst)):
        node.next = ListNode(lst[i])
        node = node.next

    return head


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __repr__(self):
        return str(self.val)

    def to_array_representation(self):
        q = deque()
        q.append(self)
        repr = []

        while q:
            element = q.popleft()
            repr.append(element.val) if element else repr.append(element)
            if element:
                q.append(element.left)
                q.append(element.right)

        while repr and repr[-1] is None:
            repr.pop()
        return repr
