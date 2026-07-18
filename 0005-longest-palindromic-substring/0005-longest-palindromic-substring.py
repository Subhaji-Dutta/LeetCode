class Solution:
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            left1, right1 = expand(i, i)       # odd length
            left2, right2 = expand(i, i + 1)   # even length

            if right1 - left1 + 1 > max_len:
                start = left1
                max_len = right1 - left1 + 1

            if right2 - left2 + 1 > max_len:
                start = left2
                max_len = right2 - left2 + 1

        return s[start:start + max_len]