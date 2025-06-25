"""
寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        arr = [0] * (m + n)
        idx, idx1, idx2 = 0, 0, 0
        while idx1 < m and idx2 < n:
            if nums1[idx1] < nums2[idx2]:
                arr[idx] = nums1[idx1]
                idx += 1
                idx1 += 1
            else:
                arr[idx] = nums2[idx2]
                idx += 1
                idx2 += 1
        while idx1 < m:
            arr[idx] = nums1[idx1]
            idx += 1
            idx1 += 1
        while idx2 < n:
            arr[idx] = nums2[idx2]
            idx += 1
            idx2 += 1
        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]


"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (arr[mid - 1] + arr[mid]) / 2
        else:
            return arr[mid]
"""
