from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 此题特别容易出错，注意和104求二叉树的最大深度比较。
#    1
#   /
#  2
# minDepth is 2 instead of 1 !!! it means root.left is None, it does NOT return 1. It should return left + 1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        # can NOT miss the below root.left is None or root.right is None
        # 如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度
        if root.left is None:
            return right + 1
        if root.right is None:
            return left + 1
        # 最后一种情况，也就是左右孩子都不为空，返回最小深度 + 1 即可
        return min(left, right) + 1

    def minDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = deque()
        queue.append(root)

        depth = 1  # 当前层的深度
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 肯定有下一层，如果没有早就return了
            depth += 1
        return depth
