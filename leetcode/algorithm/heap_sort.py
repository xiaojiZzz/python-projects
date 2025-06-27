from typing import List


# 堆排序，建堆：o(n)，排序：o(nlogn)
class HeapSort:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def heap_sort(self) -> None:
        self.heapify()
        n = len(self.nums)
        for i in range(n - 1, -1, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            self.adjust_heap(0, i)

    def heapify(self) -> None:
        n = len(self.nums)
        for i in range(n // 2 - 1, -1, -1):
            self.adjust_heap(i, n)

    def adjust_heap(self, i: int, n: int) -> None:
        while 2 * i + 1 < n:
            j = 2 * i + 1
            if j + 1 < n and self.nums[j + 1] > self.nums[j]:
                j += 1
            if self.nums[j] <= self.nums[i]:
                break
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            i = j
