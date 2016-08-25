class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [self.nums[0]] if self.nums else []
        for i in range(1, len(nums)):
            self.sums.append(self.sums[-1]+self.nums[i])
        

    def sumRange(self, i, j):
        if not self.nums:
            return 0
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - self.sums[i] + self.nums[i]
