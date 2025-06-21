"""
从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
示例 1:
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]
提示:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列
"""
from typing import List, Optional

from treenode import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {x: i for i, x in enumerate(inorder)}
        n = len(preorder)

        def build(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
            if pre_l > pre_r:
                return None
            root = TreeNode(preorder[pre_l])
            in_root = idx[preorder[pre_l]]
            size_l = in_root - in_l
            root.left = build(pre_l + 1, pre_l + size_l, in_l, in_root - 1)
            root.right = build(pre_l + size_l + 1, pre_r, in_root + 1, in_r)
            return root

        return build(0, n - 1, 0, n - 1)
