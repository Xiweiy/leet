class Solution(object):
    def nextGreatestLetter(self, letters, target):
        
        low = 0
        high = len(letters)-1        
        while high-low:
            mid = (low+high)/2
            if target >= letters[mid] and target < letters[mid+1]:
                return letters[mid+1]
            if target < letters[mid]:
                high = mid
            if target >= letters[mid+1]:
                low = mid+1
        return letters[0]

##BINARY SEARCH
