import sys
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            level_max = -sys.maxsize - 1

            for i in range(size):
                node = queue.popleft()
                if node.val > level_max:
                    level_max = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_max)
        return res

    # DFS
    # res只存每层最大值，树有几层，res长度就为几。( res[level] = max(res[level], node.val)
    # res的索引和层级level的索引相对应。
    # 递归比较节点node与node所处层级目前最大值(res[level]),找出该层最大，并赋值给res[level]
    def largestValues2(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        self.dfs(root, res, 0)
        return res

    def dfs(self, node, res, level):
        if node is None:
            return

        if level == len(res):
            res.append(node.val)
        else:
            res[level] = max(res[level], node.val)

        self.dfs(node.left, res, level + 1)
        self.dfs(node.right,res,  level + 1)
