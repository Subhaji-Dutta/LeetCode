# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 
#  Solve

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        start = 0
        min_len = float('inf')

        for right in range(len(s)):
            char = s[right]

            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1

                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]