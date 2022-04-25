# https://leetcode.com/problems/peeking-iterator/


class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        self.next_value = iterator.next() if iterator.hasNext() else None
        self.iterator = iterator

    def peek(self):
        return self.next_value

    def next(self):
        tmp = self.next_value
        self.next_value = self.iterator.next() if self.iterator.hasNext() else None
        return tmp

    def hasNext(self):
        return self.next_value is not None
