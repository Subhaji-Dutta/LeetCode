# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
 

#  Solve

from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        n = len(s)

        # Step 1: find most frequent char
        max_char = max(count, key=count.get)
        max_freq = count[max_char]

        # Step 2: check feasibility
        if max_freq > (n + 1) // 2:
            return ""

        # Step 3: create result array
        res = [""] * n
        index = 0

        # Step 4: place most frequent char at even indices
        while count[max_char] > 0:
            res[index] = max_char
            index += 2
            count[max_char] -= 1

        # Step 5: fill remaining characters
        for ch in count:
            while count[ch] > 0:
                if index >= n:
                    index = 1  # switch to odd indices
                res[index] = ch
                index += 2
                count[ch] -= 1

        return "".join(res)