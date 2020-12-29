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

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        counter = collections.Counter(nums)

        # 1:3, 2:2, 3:1
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))

        for _ in range(k):
            tmp = heapq.heappop(heap)
            res.append(tmp[1])
        return res