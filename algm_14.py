class Solution(object):
    def common_twostring(self, str1, str2):
        commonstr = ''
        for i,j in zip(str1, str2):
            if i==j:
                commonstr += i
            else:
                return commonstr
        return commonstr
    
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        n = len(strs)
        if n ==1:
            return strs[0]

        curstring = strs[0]
        count = 1
        while curstring and count < n:
            curstring = self.common_twostring(curstring, strs[count])
            count +=1
        return curstring
            
