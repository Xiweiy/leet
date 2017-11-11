class Solution(object):
    def trimBST(self, root, L, R):
        if root is None:
            return root
        if root.val <= R and root.val >= L:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L,R)
            return root
        if root.val < L:
            return self.trimBST(root.right,L,R)
        if root.val > R:
            return self.trimBST(root.left,L,R)
