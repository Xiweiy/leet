##SOLUTION 1: Flatten in a single sorted list   ##162ms
class Solution(object):
    def kthSmallest(self, matrix, k):
        return sorted(n for row in matrix for n in row)[k-1]

##SOLUTION 2: Binary Search   72ms
##time complexity is O(n * log(n) * log(N)),where N is the search space that ranges from the smallest element to the biggest element. You can argue that int implies N = 2^32, so log(N) is constant. In a way, this is an O(n * log(n)) solution.
##space complexity is constant
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)/2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:  ##bisect_right return the index of breakup point
                lo = mid+1
            else:
                hi = mid
        return lo
