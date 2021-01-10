# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
        return

    # 压STACK的顺序： 根，右， 左
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversal3(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        stack = []
        while root is not None or stack:
            if root is not None:
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return res
