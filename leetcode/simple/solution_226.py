"""
翻转二叉树
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
示例 2：
输入：root = [2,1,3]
输出：[2,3,1]
示例 3：
输入：root = []
输出：[]
提示：
树中节点数目范围在 [0, 100] 内
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional

from treenode import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            treenode = queue.popleft()
            treenode.left, treenode.right = treenode.right, treenode.left
            if treenode.left:
                queue.append(treenode.left)
            if treenode.right:
                queue.append(treenode.right)
        return root
"""
