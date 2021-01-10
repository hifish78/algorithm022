from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/dong-hua-yan-shi-105-cong-qian-xu-yu-zhong-xu-bian/
Time: O(n^2) : list.index(x) --> O(N)
Space: O(N), since we store the entire tree
'''
class Solution:

    # Best Solution
    # Time: O(N)
    # Space: O(N) since we store the entire tree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        self.pre_idx = 0
        self.idx_dic = {val: idx for idx, val in enumerate(inorder)}
        return self.helper(preorder, inorder, 0, len(inorder))

    def helper(self, preorder, inorder, in_left, in_right):
        if in_left == in_right:
            return None
        root_val = preorder[self.pre_idx]
        root = TreeNode(root_val)

        index = self.idx_dic[root_val]

        self.pre_idx += 1
        root.left = self.helper(preorder, inorder, in_left, index)
        root.right = self.helper(preorder, inorder, index + 1, in_right)
        return root

    # Solution1
    def buildTree1(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid_idx = inorder.index(preorder[0])
        root.left = self.buildTree1(preorder[1:mid_idx + 1], inorder[0:mid_idx])
        root.right = self.buildTree1(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        return root

    # Solution2
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    # 字符串截取存在性能消耗，没必要每次都切割。用两个指针表示即可。递归函数传指针。
    def helper(self, preorder, p_start, p_end, inorder, i_start, i_end):
        if p_start > p_end:
            return None
        root = TreeNode(preorder[p_start])  # root
        mid_idx = inorder.index(preorder[p_start])  # root 结点在inorder的位置
        left_num = mid_idx - i_start  # 左子树的节点数
        root.left = self.helper(preorder, p_start + 1, p_start + left_num,
                                inorder, i_start, mid_idx - 1)
        root.right = self.helper(preorder, p_start + left_num + 1, p_end,
                                 inorder, mid_idx + 1, i_end)
        return root

    # Solution3
    def buildTree3(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        if inorder:
            mid_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[mid_idx])
            root.left = self.buildTree3(preorder, inorder[:mid_idx])
            root.right = self.buildTree3(preorder, inorder[mid_idx + 1:])
            return root

    # Solution4
    # indexOf 的使用导致每次递归都花 O(n) 的时间定位根节点的位置，不理想。
    # 可以提前把inorder的元素和索引存在HASH中，空间换时间
    def buildTree4(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i

        return self.helper4(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    # 字符串截取存在性能消耗，没必要每次都切割。用两个指针表示即可。递归函数传指针。
    def helper4(self, preorder, p_start, p_end, inorder, i_start, i_end):
        if p_start > p_end:
            return None
        root = TreeNode(preorder[p_start])  # root
        # mid_idx = inorder.index(preorder[p_start]) # root 结点在inorder的位置
        mid_idx = self.dic[preorder[p_start]]
        left_num = mid_idx - i_start  # 左子树的节点数
        root.left = self.helper4(preorder, p_start + 1, p_start + left_num,
                                inorder, i_start, mid_idx - 1)
        root.right = self.helper4(preorder, p_start + left_num + 1, p_end,
                                 inorder, mid_idx + 1, i_end)
        return root


