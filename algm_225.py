class Stack(object):
    def __init__(self):
        self.a = []
        self.b = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        if not self.b:
            self.a.append(x)
        if self.b:
            self.b.append(x)
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        if self.a:
            toadd = self.a[0]
            self.a.pop(0)
            while self.a:
                self.b.append(toadd)
                toadd = self.a[0]
                self.a.pop(0)
        elif self.b:
            toadd = self.b[0]
            self.b.pop(0)
            while self.b:
                self.a.append(toadd)
                toadd = self.b[0]
                self.b.pop(0)
        """
        :rtype: nothing
        """
        

    def top(self):
        if self.a:
            while self.a:
                toadd = self.a[0]
                self.b.append(toadd)
                self.a.pop(0)
            return toadd
        elif self.b:
            while self.b:
                toadd = self.b[0]
                self.a.append(toadd)
                self.b.pop(0)
            return toadd
        """
        :rtype: int
        """
        

    def empty(self):
        if self.a or self.b:
            return False
        return True
        """
        :rtype: bool
        """
