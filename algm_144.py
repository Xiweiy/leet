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
