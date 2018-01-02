class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, minN, maxN):
        self.ans = []
        for i in range(1, len(self.ans)):
            if self.ans[i] <= self[i-1]:
                return False
        return True

    def travel(self,root):
        if root:
            self.travel(root.left)
            self.ans.append(root.val)
            self.travel(root.right)