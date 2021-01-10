from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    # Time: O(N)
    # Space:
    # worst O(N): the tree is completely unbalanced, the height of the tree would be N
    # best O(LogN): the tree is completely balanced, the height of the tree would be log(N)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # BFS (using deque as Queue)
    # Time: O(N)
    # Space: 此方法空间的消耗取决于队列存储的元素数量，其在最坏情况下会达到 O(n)。
    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque()
        queue.append(root)

        level = 0
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return level

    #  BFS (use two lists)  --> very good!
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        level = [root]
        depth = 0

        while level:
            depth += 1
            queue = []
            for item in level:
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            level = queue
        return depth

    # BFS (use stack)
    def maxDepth3(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [root]
        depth = 0

        while stack:
            next_level = []
            while stack:
                top = stack.pop()
                if top.left:
                    next_level.append(top.left)
                if top.right:
                    next_level.append(top.right)
            stack = next_level
            depth += 1
        return depth