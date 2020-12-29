
# Definition for a Node.
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: 'Node', res: List) -> List[int]:
        if root is None:
            return
        for child in root.children:
            self.helper(child, res)
        res.append(root.val)