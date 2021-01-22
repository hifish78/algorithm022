from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        dic_change = {'A': 'CGT',
                      'C': 'AGT',
                      'G': 'ACT',
                      'T': 'ACG'}
        if end not in bank:
            return -1

        queue = deque()
        queue.append((start, 0))

        while queue:
            node = queue.popleft()
            if node[0] == end:
                return node[1]

            for index, val in enumerate(node[0]):
                for ch in dic_change[val]:
                    new = node[0][:index] + ch + node[0][index + 1:]
                    if new in bank:
                        queue.append((new, node[1] + 1))
                        bank.remove(new)
        return -1

if __name__ == '__main__':
    sol = Solution()
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    res = sol.minMutation(start, end, bank)
    print(res)