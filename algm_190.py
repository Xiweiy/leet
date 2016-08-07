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
