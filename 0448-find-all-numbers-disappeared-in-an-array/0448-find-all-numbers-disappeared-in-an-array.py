class Solution:
    def findDisappearedNumbers(self, nums):
        # Mark visited numbers
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Collect missing numbers
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans