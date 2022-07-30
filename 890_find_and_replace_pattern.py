# https://leetcode.com/problems/find-and-replace-pattern/
from collections import defaultdict
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_map = defaultdict(list)
        for i, ch in enumerate(pattern):
            pattern_map[ch].append(i)

        results = []
        for word in words:
            word_pattern = [""] * len(word)
            word_map = {}

            to_add = True
            for i, lt in enumerate(word):
                if not to_add:
                    break
                if word_pattern[i]:
                    continue

                if lt in word_map:
                    to_add = False
                    break
                word_map[lt] = pattern[i]
                for j in pattern_map[pattern[i]]:
                    if word[j] not in word_map or word_map[word[j]] != pattern[i]:
                        to_add = False
                    else:
                        word_pattern[j] = pattern[i]

            if to_add:
                results.append(word)

        return results


if __name__ == '__main__':
    assert Solution().findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"],
                                            pattern="abb") == ["mee", "aqq"]
    assert Solution().findAndReplacePattern(words=["a", "b", "c"], pattern="a") == ["a", "b", "c"]
