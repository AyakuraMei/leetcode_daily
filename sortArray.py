'''
    给你一个整数数组 nums，请你将该数组升序排列。
'''
# Quick sort
from random import *

class Solution:
    def randomized_parition(self, nums, l, r):
        pivot = randint(l, r)   # 随机选取一个数作为基准
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):   # 排序算法
            if nums[j] < nums[r]:   # 如果 nums[j] 比基准小
                i += 1
                nums[j],nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_parition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

# Merge sort
class Solution2:
    def mergeSort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        ans = []
        i, j = l, mid + 1
        # 分开两边排序
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)
        while i <= mid or j <= r:
            if j > mid or (j <= r and nums[j] < nums[i]):   # 如果 j 超过界限，那么将另一个数组的全部移到ans中；如果同时都没有超过界限，那么进行比较，将比较小的放进ans中
                ans.append(nums[j])
                j += 1
            else:
                ans.append(nums[i])
                i += 1
        nums[l:r + 1] = ans

    def sortArray(self, nums):
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

