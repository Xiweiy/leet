class Solution(object):
    def reverse(self, x):
        maxmum = 2**31
        sign = 1 if x>0 else -1
        resid = x*sign
        new = 0
        while resid:
            if new > maxmum/10:   ##check if overflow
                return 0
            new = new*10 + resid%10
            resid /= 10
        return new*sign
