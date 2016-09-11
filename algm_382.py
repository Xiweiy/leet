# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        self.head = head
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        

    def getRandom(self):
        import random
        number = 1
        head = self.head
        while head:
            if random.random()*number <1:
                rvalue = head.val
            number +=1
            head= head.next
        return rvalue
        """
        Returns a random node's value.
        :rtype: int
        """
        
