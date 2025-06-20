"""
对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""
from typing import Optional

from treenode import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSym(root.left, root.right)

    def isSym(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return self.isSym(a.left, b.right) and self.isSym(a.right, b.left)
