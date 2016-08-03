class Solution(object):
    def addDigits(self, num):
        r = num%9
        return r if r or not num else r+9
