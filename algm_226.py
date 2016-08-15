###ITERATIVE SOLUTION
class Solution(object):
    def invertTree(self, root):
        nodelist = [root]
        while nodelist:
            curnode = nodelist[0]
            if curnode is not None:
                curnode.left, curnode.right = curnode.right, curnode.left
                nodelist += [curnode.left, curnode.right]
            del nodelist[0]
        return root


##RECURSIVE  SOLUTION
class Solution(object):
    def invertTree(self, root):
        if root is not None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            root.left, root.right = root.right, root.left
        return root
