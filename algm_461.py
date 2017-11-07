##SOLUTION 1:
class Solution(object):
    def calculate_sumbit(self, bitor):
        if bitor <2:
            return bitor
        else:
            return bitor%2+self.calculate_sumbit(bitor>>1)
        
    def hammingDistance(self, x, y):
        bitor = x^y
        return self.calculate_sumbit(bitor)



##SOLUTION 2:
