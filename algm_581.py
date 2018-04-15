###BITTIGER 2nd BEST SOLUTION
###time complexity: O(nlogn)
class Solution(object):
    def findUnsortedSubarray(self, nums):
        sortedNums = sorted(nums)
        start,end = 0, 0
        nNums = len(nums)
        
        for i in range(nNums):
            if nums[i] != sortedNums[i]:
                start = i 
                break
        for i in range(nNums-1 ,-1, -1):
            if nums[i] != sortedNums[i]:
                end = i 
                break
        return 0 if start==end else end-start+1

###O(N) Solution
###use maxLeft to keep track of the movingMax on the left
###use minRight to keep track of the movingMin on the right
class Solution(object):
    def findUnsortedSubarray(self, nums):  ##Consider Dup?
        nNums = len(nums)
        
        maxLeft = []
        movingMax = nums[0] if nums else None
        for i in range(nNums):
            movingMax = max(nums[i], movingMax)
            maxLeft.append(movingMax)
        
        minRight = []
        movingMin = nums[-1] if nums else None
        for i in range(nNums-1,-1,-1):
            movingMin = min(nums[i], movingMin)
            minRight.append(movingMin)   ##list concatenation is much more expensive than append
        
        minRight = minRight[::-1]
        start, end = 0, 0 
        for i in range(nNums):
            if nums[i] != minRight[i]:
                start = i
                break
        
        for i in range(nNums-1,-1,-1):
            if nums[i] != maxLeft[i]:
                end = i
                break
        return end-start+1 if end != start else 0

###SOLUTION 3: o(N) time and O(1) space
class Solution(object):
    def findUnsortedSubarray(self, nums):
        nums = [float('-inf')] + nums + [float('inf')]
        '''find left boundary'''
        left = 0
        while left<len(nums)-1 and nums[left]<=nums[left+1]:
            left += 1
        # return 0 if already sorted ascending
        if left == len(nums)-1:
            return 0
        min_num = min(nums[left+1:])
        while nums[left] > min_num:
            left -= 1
        '''find right boundary'''
        right = len(nums)-1
        while right>0 and nums[right-1]<=nums[right]:
            right -= 1
        # return 0 if sorted descending
        if right == 0:
            return 0
        max_num = max(nums[:right])
        while nums[right] < max_num:
            right += 1
        return right - left - 1
