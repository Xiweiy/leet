class Solution(object):
    
    def convertBST(self, root):
        self.sum = 0
        
        def computeSum(root):
            if not root:
                return root
            computeSum(root.right)
            self.sum += root.val
            root.val = self.sum
            if root.left:
                computeSum(root.left)
            return root
        
        return computeSum(root)


##NOTE: DFS solution, store values in a cumulative count as traversing through the tree, start from the rightmost node
