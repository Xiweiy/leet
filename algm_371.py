class Solution(object):
    def getSum(self, a, b):
        result = 0
        addition  = 0
        for i in range(32):
            cura = a & (1 << i)
            curb = b & (1 << i)
            
            result = result | (cura^curb)^addition
            addition = ((cura|curb) & addition or (cura|addition) & curb)<<1
            
        if result > (1<< 31 -1):
            return result - (1<<32)
        else:
            return result
