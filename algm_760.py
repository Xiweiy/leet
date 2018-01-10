class Solution(object):
    def anagramMappings(self, A, B):
        bdic = {B[i]:i for i in range(len(B))}
        return [bdic[i] for i in A]
