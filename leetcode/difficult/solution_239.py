"""
滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：
输入：nums = [1], k = 1
输出：[1]
提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = []
        n = len(nums)
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        ans.append(nums[queue[0]])
        for i in range(k, n):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            while i - queue[0] >= k:
                queue.pop(0)
            ans.append(nums[queue[0]])
        return ans


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        ans.append(-q[0][0])
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans
