class Solution(object):
    def myAtoi(self, str):
        number = 0
        sign = 1
        prev = 0
        for i in str.strip(' '):
            ascii = ord(i)
            if ascii < 48 or ascii >57:   ##if not number string
                if number or prev or ascii not in [43, 45]: 
		##3 cases
		###(1) some non-numeric char inside the string, '1230+' ==> 1230
		###(2) some previous non-numeric char before this char, like '+-2' ==> 0
		###(3) some char at the beginning of string, '>1' ==> 0  
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
