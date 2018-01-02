class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        stack1 = [root]
        stack2 = []
        count = 0
        while stack2 or stack1:
            while stack1:
                temp = stack1.pop()
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            count += 1
            while stack2:
                stack1.append(stack2.pop())
        return count