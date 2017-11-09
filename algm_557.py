##SOLUTION 1:
class Solution(object):
    def reverseWords(self, s):
        return " ".join([i[::-1] for i in s.split(" ")])

##SOLUTION 2:
def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]
