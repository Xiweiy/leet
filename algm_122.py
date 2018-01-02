##SOLUTION 1
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

##SOLUTION 2: ONE LINE
class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

