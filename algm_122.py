class Solution(object):
    def maxProfit(self, prices):
        total = 0
        import itertools
        a,b = itertools.tee(prices)
        next(b, None)
        for i,j in itertools.izip(a,b):
            if i < j:
                total += (j-i)
        return total
