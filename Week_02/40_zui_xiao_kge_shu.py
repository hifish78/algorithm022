import heapq
from typing import List


class Solution:
    # NLogK
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return None

        res = []
        heap = []
        for a in arr:
            heapq.heappush(heap, a)

        for _ in range(k):
            tmp = heapq.heappop(heap)
            res.append(tmp)
        return res