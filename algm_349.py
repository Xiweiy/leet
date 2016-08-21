class Solution(object):
    def intersection(self, nums1, nums2):
        numdic = {i:0 for i in nums1}
        return list(set([i for i in nums2 if i in numdic]))
