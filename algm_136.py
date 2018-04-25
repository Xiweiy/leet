class Solution(object):
    def singleNumber(self, nums):
        total = 0
        for i in nums:
            total = total ^ i
        return total
