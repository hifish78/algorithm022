from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: 'Node', res: List):
        if root is None:
            return
        res.append(root.val)
        for child in root.children:
            self.helper(child, res)
        return