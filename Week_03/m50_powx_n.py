class Solution:
    # 时间复杂度：O(logN)，即为递归的层数
    # Space: O(logN), 即为递归的层数。这是由于递归的函数调用会使用栈空间。
    def myPow(self, x: float, n: int) -> float:
        # terminator
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n
        return self.half_pow(x, n)

    def half_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        half = self.half_pow(x, n // 2)  # in python3, must use "n // 2"
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x