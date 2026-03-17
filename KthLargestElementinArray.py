# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 
#  Solve

# QuickSelect
import random

class Solution:
    def findKthLargest(self, nums, k):
        k = len(nums) - k  # convert to kth smallest index

        def quickselect(left, right):
            pivot = nums[random.randint(left, right)]
            l, r = left, right

            while l <= r:
                while nums[l] < pivot:
                    l += 1
                while nums[r] > pivot:
                    r -= 1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r -= 1

            if k <= r:
                return quickselect(left, r)
            if k >= l:
                return quickselect(l, right)
            return nums[k]

        return quickselect(0, len(nums) - 1)
    
# Heap
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    
# Mannual Heap
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

        return heap[0]