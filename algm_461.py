##SOLUTION 1: BITWISE OPERATION    ##beat 69.34%
class Solution(object):
    def calculate_sumbit(self, bitor):
        if bitor <2:
            return bitor
        else:
            return bitor%2+self.calculate_sumbit(bitor>>1)
        
    def hammingDistance(self, x, y):
        bitor = x^y
        return self.calculate_sumbit(bitor)



##SOLUTION 2: BINARY STRING    ##beat 27.55%
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
