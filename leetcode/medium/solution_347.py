"""
前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
提示：
1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        buckets = [[] for _ in range(max_cnt + 1)]
        for x, c in cnt.items():
            buckets[c].append(x)
        ans = []
        for i in range(max_cnt, -1, -1):
            ans += buckets[i]
            if len(ans) == k:
                # 保证一定存在
                return ans
        return ans


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []
        for n, c in cnt.items():
            if len(heap) == k:
                if heap[0][0] < c:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (c, n))
            else:
                heapq.heappush(heap, (c, n))
        return [heapq.heappop(heap)[1] for _ in range(k)]
"""
