class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        stack1 = [root]
        stack2 = []
        while stack2 or stack1:
            pre = None
            while stack1:
                temp = stack1.pop()
                temp.next = pre
                pre = temp
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            while stack2:
                stack1.append(stack1.pop(0))