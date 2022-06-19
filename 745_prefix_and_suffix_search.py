# https://leetcode.com/problems/prefix-and-suffix-search/
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = {}
        for i in range(len(words)):
            combinations = self._get_combinations(words[i])
            for k, v in dict.fromkeys(combinations, i).items():
                if k in self.words:
                    self.words[k] = max(v, self.words[k])
                else:
                    self.words[k] = v

    def _get_combinations(self, word):
        words = []
        for i in range(len(word) - 1, -1, -1):
            for j in range(len(word)):
                words.append(word[i:] + "#" + word[:j + 1])
        return words

    def f(self, prefix: str, suffix: str) -> int:
        print(self.words)
        return self.words.get(f"{suffix}#{prefix}", -1)
