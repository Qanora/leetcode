class Solution:

    def sumNumbers(self, root):
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root:
            if root.left:
                root.left.val = root.left.val + root.val*10
                self.dfs(root.left)
            if root.right:
                root.right.val = root.right.val + root.val*10
                self.dfs(root.right)
            if not root.left and not root.right:
                self.ans += root.val
