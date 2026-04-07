# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Solve

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        count = {}

        # Count characters in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Check ransomNote
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True