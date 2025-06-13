"""
最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：
输入：nums = [1]
输出：1
示例 3：
输入：nums = [5,4,-1,7,8]
输出：23
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm = 0
        ans = nums[0]
        for num in nums:
            sm = max(sm, 0) + num
            ans = max(ans, sm)
        return ans


"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = nums[0]
        for i in range(1, n):
            dp[i] = max(0, dp[i - 1]) + nums[i]
            ans = max(ans, dp[i])
        return ans
"""

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        def maxSubArraySum(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            return max(maxSubArraySum(left, mid), maxSubArraySum(mid + 1, right), maxCrossingSum(left, mid, right))

        def maxCrossingSum(left: int, mid: int, right: int) -> int:
            sum_left = -float('inf')
            sm = 0
            for i in range(mid, left - 1, -1):
                sm += nums[i]
                sum_left = max(sm, sum_left)
            sm = 0
            sum_right = -float('inf')
            for i in range(mid + 1, right + 1):
                sm += nums[i]
                sum_right = max(sm, sum_right)
            return sum_left + sum_right

        return maxSubArraySum(0, n - 1)
"""
