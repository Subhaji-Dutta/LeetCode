class Solution:
    def letterCasePermutation(self, s):
        res = [""]

        for ch in s:
            if ch.isalpha():
                temp = []
                for word in res:
                    temp.append(word + ch.lower())
                    temp.append(word + ch.upper())
                res = temp
            else:
                for i in range(len(res)):
                    res[i] += ch

        return res