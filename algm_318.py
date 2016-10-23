class Solution(object):
    def maxProduct(self, words):
        wordlength = [len(i) for i in words]
        wordset = [set(i) for i in words]
        nword = len(words)
        max = 0
        for i in range(nword):
            for j in range(i, nword): 
                result = 0 if wordset[i] & wordset[j] else wordlength[i]*wordlength[j]
                max = result if result > max else max
        return max
