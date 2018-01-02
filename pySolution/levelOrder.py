class Solution:
    def levelOrder(self, root):
        ans = []
        stack1 = [root]
        stack2 = []
        while stack1 or stack2:
            tempList = []
            while stack1:
                temp = stack1.pop()
                tempList.append(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            if tempList:
                ans.append(tempList)
            while stack2:
                stack1.append(stack2.pop())
