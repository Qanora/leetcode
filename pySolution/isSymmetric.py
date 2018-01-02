class Solution:
    def isSymmetric(self, root):
        return self.travel(root,root)

    def travel(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and self.travel(t1.right,t2.left) and self.travel(t1.left, t2.right)
