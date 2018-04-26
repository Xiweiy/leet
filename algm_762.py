class Solution(object):
    def countSetBits(self, num):

        num = (num >> 1 & 0x5555555555555555) + (num & 0x5555555555555555) ##64bit 0101...0101
        num = (num >> 2 & 0x3333333333333333) + (num & 0x3333333333333333) ##64bit 0011...0011
        num = (num >> 4 & 0x0f0f0f0f0f0f0f0f) + (num & 0x0f0f0f0f0f0f0f0f) ##64bit 00001111....
        num = (num >> 8 & 0x00ff00ff00ff00ff) + (num & 0x00ff00ff00ff00ff) ##need to consider operator priority
        num = (num >> 16 & 0x0000ffff0000ffff) + (num & 0x0000ffff0000ffff)
        num = (num >> 32 & 0x00000000ffffffff) + (num & 0x00000000ffffffff)
        return num
    
    def isPrime(self, num):
        if num < 2:
            return False
        
        i = 2
        for i in range(2,num/2+1):
            if num%i==0:
                return False
        return True
        
    def countPrimeSetBits(self, L, R):
        counter = 0
        for i in range(L,R+1):
            setBits = self.countSetBits(i)
            if self.isPrime(setBits):
                counter += 1
        return counter
