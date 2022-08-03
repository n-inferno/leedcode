# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.action_ts = 0
        self.cache = {}  # k:v
        self.last_used = {}  # k:action_ts
        self.usages = OrderedDict()  # action_ts:k

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        last_k_usage = self.last_used[key]
        self.last_used[key] = self.action_ts
        self.usages.pop(last_k_usage, None)
        self.usages[self.action_ts] = key

        self.action_ts += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            k = self.usages.popitem(last=False)
            del self.last_used[k[1]]
            del self.cache[k[1]]

        self.cache[key] = value
        if key in self.last_used:
            last_used_k = self.last_used[key]
            del self.usages[last_used_k]

        self.last_used[key] = self.action_ts
        self.usages[self.action_ts] = key

        self.action_ts += 1
