"""
二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
示例 1：
输入：root = [1,2,3,null,5,null,4]
输出：[1,3,4]
解释：
示例 2：
输入：root = [1,2,3,4,null,null,null,5]
输出：[1,3,4,5]
解释：
示例 3：
输入：root = [1,null,3]
输出：[1,3]
示例 4：
输入：root = []
输出：[]
提示:
二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional, List

from treenode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        queue = deque([root])
        while queue:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if size == 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
        return ans


"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return None
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return ans
"""
