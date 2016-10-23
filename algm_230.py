##Use inorder morris traversal
class Solution(object):

    def find_mostright(self, root):
        if not root.left.right:
            return root.left
        else:
            curparent = root.left
            while curparent.right and curparent.right != root:
                curparent = curparent.right
            return curparent
        
        
        
    def kthSmallest(self, root, k):
        if not root:
            return None
        curnode = root
        inorder = []
        while curnode:
            if not curnode.left: 
                if k == 1:
                    return curnode.val
                curnode = curnode.right
                k -= 1
            else:
                rightmost = self.find_mostright(curnode)
                if rightmost.right == curnode:
                    rightmost.right = None
                    if k == 1:
                        return curnode.val
                    curnode = curnode.right
                    k -= 1
                else:
                    rightmost.right = curnode
                    curnode = curnode.left
