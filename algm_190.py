##SOLUTION 1: STRING
class Solution(object):
    def reverseBits(self, n):
        n = bin(n)
        rev = n[:2] + n[2:].zfill(32)[::-1]
        return int(rev,2)


##SOLUTION 2: REVERSE BIT BY BIT AND STORE IN A NEW NUM
class Solution(object):
    def reverseBits(self, n):
        newnum = 0
        for i in range(16):
            first, last = n & 1<< (31-i), n & 1<<i
            newnum = newnum | first >> (31-2*i)| last <<(31-2*i)
        return newnum

##SOLUTION 3: REVERSE EVERY 1,2,4,8,16 NEIGHBORING BITS 
class Solution(object):
    def reverseBits(self, n):
        n = ((n & 0x55555555)<<1) | ((n&0xaaaaaaaa)>>1)
        n = ((n & 0x33333333)<<2) | ((n&0xcccccccc)>>2)
        n = ((n & 0x0f0f0f0f)<<4) | ((n&0xf0f0f0f0)>>4)
        n = ((n & 0x00ff00ff)<<8) | ((n&0xff00ff00)>>8)
        n = ((n & 0xffff)<<16) | ((n&0xffff0000)>>16)
        return n
