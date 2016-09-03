##SOLUTION 1
class Solution(object):
    def titleToNumber(self, s):
        digit = 0
        total = 0
        for i in s[::-1]:
            total += (ord(i)-64)*26**digit
            digit += 1
        return total


##SOLUTION 2
class Solution(object):
    def titleToNumber(self, s):
        index = dict(zip(list(string.uppercase), range(1,27)))
        base = 1
        result = 0

        for char in s[::-1]:
            result += index[char] * base
            base *= 26

        return result

##SOLUTION 3
class Solution(object):
    def titleToNumber(self, s):
        list1 = [ord(x)-64 for x in s]
        list2 = [pow(26,x) for x in range(len(s))[::-1]]
        return sum([x*y for x,y in zip(list1,list2)])
