##SOLUTION 1  USE COUNTER PACKAGE  368MS
class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s) == Counter(t)


##SOLUTION 2   USE SORTED LIST   296MS
class Solution(object):
    def isAnagram(self, s, t):
        l1 = list(sorted(s))
        l2 = list(sorted(t))
        if l1 == l2:
            return True
        else:
            return False


##SOLUTION 3   USE DICTIONARY   340MS
class Solution(object):
    def isAnagram(self, s, t):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
            if i not in dic:
                return False
            else:
                dic[i] -= 1
        if all(i==0 for i in dic.values()):
            return True
        else:
            return False
