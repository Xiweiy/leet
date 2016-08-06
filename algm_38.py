class Solution(object):
    def countAndSay(self, n):
        prev = ['1']
        for i in range(n-1):
            prev = self.calculate_freq(prev)
        return "".join(prev)
                    
    def calculate_freq(self, string):
        prevchar = ''
        count = 0
        string = ['']+ string+['']
        newstring = []
        for j in string:
            if j != prevchar:
                newstring += [str(count), prevchar] 
                prevchar = j
                count =1
            else:
                count +=1
        return newstring[2:]
