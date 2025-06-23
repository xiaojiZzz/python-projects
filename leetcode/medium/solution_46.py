"""
全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]
输出：[[1]]
提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []

        def dfs() -> None:
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs()
                    path.remove(nums[i])

        dfs()
        return ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []
        for num in nums:
            path.append(num)

        def dfs(i: int) -> None:
            if i == len(nums):
                ans.append(path[:])
                return None
            for j in range(i, len(nums)):
                path[i], path[j] = path[j], path[i]
                dfs(i + 1)
                path[i], path[j] = path[j], path[i]

        dfs(0)
        return ans
