class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        n = len(s)
        grid = numRows + numRows - 2
        new = ['']*numRows
        for i in range(n):
            rem = i%grid
            index = rem if rem < numRows else (grid-rem)
            new[index] += s[i]
        return ''.join(new)
