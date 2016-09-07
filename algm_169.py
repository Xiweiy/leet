##SOLUTION 1 SORT   100MS
class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)/2]

##SOLUTION 2  COLLECTION.COUNTER 120MS
class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        n = len(nums)
        cnt = Counter(nums).items()                          # Get items and counters pair
        gen = (k for (k,v) in cnt if v > n/ 2)      # Filter out the "common" item
        return next(gen)


##SOLUTION 3 SORT AND REVERSE 84MS
class Solution(object):
    def majorityElement(self, nums):
        return sorted([[nums.count(x),x] for x in set(nums)],reverse=True)[0][1]
