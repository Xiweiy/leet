class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        freq = Counter(nums)
        newlist = sorted(freq.iteritems(), key=lambda x: x[1], reverse=True)
        return [newlist[i][0] for i in range(k)]
