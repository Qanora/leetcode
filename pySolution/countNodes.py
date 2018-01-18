# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = 1
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp.left:
                stack.append(temp.left)
                count += 1
            if temp.right:
                stack.append(temp.right)
                count += 1
        return count
