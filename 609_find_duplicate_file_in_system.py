# https://leetcode.com/problems/find-duplicate-file-in-system/
from collections import defaultdict
from typing import List

if __name__ == '__main__':
    class Solution:
        def findDuplicate(self, paths: List[str]) -> List[List[str]]:
            dirs = defaultdict(list)
            for path in paths:
                rt, *files = path.split()
                for f in files:
                    file, content = f.split("(")
                    content = content.strip(")")
                    dirs[content].append(rt + "/" + file)

            return [d for d in dirs.values() if len(d) > 1]
