# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

# Solve

class Solution(object):
    def firstUniqChar(self, s):
      
        count = {}

        # Step 1: Count frequency
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Step 2: Find first unique character
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1