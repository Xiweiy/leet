#sliding window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        maxLen = 0
        window = set()
        
        n = len(s)
        while end < len(s):
            newChar = s[end]
            if newChar in window:
                window.remove(s[start])
                start += 1
            else:
                window.add(newChar)
                end += 1
                if end-start > maxLen:
                    maxLen = end-start
        return maxLen
