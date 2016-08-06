class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip(' ').split(' ')
        return len(s[-1]) if s else 0
