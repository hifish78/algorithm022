from typing import List

class Solution:
    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    # Solution#1
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits is None or len(digits) == 0:
            return res
        self.dfs(digits, 0, "", res)
        return res

    def dfs(self, digits, index, item, res):
        if len(item) == len(digits):
            res.append(item)
            return

        for ch in self.dic[digits[index]]:
            self.dfs(digits, index + 1, item + ch, res)

    # Solution2
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits is None or len(digits) == 0:
            return res

        self.dfs(digits, 0, "", res)
        return res

    def dfs(self, digits, index, item, res):
        # terminator (index --> level)
        if index == len(digits):
            res.append(item)
            return

        # current level (index)
        for ch in self.dic[digits[index]]:
            self.dfs(digits, index + 1, item + ch, res)