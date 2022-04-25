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
        self.peeked = False
        self.next_value = None
        self.iterator = iterator

    def peek(self):
        if not self.peeked:
            self.next_value = self.iterator.next()
            self.peeked = True
        return self.next_value

    def next(self):
        if self.peeked:
            self.peeked = False
            return self.next_value
        return self.iterator.next()

    def hasNext(self):
        return self.peeked or self.iterator.hasNext()
