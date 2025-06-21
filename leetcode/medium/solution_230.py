"""
二叉搜索树中第 K 小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
提示：
树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
"""
from typing import Optional

from treenode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def inOrder(node: Optional[TreeNode]) -> None:
            nonlocal k
            if node is None or k == 0:
                return None
            inOrder(node.left)
            k -= 1
            if k == 0:
                nonlocal ans
                ans = node.val
            inOrder(node.right)

        inOrder(root)
        return ans


"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            left = inOrder(node.left)
            if left != -1:
                return left
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return inOrder(node.right)

        return inOrder(root)
"""
