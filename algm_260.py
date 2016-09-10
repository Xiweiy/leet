class Solution(object):
    def singleNumber(self, nums):
        xor = reduce(lambda a, b: a ^ b, nums)   ##XOR all numbers in the list
        ##if only 1 non-pair int in the list, then the XOR result is that int
        ##if 2 non-pair integers, then need to pick the distinct integer as flag, and use the flag to separate the list into 2 group
        distinct = xor & (xor*-1)   #xor + (-xor) =0, so xor & -xor return the rightmost non-zero digit
        one, two = 0,0  ##initialize 2 sums
        for i in nums:
            if i & distinct:
                one ^= i
            else:
                two ^= i
        return one, two
