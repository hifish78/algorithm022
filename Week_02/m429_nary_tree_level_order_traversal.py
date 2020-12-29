
# Definition for a Node.
from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            for _ in range(len(queue)):
                item = queue.popleft()
                level.append(item.val)
                for child in item.children:
                    if child is not None:
                        queue.append(child)
            res.append(level)
        return res