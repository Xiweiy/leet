##solution 1: O(n) time with n=window size
class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.window = []
        
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        if len(self.window) >=self.size:
            self.window.pop(0)
        self.window.append(val)
        return sum(self.window)*1.0/len(self.window)

##solution 2: O(1) time
class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.window = []
        self.sum = 0
        
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        if len(self.window) >=self.size:
            self.sum -= self.window.pop(0)
        self.window.append(val)
        self.sum += val
        return self.sum*1.0/len(self.window)
