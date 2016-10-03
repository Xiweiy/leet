##SOLUTION 1: Flatten in a single sorted list
class Solution(object):
    def kthSmallest(self, matrix, k):
        return sorted(n for row in matrix for n in row)[k-1]
