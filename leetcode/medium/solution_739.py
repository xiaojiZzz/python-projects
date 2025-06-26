"""
每日温度
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，
下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
提示：
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, ans = [], [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while st and temperature > temperatures[st[-1]]:
                idx = st.pop()
                ans[idx] = i - idx
            st.append(i)
        return ans


"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st, ans = [], [0] * n
        for i in range(n - 1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            ans[i] = st[-1] - i if st else 0
            st.append(i)
        return ans
"""
