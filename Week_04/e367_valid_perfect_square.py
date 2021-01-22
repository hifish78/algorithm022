class Solution:
    # num = x * x
    # Time: O(logN)
    # Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid
            else:
                right = mid

        if right * right == num:
            return True
        if left * left == num:
            return True
        return False