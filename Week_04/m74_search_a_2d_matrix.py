from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # 将一维坐标变成二维坐标
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False