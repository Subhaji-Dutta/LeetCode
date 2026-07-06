class Solution:
    def longestMountain(self, arr):
        up = down = ans = 0

        for i in range(1, len(arr)):

            if (down and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                up = down = 0

            if arr[i] > arr[i-1]:
                up += 1

            elif arr[i] < arr[i-1]:
                if up:
                    down += 1

            if up and down:
                ans = max(ans, up + down + 1)

        return ans
        