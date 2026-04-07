# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

# Solve

import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result