class Solution(object):
    
    def isSelfDividing(self, number):
        digit = number
        while digit:
            if digit%10 and not number%(digit%10):
                digit /= 10
            else:
                return False
        return True
        
    def selfDividingNumbers(self, left, right):
        return [i for i in range(left, right+1) if self.isSelfDividing(i)]
