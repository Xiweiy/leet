class Solution(object):
    def canPermutePalindrome(self, s):
        from collections import Counter
        sdic = Counter(s)
        
        oddchars = 0
        for i in sdic:
            oddchars += sdic[i]%2
            if oddchars>1:
                return False
        return True
