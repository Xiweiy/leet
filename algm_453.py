class Solution(object):
    def minMoves(self, nums):
        return sum(nums) - len(nums) * min(nums)

##math problem
##solve two equations:
## sum(nums) + moves*(len(nums)-1) = fianlNumber * len(nums)
## min(nums) + moves = finalNum   (idea is: at every round, all items except the currently largest got incremented, so after the incrementation, the smallest will still be smallest, otherwise all items will be equal)
