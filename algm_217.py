##SOLUTION 1 use counter
class Solution(object):
    def containsDuplicate(self, nums):
        from collections import Counter
        cnt = Counter(nums)
        return bool([i for i in cnt if cnt[i]>1])

##SOLUTION 2 USE SET
class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)   
