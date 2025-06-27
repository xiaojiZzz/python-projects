"""
数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
示例 1:
输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
提示：
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def heapify() -> None:
            for i in range(n // 2 - 1, -1, -1):
                adjust_heap(i, n)

        def adjust_heap(x: int, y: int) -> None:
            while 2 * x + 1 < y:
                j = 2 * x + 1
                if j + 1 < y and nums[j + 1] > nums[j]:
                    j += 1
                if nums[j] <= nums[x]:
                    break
                nums[x], nums[j] = nums[j], nums[x]
                x = j

        heapify()
        for k in range(n - 1, n - k, -1):
            nums[0], nums[k] = nums[k], nums[0]
            adjust_heap(0, k)
        return nums[0]


"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
"""

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        buckets = [0] * 20001
        for num in nums:
            buckets[num + 10000] += 1
        for i in range(20000, -1, -1):
            k -= buckets[i]
            if k <= 0:
                return i - 10000
        return 0
"""

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(nums, k):
            big, small, equal = [], [], []
            pivot = random.choice(nums)
            for c in nums:
                if c > pivot:
                    big.append(c)
                elif c < pivot:
                    small.append(c)
                else:
                    equal.append(c)
            if len(big) >= k:
                return quick(big, k)
            elif len(nums) - len(small)  < k:
                return quick(small, k + len(small)-len(nums))
            else:
                return pivot
        return quick(nums, k)
"""
