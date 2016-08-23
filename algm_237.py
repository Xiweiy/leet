class Solution(object):
    def deleteNode(self, node):
        if node.next is not None:
            node.val = node.next.val
            node.next = node.next.next



class Solution(object):
    def deleteNode(self, node):
        if node.next != None:
            temp = node.next
            node.val = temp.val
            node.next = temp.next
