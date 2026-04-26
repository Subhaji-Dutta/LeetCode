# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Solve:

class Solution(object):
    def subarraySum(self, nums, k):
        prefix_map = {0: 1}  # sum 0 occurs once
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix_map:
                count += prefix_map[curr_sum - k]

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        return count