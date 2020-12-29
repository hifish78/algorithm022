# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: List) -> None:
        if root is None:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)