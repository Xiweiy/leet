class Solution(object):
    def productExceptSelf(self, nums):
        left, right = [1], [1]
        n = len(nums)
        output = [1]*n
        left, right = 1,1
        for i in range(1, n):
            left *= nums[i-1]
            right *= nums[-i]
            output[i] *= left
            output[-i-1] *= right
        return output

##NOT USE TWO LIST AND MULTIPLY TOGETHER BECAUSE 
###(1) Concatenate list not run in O(1) time
###(2) Question ask for constant space
