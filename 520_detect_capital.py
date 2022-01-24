# https://leetcode.com/problems/detect-capital/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_range = range(65, 91)
        met_capital = 0
        first_capital = False
        for i in range(len(word)):
            if ord(word[i]) in capital_range:
                if i == 0:
                    first_capital = True
                met_capital += 1
            elif met_capital > 1:
                return False

        return met_capital == 0 or met_capital == len(word) or (first_capital and met_capital == 1)


if __name__ == '__main__':
    solution = Solution()
    assert solution.detectCapitalUse(word="USA") == True
    assert solution.detectCapitalUse(word="leetcode") == True
    assert solution.detectCapitalUse(word="Flag") == True
    assert solution.detectCapitalUse(word="FlaG") == False
    assert solution.detectCapitalUse(word="mL") == False
    assert solution.detectCapitalUse(word="Leetcode") == True
    assert solution.detectCapitalUse(word="FFFFFFFFFFFFFFFFFFFFf") == False
