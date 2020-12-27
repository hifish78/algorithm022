import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        # 1: 3; 2: 2, 3:1
        res = []
        heap = []
        # -3:1, -2:2, -1:3
        for i in set(nums):
            heapq.heappush(heap, (-1 * counts[i], i))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res