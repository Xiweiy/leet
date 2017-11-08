##SOLUTION 1:RECURSIVE
class Solution(object):
    def findComplement(self, num):
        if num <2:
            return 1-num
        else:
            return self.findComplement(num/2)*2+self.findComplement(num%2)


##SOLUTION 2: ITERATIVE+XOR
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
