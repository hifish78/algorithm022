class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            next_ugly = min(u2, u3, u5)
            if next_ugly == u2:
                i2 += 1
            if next_ugly == u3:
                i3 += 1
            if next_ugly == u5:
                i5 += 1
            ugly.append(next_ugly)
            n -= 1
        return ugly[-1]

if __name__ == "__main__":
    sol = Solution()
    res = sol.nthUglyNumber(10)
    print(res)