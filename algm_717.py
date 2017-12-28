class Solution(object):
    def isOneBitCharacter(self, bits):
        index = 0
        n = len(bits)
        while index < n:
            if index == n-1:
                return True
            if bits[index]==0:
                index += 1
            else:
                index += 2
        return False
