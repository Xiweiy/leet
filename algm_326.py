class Solution(object):
    def isPowerOfThree(self, n):
        if n <=0:
            return False
        temp = math.log10(n) / math.log10(3)
        if temp.is_integer():
            return True
        return False
