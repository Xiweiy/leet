class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        largestOnes = 0
        currentOnes = 0
        for i in nums:
            if i:
                currentOnes += 1
            else:
                largestOnes = max(currentOnes, largestOnes)
                currentOnes = 0
        return max(currentOnes, largestOnes)
