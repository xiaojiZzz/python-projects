"""
二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：
输入：root = [1]
输出：[[1]]
示例 3：
输入：root = []
输出：[]
提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Optional, List

from treenode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        queue = deque([root])
        while queue:
            size = len(queue)
            l = []
            for _ in range(size):
                node = queue.popleft()
                l.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(l)
        return ans


"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.levelTraversal(root, ans, 0)
        return ans

    def levelTraversal(self, node: Optional[TreeNode], ans: List[List[int]], level: int) -> None:
        if node is None:
            return None
        if len(ans) == level:
            ans.append([])
        ans[level].append(node.val)
        self.levelTraversal(node.left, ans, level + 1)
        self.levelTraversal(node.right, ans, level + 1)
"""
