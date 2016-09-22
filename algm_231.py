class Solution(object):
    def isPowerOfTwo(self, n):
        if n <=0:
            return False
        if not n&(n-1):
            return True
        else:
            return False
