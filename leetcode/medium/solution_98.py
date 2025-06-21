"""
验证二叉搜索树
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1：
输入：root = [2,1,3]
输出：true
示例 2：
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
提示：
树中节点数目范围在[1, 104] 内
-231 <= Node.val <= 231 - 1
"""
from math import inf
from typing import Optional

from treenode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower: float = -inf, upper: float = inf) -> bool:
        if root is None:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)


"""
class Solution:
    def __init__(self):
        self.pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
"""

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[1] != inf

    def dfs(self, node: Optional[TreeNode]) -> tuple:
        if node is None:
            return inf, -inf
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        x = node.val
        if x <= left[1] or x >= right[0]:
            return -inf, inf
        return min(left[0], x), max(right[1], x)
"""
