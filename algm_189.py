class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0, nums.pop())
