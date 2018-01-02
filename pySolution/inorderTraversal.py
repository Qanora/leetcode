class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self, root, ans):
        if root is None:
            return
        else:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)


Solution().inorderTraversal([1,None,2,3])