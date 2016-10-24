
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.memo = {}
        return self.helper(root)

    def helper(self, root):
        if not root:   # if not root
            return 0

        if root not in self.memo:  # if it is not in memo
            val = 0
            if root.left:  # we calculate not have left
                val += self.helper(root.left.left) + self.helper(root.left.right)
            if root.right: # we calculate not have right
                val += self.helper(root.right.left) + self.helper(root.right.right)
            f = root.val+val    # max include root
            s = self.helper(root.left) + self.helper(root.right) # max not include root
            self.memo[root] = max(f, s)
        return self.memo[root]
