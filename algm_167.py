class Solution(object):
    def twoSum(self, numbers, target):
        index = 0
        n = len(numbers)
        suppindex = {}
        while index < n:
            curnum = numbers[index]
            if curnum in suppindex:
                return [suppindex[curnum], index+1]
            suppindex[target - curnum] = index+1
            index +=1
        return None
