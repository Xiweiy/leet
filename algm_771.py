class Solution(object):
    def numJewelsInStones(self, J, S):
        uniqueJ = set(J)
        return len([i for i in S if i in uniqueJ])
