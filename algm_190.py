class Solution(object):
    def reverseBits(self, n):
        n = bin(n)
        rev = n[:2] + n[2:].zfill(32)[::-1]
        return int(rev,2)
