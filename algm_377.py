##Dynamic Programming
class Solution(object):

    def combinationSum4(self, nums, target):
        maps = [0]*(target+1)
        maps[0] = 1
        i = 1
        while i <= target:
            for num in nums:
                if num <= i:
                    maps[i] += maps[i - num]
            i += 1
                    
        return maps[target]
