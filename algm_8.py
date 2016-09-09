class Solution(object):
    def myAtoi(self, str):
        number = 0
        sign = 1
        prev = 0
        for i in str.strip(' '):
            ascii = ord(i)
            if ascii < 48 or ascii >57:
                if number or prev or ascii not in [43, 45]:
                    break
                prev = 1
                if ascii ==45:
                    sign = -1
            else:
                number = number*10 + ascii-48
                prev = 0
        if sign*number >2**31-1:
            return 2**31-1 
        elif sign*number<-(2**31):
            return -2**31
        else:
            return number*sign
