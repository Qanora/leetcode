class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        return self.build(None, nums)


    def build(self, root, nums):
        if nums:
            mid = int((len(nums)+1)/2)-1
            root = TreeNode(nums[mid])
            root.left = self.build(root.left, nums[:mid])
            root.right = self.build(root.right, nums[mid+1:])
            return root

Solution().sortedArrayToBST([-10,-3,0,5,9])