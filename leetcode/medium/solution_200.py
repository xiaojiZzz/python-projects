"""
岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""
from collections import deque
from typing import List, Deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == '0':
                return None
            grid[x][y] = '0'
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x - 1, y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans


"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    ans += 1
                    grid[i][j] = '0'
                    queue = deque([i * col + j])
                    while queue:
                        idx = queue.popleft()
                        r = idx // col
                        c = idx % col
                        if r - 1 >= 0 and grid[r - 1][c] == '1':
                            queue.append((r - 1) * col + c)
                            grid[r - 1][c] = '0'
                        if r + 1 < row and grid[r + 1][c] == '1':
                            queue.append((r + 1) * col + c)
                            grid[r + 1][c] = '0'
                        if c - 1 >= 0 and grid[r][c - 1] == '1':
                            queue.append(r * col + c - 1)
                            grid[r][c - 1] = '0'
                        if c + 1 < col and grid[r][c + 1] == '1':
                            queue.append(r * col + c + 1)
                            grid[r][c + 1] = '0'
        return ans
"""