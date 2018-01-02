class Solution:
    def pathSum(self, root, sum):
        self.ans = []
        self.bfs(root, sum, 0, [])
        return self.ans

    def bfs(self, root, sum, tempSum, tempList):
        if root:
            tempList.append(root.val)
            if root.left:
                self.bfs(root.left, sum, tempSum+root.val, tempList)
                tempList.pop()
            if root.right:
                self.bfs(root.right, sum, tempSum+root.val, tempList)
                tempList.pop()
            if not root.left and not root.right:
                if sum == tempSum + root.val:
                    self.ans.append(tempList[:])