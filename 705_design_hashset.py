# https://leetcode.com/problems/design-hashset/


class MyHashSetIndexBased:

    def __init__(self):
        self.map = [0 for _ in range(10 ** 6 + 1)]

    def add(self, key: int) -> None:
        self.map[key] = 1

    def remove(self, key: int) -> None:
        self.map[key] = 0

    def contains(self, key: int) -> bool:
        return bool(self.map[key])


class MyHashSetSetBased:

    def __init__(self):
        self.map = set()

    def add(self, key: int) -> None:
        self.map.add(key)

    def remove(self, key: int) -> None:
        self.map.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.map
