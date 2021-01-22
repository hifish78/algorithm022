from typing import List


class Solution:
    # https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-3/

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # [left, right] 递增，直接返回
            if nums[left] <= nums[right]:
                return nums[left]

            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                left = mid + 1  # NOT include mid
            else:
                right = mid  # MUST include mid (不能排除mid)
        return -1

