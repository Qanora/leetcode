class Solution:
    def minDepth(self, root):
        if root.left and not root.right:
            return self.bfs(root.left)
        if root.right and not root.left:
            return self.bfs(root.right)
        return min(self.bfs(root.left), self.bfs(root.right))

    def bfs(self, root):
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        lIndex = self.bfs(root.left)
        rIndex = self.bfs(root.right)
        return max(lIndex, rIndex)+1