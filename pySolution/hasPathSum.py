class Solution:
    def hasPathSum(self, root, sum):
        if root:
            if root.left:
                root.left.val += root.val
            if root.right:
                root.right.val += root.val
            if not root.left and not root.right:
                if root.val == sum:
                    return True
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        return False