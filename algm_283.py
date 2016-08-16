class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j = 0
        n = len(nums)
        while j <n:
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
