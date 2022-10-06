# https://leetcode.com/problems/time-based-key-value-store/
from bisect import bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)  # key: [times]
        self.store = {}  # (key, time): value

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.store[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        i = bisect_right(self.times[key], timestamp)
        if i <= 0:
            return ""
        ts = self.times[key][i - 1]
        if ts > timestamp:
            return ""
        return self.store.get((key, ts)) or ""
