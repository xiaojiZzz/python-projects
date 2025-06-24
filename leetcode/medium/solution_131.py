"""
分割回文串
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
示例 1：
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：
输入：s = "a"
输出：[["a"]]
提示：
1 <= s.length <= 16
s 仅由小写英文字母组成
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans, path = [], []

        def dfs(begin: int) -> None:
            if begin == n:
                ans.append(path[:])
                return None
            for i in range(begin, n):
                string = s[begin: i + 1]
                if string == string[::-1]:
                    path.append(s[begin: i + 1])
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return ans
