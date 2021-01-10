# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = []
        last = None
        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                if last is not None and last.val >= tmp.val:
                    return False
                last = tmp
                root = tmp.right
        return True

    # Solution2
    last = None
    def isValidBST2(self, root: TreeNode) -> bool:
        if root is None:
            return True

        if not self.isValidBST2(root.left):
            return False
        if self.last is not None and self.last.val >= root.val:
            return False
        self.last = root
        if not self.isValidBST2(root.right):
            return False
        return True
