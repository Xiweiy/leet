class Solution(object):
    def matrixReshape(self, nums, r, c):
        import itertools
        fulllist = list(itertools.chain.from_iterable(nums))
        fulllength = len(fulllist)
        if r*c==fulllength:
            return [fulllist[i*c:i*c+c] for i in range(r)]
        else:
            return nums
