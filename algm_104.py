##SOLUTION 1
class Solution(object):
    def maxDepth(self, root):
        nodelist = [root]
        layerlist = [1]
        lastcount = 0
        while len(nodelist):
            curnode = nodelist[0]
            if curnode is not None:
                nodelist += [curnode.left, curnode.right]
                layerlist += [layerlist[0]+1, layerlist[0]+1]
                lastcount = layerlist[0]
            del nodelist[0]
            del layerlist[0]
        return lastcount

##SOLUTION 2
class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1




