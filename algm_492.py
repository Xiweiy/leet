class Solution(object):
    def constructRectangle(self, area):
        import math
        sqrt = int(math.sqrt(area))
        for i in range(sqrt, 0,-1):
            if not area%i:
                return area/i, i
