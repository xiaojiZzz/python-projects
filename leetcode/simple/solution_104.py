"""
二叉树的最大深度
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：
输入：root = [1,null,2]
输出：2
提示：
树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional

from treenode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            while size > 0:
                treenode = queue.popleft()  # o(1) 时间弹出
                if treenode.left:
                    queue.append(treenode.left)
                if treenode.right:
                    queue.append(treenode.right)
                size -= 1
            ans += 1
        return ans
"""

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            depth += 1
            nonlocal ans
            ans = max(ans, depth)
            dfs(node.left, depth)
            dfs(node.right, depth)

        dfs(root, 0)
        return ans
"""
