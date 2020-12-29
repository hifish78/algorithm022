from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = [-1, -1]
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dic:
                res[0] = dic[diff]
                res[1] = i
                return res
            dic[num] = i
        return res

