#SOLUTION 1: Stored as list of tuple    176MS
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



#SOLUTION 2: STORE AS TWO LISTS - SAVE MEMORY  146MS
class MinStack(object):

    def __init__(self):
        self.elements = []
        self.mini = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.elements.append(x)
        if not self.mini:
            self.mini.append(x)
        elif x <= self.mini[-1]:
            self.mini.append(x)

        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        last = self.elements[-1]
        self.elements.pop()
        if self.mini and self.mini[-1] == last:
            self.mini.pop()

        """
        :rtype: void
        """
        

    def top(self):
        return self.elements[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        if self.mini:
            return self.mini[-1]
        else:
            return None
        """
        :rtype: int
        """

