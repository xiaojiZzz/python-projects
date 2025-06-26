"""
柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：
输入： heights = [2,4]
输出： 4
提示：
1 <= heights.length <=105
0 <= heights[i] <= 104
"""
from typing import List


class Solution:
    # 三次遍历
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [-1] * n, [n] * n
        st = []
        for i, height in enumerate(heights):
            while st and height < heights[st[-1]]:
                r[st.pop()] = i
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and heights[i] < heights[st[-1]]:
                l[st.pop()] = i
            st.append(i)
        ans = 0
        for i, height in enumerate(heights):
            ans = max(ans, (r[i] - l[i] - 1) * height)
        return ans


"""
class Solution:
    # 两次遍历
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = [-1] * n, [n] * n
        st = []
        for i, height in enumerate(heights):
            while st and height < heights[st[-1]]:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        ans = 0
        for i, height in enumerate(heights):
            ans = max(ans, (r[i] - l[i] - 1) * height)
        return ans


class Solution:
    # 一次遍历
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # 最后大火收汁，用 -1 把栈清空（-1 可以改成 0）
        st = [-1]  # 在栈中只有一个数的时候，栈顶的「下面那个数」是 -1，对应 left[i] = -1 的情况
        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and h <= heights[st[-1]]:
                i = st.pop()  # 矩形的高（的下标）
                left = st[-1]  # 栈顶下面那个数就是 left
                ans = max(ans, heights[i] * (right - left - 1))
            st.append(right)
        return ans
"""
