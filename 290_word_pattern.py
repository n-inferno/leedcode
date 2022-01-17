# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        map = {}
        seen = set()
        for p, w in zip(pattern, words):
            if p not in map and w not in seen:
                map[p] = w
                seen.add(w)
            if not map.get(p) == w:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    assert solution.wordPattern(pattern="abba", s="dog cat cat dog") == True
    assert solution.wordPattern(pattern="abba", s="dog cat cat fish") == False
    assert solution.wordPattern(pattern="aaaa", s="dog cat cat dog") == False
    assert solution.wordPattern(pattern="abba", s="dog dog dog dog") == False
    assert solution.wordPattern(pattern="jquery", s="jquery") == False
