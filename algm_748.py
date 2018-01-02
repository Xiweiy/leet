##SOLUTION 1: O(N)
class Solution(object):
    def dominantIndex(self, nums):
        highest, index = 0,-1
        second = 0
        
        for i in range(len(nums)):
            if nums[i] >= highest:
                highest, index, second = nums[i], i, highest
            elif nums[i] >= second:
                second = nums[i]

        if highest >= 2*second:
            return index
        else:
            return -1
