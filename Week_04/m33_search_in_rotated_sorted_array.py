from typing import List

# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/yi-wen-dai-ni-shua-bian-er-fen-cha-zhao-dtadq/
class Solution:
    # nums[0], nums[i], target
    # nums[0] <= nums[i], nums[0]到nums[i]为有序数组， 如果 nums[0] <= target <= nums[i], 那么我们应该在0-i之间查找
    # nums[0] > nums[i], 说明0-i区间的某个点处发生了下降，那么i+1 到最后一个数字的区间为有序数组

    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            # [0, mid]有序，
            if nums[0] <= nums[mid]:
                if nums[0] <= target and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # [0, mid]之间发生了旋转
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1