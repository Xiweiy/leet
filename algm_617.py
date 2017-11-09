##SOLUTION 1: DFS - RECURSIVE
class Solution(object):

    def mergeTrees(self, t1, t2):
        if t1==None and t2==None:
            return t1
        elif t1==None or t2==None:
            return (t1 or t2)
        else:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
