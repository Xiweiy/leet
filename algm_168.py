class Solution(object):
    def convertToTitle(self, n):
        import string
        letters = string.uppercase
        resid = n
        out = ''
        while resid:
            out = letters[resid%26-1] + out
            resid = (resid-1)/26 
        return out
