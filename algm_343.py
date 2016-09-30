class Solution(object):
    def integerBreak(self, n):
        initiate = [1,1,2,4]
        if n<5:
            return initiate[n-1]
        prod = 1
        while n > 4:
            n -= 3
            prod *= 3
        return prod*n
