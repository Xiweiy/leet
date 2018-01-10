class Logger(object):

    def __init__(self):
        self.lastprint = {}
        """
        Initialize your data structure here.
        """
        

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.lastprint or timestamp-self.lastprint[message] >= 10:
            self.lastprint[message] = timestamp
            return True
        else:
            return False
