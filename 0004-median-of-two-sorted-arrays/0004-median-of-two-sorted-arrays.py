class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxleftA = float('-inf') if i == 0 else nums1[i - 1]
            minrightA = float('inf') if i == m else nums1[i]

            maxleftB = float('-inf') if j == 0 else nums2[j - 1]
            minrightB = float('inf') if j == n else nums2[j]

            if maxleftA <= minrightB and maxleftB <= minrightA:

                if (m + n) % 2 == 0:
                    return (max(maxleftA, maxleftB) +
                            min(minrightA, minrightB)) / 2.0
                else:
                    return max(maxleftA, maxleftB)

            elif maxleftA > minrightB:
                high = i - 1
            else:
                low = i + 1