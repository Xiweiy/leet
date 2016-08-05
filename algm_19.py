class Solution(object):
    def removeNthFromEnd(self, head, n):
        p1, p2 = head, head
        while n:
            p1 = p1.next
            n -=1
        if p1 is None:
            return head.next
        while p1.next is not None:
            p1, p2 = p1.next, p2.next
        p2.next = p2.next.next
        return head
