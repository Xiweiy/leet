##SOLUTION 1: 152ms
class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        return sum([nums[i] for i in range(len(nums)) if not i%2])


##SOLUTION 2: 125ms
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
