class Solution(object):
    def numberOfLines(self, widths, S):
        if not S:
            return [0,0]
        total = 1
        lastline = 0
        for i in S:
            index = ord(i)-ord('a')
            each_width = widths[index]
            if lastline + each_width <= 100:
                lastline += each_width
            else:
                total += 1
                lastline = each_width
        return [total, lastline]
