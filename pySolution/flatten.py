class Solution:
    def flatten(self, root):
        self.stack = []
        self.bfs(root)
        self.toRight(root)

    def bfs(self, root):
        if root:
            if root.right:
                self.stack.append(root)
            if not root.left and self.stack:
                temp = self.stack.pop()
                root.left = temp.right
                temp.right= None
            self.bfs(root.left)

    def toRight(self, root):
        if root:
            root.right = root.left
            self.toRight(root.right)

