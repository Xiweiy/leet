class Solution(object):
    def calPoints(self, ops):
        history = []
        total = 0
        for i in ops:
            try: 
                history.append(int(i))
            except:                
                if i=="C":
                    history.pop()     
                elif i=="+":
                    history.append(sum(history[-2:]))
                else:
                    history.append(history[-1]*2)
        return sum(history)
