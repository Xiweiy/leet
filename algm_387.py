class Solution(object):
    def firstUniqChar(self, s):
        from collections import Counter
        stringDic = Counter(s)
        for i in range(len(s)):
            if stringDic[s[i]]==1:
                return i
        return -1
