"""
电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：
输入：digits = ""
输出：[]
示例 3：
输入：digits = "2"
输出：["a","b","c"]
提示：
0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。
"""
from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ss = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []
        ans = []
        s = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(s))
                return None
            string = ss[int(digits[i])]
            for c in string:
                s.append(c)
                dfs(i + 1)
                s.pop()

        dfs(0)
        return ans


"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ss = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        if n == 0:
            return []
        ans = deque([""])
        for i in range(n):
            string = ss[int(digits[i])]
            size = len(ans)
            for j in range(size):
                tmp = ans.popleft()
                for c in string:
                    ans.append(tmp + c)
        return list(ans)
"""
