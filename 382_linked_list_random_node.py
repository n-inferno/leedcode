# https://leetcode.com/problems/linked-list-random-node/
import random
from typing import Optional

from helpers import ListNode, to_linked_list


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.range = []
        while head:
            self.range.append(head)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.range).val


if __name__ == '__main__':
    obj = Solution(to_linked_list([1, 2, 3]))
    param_1 = obj.getRandom()
    param_2 = obj.getRandom()
    param_3 = obj.getRandom()
    print(param_1, param_2, param_3)
