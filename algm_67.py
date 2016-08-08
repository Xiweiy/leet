class Solution(object):
    def addBinary(self, a, b):
        
        result = []
        addition  = 0

        n = max(len(a), len(b))
        a, b = list(a.zfill(n)), list(b.zfill(n))
        while a and b:
            cura = int(a.pop())
            curb = int(b.pop())
            
            result =  [str((cura^curb)^addition)] + result
            addition = ((cura|curb) & addition or (cura|addition) & curb)
        
        addition = ['1'] if addition else ['']
        return ''.join(addition+result)
