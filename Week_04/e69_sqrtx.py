class Solution:
    # 为什么可以用二分法？
    # 因为 y = x^2  (x > 0): 抛物线， 在Y轴右侧单调递增； 上下届
    # 二分查找必须是对排好序的序列
    def mySqrt(self, x: int) -> int:
        # can NOT remove x == 0 or x == 1 since we check left * left == x first
        if x == 0 or x == 1:
            return x

        left, right = 0, x
        if x == 0:
            return 0
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid
        # NOT left * left == x
        if left * left <= x:
            return int(left)
        if right * right <= x:
            return int(right)
        return -1

    def mySqrt2(self, x: int) -> int:
        left, right = 0, x
        if x == 0:
            return 0
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid
        # put right * right as first check, so no need to check x = 0 or x = 1
        if right * right <= x:
            return int(right)
        if left * left <= x:
            return int(left)
        return -1


