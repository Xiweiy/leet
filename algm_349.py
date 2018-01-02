##SOLUTION 1: SET
class Solution(object):
    def intersection(self, nums1, nums2):
        numdic = {i:0 for i in nums1}
        return list(set([i for i in nums2 if i in numdic]))

##SOLUTION 2: WHEN SET NOT ALLOWED
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i,j = 0,0
        m,n = len(nums1), len(nums2)
        resultlist = []
        while i<m and j<n:
            print i,j
            if nums1[i]<nums2[j]:
                i += 1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                if not resultlist or resultlist[-1]!= nums1[i]:
                    resultlist.append(nums1[i])
                i += 1
                j += 1
        return resultlist

##NOTE: similar to merge sort
