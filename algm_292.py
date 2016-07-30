##solution 1   55ms
class Solution(object):
    def canWinNim(self, n):
        return [False if n%4==0 else True][0]

##Solution 2    56ms
class Solution(object):
    def canWinNim(self, n):
        a = n%4
        if a == 0:
            return False
        else:
            return True

##Solution 3   48s
class Solution(object):
    def canWinNim(self, n):
        return bool(n%4)
