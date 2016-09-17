##Recursive
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return newhead

##iterative
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        prenode = head
        curnode = head.next
        head.next = None
        while curnode is not None:
            nextnode = curnode.next
            curnode.next = prenode
            prenode = curnode
            curnode = nextnode
        return prenode
