from collections import deque

# https://leetcode-cn.com/problems/invert-binary-tree/solution/di-gui-bfshe-dfsduo-chong-fang-shi-jie-jue-quan-bu/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 先递归调用，再交换
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root

    # 先交换，再递归调用
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree2(root.left)
        self.invertTree2(root.right)
        return root

    # BFS
    # 层次遍历，只要遍历树的所有节点，然后把他们的左右子树交换即可。
    def invertTree3(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            # 交换子节点
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    # DFS preorder
    def invertTree4(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root


    ## WRONG solution !!! since root is changed. Finally return None. So if you want to use DFS, use invertTree4
    def invertTree5(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        stack = []
        while root is not None or stack:
            if root is not None:
                root.left, root.right = root.right, root.left
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return root