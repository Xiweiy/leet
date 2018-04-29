class Solution(object):
    def countDigits(self, head):
        count = 0
        currnode = head
        while currnode:
            count +=1 
            currnode = currnode.next
        return count
    
    def addTwoNumbers(self, l1, l2):
        lenl1 = self.countDigits(l1)
        lenl2 = self.countDigits(l2)
        if lenl2 > lenl1:
            l1, l2 = l2, l1
        
        prev1, cur1 = None, l1
        cur2 = l2
        addon = 0
        while cur1 or cur2:
            val2 = cur2.val if cur2 else 0
            currsum = cur1.val + val2 + addon
            cur1.val = currsum%10
            addon = currsum/10
            prev1, cur1 = cur1, cur1.next
            cur2 = cur2.next if cur2 else cur2
        if addon:
            prev1.next = ListNode(1)
        return l1
