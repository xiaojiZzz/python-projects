"""
最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：
输入：nums = [1,0,1,2]
输出：3
提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num - 1 in s:
                continue
            n = num + 1
            while n in s:
                n += 1
            ans = max(ans, n - num)
        return ans


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0
        for num in nums:
            if num in mp.keys():
                continue
            # 这里不能直接 left = mp[num - 1] 因为会执行 mp[num - 1] = 0 操作，将键值对插入到字典中
            left = mp[num - 1] if num - 1 in mp.keys() else 0
            right = mp[num + 1] if num + 1 in mp.keys() else 0
            length = left + right + 1
            mp[num] = 1
            mp[num - left] = length
            mp[num + right] = length
            ans = max(ans, length)
        return ans
"""
