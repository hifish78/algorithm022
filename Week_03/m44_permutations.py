from typing import List


class Solution:
    # Time Complexity: O(N * N!)
    # Initially we have N choices, and in each choice we have (N - 1) choices,
    # and so on. Notice that at the end when adding the list to the result list, it takes O(N).
    # So the time complexity should be N x N!.

    # Space Complexity: O(N!) since one has to keep N! Solution
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if nums is None:
            return res
        visited = [False] * len(nums)
        self.dfs(nums, [], res, visited)
        return res

    def dfs(self, nums, item, res, visited):
        if len(item) == len(nums):
            res.append(list(item))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            item.append(nums[i])
            visited[i] = True
            self.dfs(nums, item, res, visited)
            visited[i] = False
            item.pop()

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3]
    res = sol.permute(nums)
    print(res)

