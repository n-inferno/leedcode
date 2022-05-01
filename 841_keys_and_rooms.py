# https://leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def visit(room_number):
            nonlocal rooms

            visited.add(room_number)
            for key in rooms[room_number]:
                if key not in visited:
                    visit(key)

        visit(0)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    assert Solution().canVisitAllRooms(rooms=[[1], [2], [3], []])
    assert not Solution().canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]])
