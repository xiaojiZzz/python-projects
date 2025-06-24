"""
括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：
输入：n = 1
输出：["()"]
提示：
1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, path = [], []

        def dfs(l: int, r: int) -> None:
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return None
            if l < n:
                path.append('(')
                dfs(l + 1, r)
                path.pop()
            if r < l:
                path.append(')')
                dfs(l, r + 1)
                path.pop()

        dfs(0, 0)
        return ans
