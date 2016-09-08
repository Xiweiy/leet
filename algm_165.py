class Solution(object):
    def compareVersion(self, version1, version2):
        v1, v2 = version1.split('.'), version2.split('.')
        print len(v1), len(v2)
        while v1 and v2:
            i,j = int(v1[0]), int(v2[0])
            if i>j:
                return 1
            elif i<j:
                return -1
            else:
                v1.pop(0)
                v2.pop(0)
        while v1:
            if int(v1[0]):
                return 1
            else:
                v1.pop(0)
        while v2:
            if int(v2[0]):
                return -1
            else:
                v2.pop(0)
        return 0
