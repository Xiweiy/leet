##1 RECURSIVE   68ms
class Solution(object):
    def isSameTree(self, p, q):
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        if p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

##2 ITERATIVE   88ms
class Solution(object):
    def isSameTree(self, p, q):
        plist = [p]
        qlist = [q]
        while plist and qlist:
            curnodep, curnodeq = plist[0],qlist[0]
            if curnodep is None and curnodeq is None:
                pass
            elif curnodep is None or curnodeq is None:
                return False
            elif curnodep.val != curnodeq.val:
                return False
            else:
                plist += [curnodep.left, curnodep.right]
                qlist += [curnodeq.left, curnodeq.right]
            del plist[0]
            del qlist[0]
        return True
