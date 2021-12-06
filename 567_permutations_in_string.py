# https://leetcode.com/problems/permutation-in-string/
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        i = 0
        items_map = defaultdict(int)
        map_items_counter = 0
        while i < len(s2):
            if s2[i] in counter:
                items_map[s2[i]] += 1
                map_items_counter += 1
                if map_items_counter == len(s1):
                    for k, v in items_map.items():
                        if counter[k] != v:
                            break
                    else:
                        return True
                    items_map[s2[i - map_items_counter + 1]] -= 1
                    map_items_counter -= 1
            else:
                items_map.clear()
                map_items_counter = 0

            i += 1

        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.checkInclusion(s1="ab", s2="eidbaooo") == True
    assert solution.checkInclusion(s1="ab", s2="eidboaoo") == False
    assert solution.checkInclusion(s1="abc", s2="abc") == True
    assert solution.checkInclusion(s1="abf", s2="abc") == False
    assert solution.checkInclusion(s1="bca", s2="aavabbabc") == True
