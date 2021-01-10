from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, index, subset, res):
        res.append(list(subset))
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.helper(nums, i + 1, subset, res)
            subset.pop()


    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = []  # can Not be "res = [[]]
        if nums is None:
            return [[]]
        self.dfs1(res, nums, [], 0)
        return res

    def dfs1(self, res, nums, item, index):
        # index 其实就是层（这一层的数字可选可不选）， 如果index == len(nums) 就意味着走到最末层了，应该退出了。
        if index == len(nums):
            res.append(list(item))
            return

        self.dfs1(res, nums, item, index + 1)  # not pick the number at the index, item不改变，直接去下一层
        item.append(nums[index])  # pick the number at the index， item 改变
        self.dfs1(res, nums, item, index + 1)
        # reverse the current state (since we change the parameter(item), it is not local variable, it change each layer' value)
        item.pop()

    # 增加一个数的时候，用 item + [nums[index]] 往下传递，这样虽然写起来简单，但是效率会低一些，因为每次都会创建一个新的数组。
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums is None:
            return [[]]
        self.dfs2(nums, [], 0, res)
        return res

    def dfs2(self, nums, item, index, res):
        if index == len(nums):
            res.append(list(item))
            return

        # NOT pick up the nums[index] number, item does NOT change and go to next level directly
        self.dfs2(nums, item, index + 1, res)
        # pick up the nums[index] number, item was changed locally, then go to next level
        self.dfs2(nums, item + [nums[index]], index + 1, res)


    def subsets3(self, nums: List[int]) -> List[List[int]]:
        # [[]] -> [], [1]
        res = [[]]
        for num in nums:
            newsets = []
            for subset in res:
                new_subset = subset + [num]
                newsets.append(new_subset)
            res.extend(newsets)   # <=> res = res + newsets
        return res

    def subsets4(self, nums):
        res = [[]]
        for num in nums:
            res = res + [ subset + [num] for subset in res]
        return res



nums = [1, 2, 3]
sol = Solution()
res = sol.subsets(nums)
print(res)