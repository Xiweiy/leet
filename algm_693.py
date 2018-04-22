class Solution(object):
    def hasAlternatingBits(self, n):
        xor = n ^ (n >> 1)
        return not xor & (xor + 1)
