"""
螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        loc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = i = 0
        for _ in range(m * n):
            ans.append(matrix[x][y])
            matrix[x][y] = None
            if 0 <= x + loc[i][0] < m and 0 <= y + loc[i][1] < n and matrix[x + loc[i][0]][y + loc[i][1]] is not None:
                x += loc[i][0]
                y += loc[i][1]
            else:
                i = (i + 1) % 4
                x += loc[i][0]
                y += loc[i][1]
        return ans
