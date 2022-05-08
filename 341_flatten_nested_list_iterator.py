# https://leetcode.com/problems/flatten-nested-list-iterator/
from collections import deque


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nested_list = deque(self.toSimpleList(nestedList))

    def toSimpleList(self, nested_list):
        result = []

        def helper(nested):
            nonlocal result
            if not isinstance(nested, list) and nested.isInteger():
                result.append(nested.getInteger())
            items = nested.getList() if not isinstance(nested, list) else nested
            for item in items:
                helper(item)

        helper(nested_list)
        return result

    def next(self) -> int:
        return self.nested_list.popleft()

    def hasNext(self) -> bool:
        return bool(self.nested_list)
