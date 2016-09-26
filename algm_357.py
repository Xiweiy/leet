class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if not n:
            return 1

        total = 10
        culmuprod = 9
        
        curint = n-1
        if n > 10:
            curint = 10
        
        i = 0
        while i < curint:
            culmuprod = culmuprod*(9 - i)
            total += culmuprod
            i += 1
        return total
