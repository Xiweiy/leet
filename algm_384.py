from random import randint

class Solution(object):

    def __init__(self, nums):
        self.reset = lambda: nums
        self.nums = nums

    def shuffle(self):
        res = self.nums[:]
        
        for r, _ in enumerate(res):
            l = randint(0, r)
            res[r], res[l] = res[l], res[r]
        
        return res
