from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, n, "", res)
        return res

    # left - remaining left parenthesis
    # right - remaining right parenthesis
    # 括号合法性：
    # Left 随时可以加，只要有剩余的左括号给你用 left > 0
    # right必须之前有左括号， 也就是剩余的左括号比右括号少，也就是说RIGHT之前有左括号
    def helper(self, left: int, right: int, item: str, res: List[str]) -> None:
        if left == 0 and right == 0:
            res.append(item)
            return

        if left > 0:
            self.helper(left - 1, right, item + "(", res)
        if left < right:
            self.helper(left, right - 1, item + ")", res)

    def generateParenthesis2(self, n: int) -> List[str]:
        res = []
        self.helper2(0, 0, n, "", res)
        return res

    # left : 用掉的左括号的个数
    # right： 用掉的右括号的个数
    def helper2(self, left, right, n, item, res):
        if left == n and right == n:
            res.append(item)
            return
        if left < n:
            self.helper(left + 1, right, n, item + "(", res)
        if left > right:
            self.helper(left, right + 1, n, item + ")", res)


