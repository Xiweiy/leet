#SOLUTION 1: Stored as list of tuple
class MinStack(object):

    def __init__(self):
        self.elements = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        if not self.elements:
            self.elements.append( (x,x))
        else:
            lastmin = self.elements[-1][1]
            curmin = lastmin if x>lastmin else x
            self.elements.append((x,curmin))
        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        self.elements.pop()
        """
        :rtype: void
        """
        

    def top(self):
        return self.elements[-1][0]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.elements[-1][1]
        """
        :rtype: int
        """
        

