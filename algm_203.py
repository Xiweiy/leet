class Solution(object):
    def removeElements(self, head, val):
        pseudohead = ListNode(None)
        pseudohead.next = head
        prev = pseudohead
        while prev and prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return pseudohead.next
