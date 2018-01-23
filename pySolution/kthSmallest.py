import TreeNodeUtils
class Solution:

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans = None
        self.find(root,0,k)
        return self.ans

    def find(self, root, temp, k):
        if root:
            temp = self.find(root.left, temp, k)
            temp += 1
            if k == temp:
                self.ans = root.val
            temp = self.find(root.right, temp, k)
        return temp


ans = TreeNodeUtils.make_tree([1,2,3])
Solution().kthSmallest(ans,5)