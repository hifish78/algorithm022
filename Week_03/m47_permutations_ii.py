from typing import List


class Solution:
    # Time Complexity: O(N * N!)
    # Initially we have N choices, and in each choice we have (N - 1) choices,
    # and so on. Notice that at the end when adding the list to the result list, it takes O(N).
    # So the time complexity should be N x N!.

    # Space Complexity: O(N!) since one has to keep N! Solution
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums is None or len(nums) == 0:
            return res

        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, item, res, visited):
        if len(nums) == len(item):
            res.append(list(item))
            return

        # 1, 1', 2
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i - 1 >= 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            item.append(nums[i])
            visited[i] = True
            self.dfs(nums, item, res, visited)
            visited[i] = False
            item.pop()