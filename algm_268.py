class Solution(object):
    def missingNumber(self, nums):
        maximum = 0
        sum = 0
        length = len(nums)
        for i in nums:
            sum += i
            maximum = i if i>maximum else maximum
        if maximum < length:  ##missing the maximum number
            return maximum +1
        total = (1+maximum)*(len(nums))/2
        return total - sum
