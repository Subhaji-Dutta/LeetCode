class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find next greater element
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: swap
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1