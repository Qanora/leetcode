class Solution:
    def isSameTree(self, p, q):
        return self.travel(p, q)

    def travel(self, pRoot, qRoot):
        if not pRoot and not qRoot:
            return True
        if (not pRoot and qRoot) or (not qRoot and pRoot):
            return False
        if pRoot.val == qRoot.val:
            return self.travel(pRoot.left, qRoot.left) and self.travel(pRoot.right, qRoot.right)
        return False