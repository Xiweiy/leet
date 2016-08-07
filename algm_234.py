class Solution(object):
    def isPalindrome(self, head):
        reverse = None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next
        if fast:
            slow = slow.next
        while reverse and reverse.val == slow.val:
            reverse = reverse.next
            slow = slow.next
        return not reverse
