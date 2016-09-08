##binary search
class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        low, high, mid = 1, n, (n+1)/2
        while low != mid:
            if isBadVersion(mid):
                high = mid
            else:
                low = mid
            mid = (low+high)/2
        return high
