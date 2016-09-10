class Solution(object):
    def countBits(self, num):
        digits = 1
        out = [0, 1]
        end = 2**digits
        while num >= end:
            out = out + [i+1 for i in out]
            digits += 1
            end = 2**digits
        return out[:num+1]
