class Solution:
    def preorderTraversal(self, root):
        self.ans = []
        return self.ans
    def preorder(self, root):
        if root:
            self.ans.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)