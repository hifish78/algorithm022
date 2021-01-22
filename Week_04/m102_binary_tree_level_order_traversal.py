from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Time: O(N) since eache node is processed exactly once
    # Space: O(N) to keep the output structure which contains N node values
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            item = []
            for i in range(size):
                node = queue.popleft()
                item.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(item))
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res

        queue = [root]

        while queue:
            child = []
            node = []
            for item in queue:
                child.append(item.val)
                if item.left:
                    node.append(item.left)
                if item.right:
                    node.append(item.right)
            res.append(child)
            queue = node
        return res

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res

        queue = [root]

        while queue:
            size = len(queue)
            item = []
            for i in range(size):
                node = queue.pop(0)
                item.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list(item))
        return res