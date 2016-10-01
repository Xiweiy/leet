##SOLUTION 1: RECURSIVE SOLUTION
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


##SOLUTION 2: ITERATIVE SOLUTION
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        nodelist = [root]
        visited = [0]
        inorder = []
        while nodelist:
            if visited[-1]:  ##Left child added
                curparent = nodelist.pop()
                visited.pop()
                inorder.append(curparent.val)
                nodelist.append(curparent.right)
                visited.append(0)
            elif not nodelist[-1]:   ##Node is None
                nodelist.pop()
                visited.pop()
            else:      ##Before left child added
                visited[-1] += 1
                nodelist.append(nodelist[-1].left)
                visited.append(0)
                
        return inorder
