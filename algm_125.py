##SOLUTION 1  regular expression
class Solution(object):
    def isPalindrome(self, s):
        import re
        s = ''.join(re.findall("[a-zA-Z0-9]+", s)).lower()
        n = len(s)
        if n<2:
            return True
        half = n/2
        for i in range(n/2):
            if s[i] != s[n-1-i]:
                return False
        return True


##SOLUTION 2 FILTER FUNCTION
class Solution(object):
    def isPalindrome(self, s):
        s = filter(lambda x:x.isalnum(), s).lower()
        n = len(s)
        if n<2:
            return True
        half = n/2
        for i in range(n/2):
            if s[i] != s[n-1-i]:
                return False
        return True
