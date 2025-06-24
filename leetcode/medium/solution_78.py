"""
子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, path = [], []

        def dfs(begin: int) -> None:
            ans.append(path[:])
            for i in range(begin, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.remove(nums[i])

        dfs(0)
        return ans


"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            size = len(ans)
            for i in range(size):
                subset = ans[i][:]
                subset.append(num)
                ans.append(subset)
        return ans
"""

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        for i in range(1 << n):
            sub = []
            for j in range(n):
                if ((i >> j) & 1) == 1:
                    sub.append(nums[j])
            ans.append(sub)
        return ans
"""
