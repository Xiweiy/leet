##SOLUTION 1
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)


##SOLUTION 2: KMP algm
class Solution(object):
    def find_prefix(self, needle, n):

        prefix = [-1]*n
        a = -1
        
        for b in range(1,n):
            while a >= 0 and needle[a+1] != needle[b]:
                a = prefix[a]
            if needle[a+1] == needle[b]:
                a += 1
            prefix[b] = a
        return prefix
        
    def strStr(self, haystack, needle):
        m = len(needle)
        prefix = self.find_prefix(needle, m)
        print prefix
        n = len(haystack)
        
        if not m:
            return 0
        if not n:
            return -1
            
        i,j,k = 0,0,0
        
        while n-k >= m:
            while j<m and haystack[i] == needle[j]:
                i+= 1
                j+=1
                print i,j
            if j>=m:
                return k
            if not j or prefix[j-1]<0:
                i = i+1 if i==k else i
                k = i
            else:
                k = i - prefix[j-1]-1
                i = k
            if j:
                j = prefix[j-1]
        return -1
