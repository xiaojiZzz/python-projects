"""
二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：
输入：root = []
输出：[]
示例 3：
输入：root = [1]
输出：[1]
提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
from typing import Optional, List

from treenode import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def inOrder(treenode: Optional[TreeNode]) -> None:
            if treenode is None:
                return None
            inOrder(treenode.left)
            inorder.append(treenode.val)
            inOrder(treenode.right)

        inOrder(root)
        return inorder


"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        if not root:
            return inorder
        st = []
        while root or st:
            while root:
                st.append(root)
                root = root.left
            root = st.pop()
            inorder.append(root.val)
            root = root.right
        return inorder
"""
