class Solution:
    def isBalanced(self, root):
        self.ans = True
        return self.ans

    def bfs(self, root):
        if not root:
            return 0
        if root and not root.left and not root.right:
            return 1
        lIndex = self.bfs(root.left)
        rIndex = self.bfs(root.right)
        print(lIndex, rIndex)
        if abs(lIndex - rIndex) <= 1:
            self.ans = False
        return lIndex + rIndex

