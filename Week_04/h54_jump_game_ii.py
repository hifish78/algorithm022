from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 长度为0或者1，表示不用跳，直接返回0
        if len(nums) < 2:
            return 0

        max_distance = 0  # 记录从原点开始最远可以跳多远
        end = 0  # 记录用最少的跳跃次数可以跳多远
        res = 0  # 记录跳跃次数

        for i in range(len(nums)):
            max_distance = max(i + nums[i], max_distance)
            # 如果到达边界，那么就需要用能跳的最远的值更新边界
            if end == i:
                res += 1
                end = max_distance

                if end >= len(nums) - 1:
                    return res



