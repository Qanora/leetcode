import TreeNodeUtils
class Solution(object):
    def lowestCommonAncestor_235(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor_235(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor_235(root.right, p, q)
        else:
            return root

    def lowestCommonAncestor_236(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack_p = []
        stack_q = []
        self.dfs(root, p, stack_p)
        self.dfs(root, q, stack_q)
        ans = None
        for val in stack_q:
            if val in stack_p:
                ans = val
                break
        return ans

    def dfs(self, root, p, stack):
        if root:
            if root.val == p:
                stack.append(root)
                return True
            if self.dfs(root.left, p, stack) or self.dfs(root.right, p, stack):
                stack.append(root)
                return True
            return False

s = TreeNodeUtils.make_tree([1,2,3,4,5,6,7,8])
temp = []
w = Solution().lowestCommonAncestor_236(s, 1, 8)
print(w)

