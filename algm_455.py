class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        i,j = 0,0
        m,n = len(g), len(s)
        total = 0
        
        while i<m and j<n:
            if g[i] <= s[j]:
                i, j, total = i+1, j+1, total+1
            else:
                j += 1
        return total

##similar to the ransom note question
