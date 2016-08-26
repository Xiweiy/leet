class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            supp = target - nums[i]
            if supp in dic:
                return [dic[supp], i]
            dic[nums[i]] = i
