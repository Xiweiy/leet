
class Solution(object):
    def sumOfLeftLeaves(self, root, isLeft=False):   
        
        if not root:
            return 0
        if not (root.left or root.right):
            return root.val*isLeft
        return self.sumOfLeftLeaves(root.left, isLeft=True) + self.sumOfLeftLeaves(root.right, isLeft=False)

