class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m*n
        min_x = min([i[0] for i in ops])
        min_y = min([i[1] for i in ops])
        return min_x*min_y
