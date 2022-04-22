# https://leetcode.com/problems/design-hashmap/


class MyHashMap:

    def __init__(self):
        self.storage = [None for _ in range(10 ** 6 + 1)]

    def put(self, key: int, value: int) -> None:
        self.storage[key] = value

    def get(self, key: int) -> int:
        value = self.storage[key]
        return value if value is not None else -1

    def remove(self, key: int) -> None:
        self.storage[key] = None
