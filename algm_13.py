class Solution(object):
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D' :500, 'M': 1000}
        cursum = 0
        p = 0
        for i in s[::-1]:
            if roman[i] >= p:
                cursum += roman[i]
            else:
                cursum -= roman[i]
            p = roman[i]
        return cursum
