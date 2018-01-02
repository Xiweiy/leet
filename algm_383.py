##solution 1: use collections.Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        from collections import Counter
        ransom = Counter(ransomNote)
        magazine = Counter(magazine)
        return all([ransom[i]<=magazine[i] for i in ransom])

##solution 2: similar idea as merging two sorted list
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom = sorted(ransomNote)
        magazine = sorted(magazine)
        
        i,j = 0,0
        m,n = len(ransom), len(magazine)
        
        while i<m and j<n:
            if ransom[i]<magazine[j]:
                return False
            elif ransom[i]>magazine[j]:
                j += 1
            else:
                i += 1
                j += 1
        if i<m:
            return False
        return True
