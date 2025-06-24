"""
N 皇后
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：
输入：n = 1
输出：[["Q"]]
提示：
1 <= n <= 9
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [['.' for _ in range(n)] for _ in range(n)]

        def dfs(begin: int) -> None:
            if begin == n:
                ans.append([''.join(row) for row in queens])
                return None
            for i in range(n):
                queens[begin][i] = 'Q'
                if check(begin, i):
                    dfs(begin + 1)
                queens[begin][i] = '.'

        def check(i: int, j: int) -> bool:
            # 检查列冲突
            for k in range(i):
                if queens[k][j] == 'Q':
                    return False
            # 检查左上对角线
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                if queens[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1
            # 检查右上对角线
            x, y = i - 1, j + 1
            while x >= 0 and y < n:
                if queens[x][y] == 'Q':
                    return False
                x -= 1
                y += 1
            return True

        dfs(0)
        return ans
