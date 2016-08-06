class Solution(object):
    def isValid(self, s):
        rightdic = {']':'[', ')':'(','}':'{'}
        prev = []
        for i in s:
            if i not in rightdic:
                prev.append(i)
            elif not prev or prev.pop() != rightdic[i]:
                return False
        return True if not prev else False
