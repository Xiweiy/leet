class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        headeven = head.next
        odd, even =  head, head.next
        while odd.next and odd.next.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = headeven
        return head
