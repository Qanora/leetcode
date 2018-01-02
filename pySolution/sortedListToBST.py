class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        self.node = head
        if not head:
            return None
        size = 0
        travel = head

        while travel:
            travel = travel.next
            size += 1
        return self.inorderHelper(0, size-1)

    def inorderHelper(self, start, end):
        if start > end:
            return None
        mid = start + int((end - start)/2)
        left = self.inorderHelper(start, mid - 1)
        root = TreeNode(self.node.val)
        self.node = self.node.next
        root.left =left
        root.right = self.inorderHelper(mid + 1, end)
        return root