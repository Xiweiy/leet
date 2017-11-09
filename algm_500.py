class Solution(object):
    def findWords(self, words):
        return filter(re.compile("(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$").match, words)
