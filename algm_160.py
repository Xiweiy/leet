class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA = headA
        curB = headB
        while curA != curB:
            curA = headB if curA is None else curA.next
            curB = headA if curB is None else curB.next
        return curA
