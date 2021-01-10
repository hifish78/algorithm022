from typing import List


class Solution:
    # Time: O(n)
    # Space: O(n)
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > len(nums) // 2:
                return num
        return -1

    # space: O(logN) --> stack的深度
    # time： O(NlogN)
    def majorityElement2(self, nums: List[int]) -> int:
        res = self.helper(nums, 0, len(nums) - 1)
        return res

    def helper(self, nums, low, high):
        if low == high:
            return nums[low]

        mid = (high - low) // 2 + low
        left = self.helper(nums, low, mid)
        right = self.helper(nums, mid + 1, high)

        if left == right:
            return left

        left_cnt = 0
        right_cnt = 0
        for i in range(low, high + 1):
            if nums[i] == left:
                left_cnt += 1
            if nums[i] == right:
                right_cnt += 1

        return left if left_cnt > right_cnt else right

    # Space: O(logN)
    # Time: O(NlogN)
    # 题目说了出现次数最多的数一定超过长度的一半，排序之后取中间的数，如果满足题意则该数一定是出现次数最多的
    def majorityElement3(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
        # return sorted(nums)[len(nums) // 2]

nums = [3, 3, 4]
sol = Solution()
res = sol.majorityElement2(nums)
print(res)
