class Solution:
    def canJump(self, nums):
        if len(nums) < 2:
            return True
        if 0 not in nums: # 如果没有0， 至少可以走一步，一定可以到达最后
            return True
        max_distance = nums[0] # 设定可以到达的最大坐标
        for i in range(1, len(nums)):
            if i > max_distance: #最远都到不达这个节点，应该return FALSe
                return False
            # i <= max_distance; # 表示当前坐标可以到达
            max_distance = max(max_distance, i + nums[i])  # 更新可以到达的最远坐标
        return max_distance >= len(nums) - 1