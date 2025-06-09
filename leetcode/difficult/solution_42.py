"""
接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        left[0] = height[0]
        ans = 0
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        max_right = height[n - 1]
        for i in range(n - 2, 0, -1):
            max_right = max(max_right, height[i])
            ans += min(left[i], max_right) - height[i]
        return ans


"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max, right_max = height[0], height[n - 1]
        left, right = 0, n - 1
        ans = 0
        while left < right:
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                ans += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return ans
"""

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                mid_h = height[st.pop()]
                if not st:
                    break
                ans += (min(h, height[st[-1]]) - mid_h) * (i - st[-1] - 1)
            st.append(i)
        return ans

"""
