from typing import List


class BinaryTemplate:
    # 闭区间 [0, n - 1]
    def binaryTemplate1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 左闭右开 [0, n)
    def binaryTemplate2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    # 开区间 (-1, n)
    def binaryTemplate3(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right
