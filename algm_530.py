##solution 1: (1) USE in-order traversal to return sorted array (2) then loop over the sorted array to find min
##            O(n) and O(n) time/space complexity
class Solution(object):
 
    def inorderTraversal(self, root):   #return a sorted array
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left)+ [root.val] + self.inorderTraversal(root.right)
    
    def getMinimumDifference(self, root):
        nodelist = self.inorderTraversal(root)
        minimum = 2147483647
        for i in range(len(nodelist)-1):
            absdiff = nodelist[i+1]-nodelist[i]
            if absdiff < minimum:
                minimum = absdiff
        return minimum

##solution 2: Morris traversal O(1) space and O(n) time

class Solution(object):
 
    def morrisTraversal(self, root):
        def findsmallestdiff(secondlargest, largest, smallestdiff):
            if largest-secondlargest < smallestdiff:
                smallestdiff = largest-secondlargest
            secondlargest = largest
            return secondlargest,smallestdiff
        
        secondlargest=-1000000
        smallestdiff = 2147483647
        
        cur = root
        while cur:
            if not cur.left:
                secondlargest,smallestdiff = findsmallestdiff(secondlargest, cur.val, smallestdiff)
                cur = cur.right
            else:
                pre = cur.left
                while (pre.right and pre.right != cur):
                    pre = pre.right
                
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:                
                    pre.right = None
                    secondlargest,smallestdiff = findsmallestdiff(secondlargest, cur.val, smallestdiff)
                    cur = cur.right
        return smallestdiff
            
    
    def getMinimumDifference(self, root):
        return self.morrisTraversal(root)
         
