##SOLUTION 1: Recursive Solution
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.righti)

##SOLUTION 2: Iterative Solution
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        nodelist = [root]
        visited = [0]
        inorder = []
        while nodelist:
            if visited[-1]:  ##Left child added
                curparent = nodelist.pop()
                visited.pop()
                nodelist.append(curparent.right)
                visited.append(0)
            elif not nodelist[-1]:   ##Node is None
                nodelist.pop()
                visited.pop()
            else:      ##Before left child added
                visited[-1] += 1
                inorder.append(nodelist[-1].val)
                nodelist.append(nodelist[-1].left)
                visited.append(0)
        return inorder


##SOLUTION 3: Morris Traversal
class Solution(object):
    def find_mostright(self, root):
        if not root.left.right:
            return root.left
        else:
            curparent = root.left
            while curparent.right and curparent.right != root:
                curparent = curparent.right
            return curparent
        
    def preorderTraversal(self, root):
        if not root:
            return []
        curnode = root
        inorder = []
        while curnode:
            if not curnode.left: 
                inorder.append(curnode.val)
                curnode = curnode.right
            else:
                rightmost = self.find_mostright(curnode)
                if rightmost.right == curnode:
                    rightmost.right = None
                    curnode = curnode.right
                else:
                    inorder.append(curnode.val)
                    rightmost.right = curnode
                    curnode = curnode.left
        return inorder
