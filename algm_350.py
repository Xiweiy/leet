class Solution(object):
    def intersect(self, nums1, nums2):
        result = []
        from collections import Counter
        dic1, dic2 = Counter(nums1), Counter(nums2)
        for i in set(dic1.keys()+dic2.keys()):
            if i in dic1 and i in dic2:
                result += [i]*min(dic1[i],dic2[i])
        return result
